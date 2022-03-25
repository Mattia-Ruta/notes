# Gunicorn
Python package to run WSGI applications

## Installation
Using pip3 \
`pip3 install gunicorn`

## General Use
You need to have a WSGI application to run gunicorn, access the application using python objects

For Django, inside the main project dir where manage.py is \
`gunicorn --bind 0.0.0.0:8000 applications.wsgi:application`

Accesses applications as the python module and binds it to any IP that enters to the 8000 port, the wsgi.py file inside is the submodule, and the :application is the application object inside the wsgi.py script

Now that we know we can serve the project, we can create the systemd service

## Gunicorn Systemd Service
Add gunicorn as a service to systemd \
`sudo nano /etc/systemd/system/gunicorn.service`

Create the service file:
```
[Unit]
Description=Gunicorn Daemon
After=network.target

[Service]
User=sammy
Group=www-data
WorkingDirectory=/path/to/project
ExecStart=/path/to/project/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/tmp/project.sock project.wsgi:application

[Install]
WantedBy=multi-user.target
```

*Make sure to place the socket in a directory open to everyone, make a new folder in root maybe*

This creates the service, so we can start and stop using our system controller

`sudo systemctl start gunicorn`

`sudo systemctl enable gunicorn`

We can check this worked by looking for the socket file we created in the service



# NGINX
Server that routes the incoming requests to either the:
* Static Directories
* Media Directories
* Gunicorn application running

## Installation
Install as Aptitude package \
`sudo apt install nginx`

## Sites Available
In /etc/nginx/sites-available you can create a new server block for your site

`sudo nano /etc/nginx/sites-available/project.conf`

Listen to requests on port 80 and ignore errors on finding favicon.ico

```
server {
    listen 80;
    server_name domain.co.uk;
    # Or can use server_name IP instead

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static {
        alias /var/www/html/project.co.uk/static;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/path/to/project/project.sock;
    }
}
```

The / location passes the requests that aren't static to the gunicorn socket we create with the gunicorn service

Link the config file into sites-enabled to enable the site \
`sudo ln -s /etc/nginx/sites-available/project.conf /etc/nginx/sites-enabled`

Test config file for syntax errors \
`sudo nginx -t`

If no errors, you can restart NGINX to save \
`sudo systemctl restart nginx`

## Firewall Settings
Make sure to open your firewall to allow these requests into the project

`sudo ufw delete allow 8000`

`sudo ufw allow 'Nginx Full`

This will disallow port 8000 connections and let you connect to your server on port 80 as normal HTTP.

# Next Steps
Be sure to secure traffic after using SSL/TLS. Let's Encrypt is a good option

If you don't have let's encrypt for SSL, you can use a self-assigned certificate until you do.

# Self-Assigned Certificate
## Create self-assigned key
`sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt`

* OpenSSL manages SSL certs
* req created an x509 type of key
* nodes skips passphrase option
* days sets the amount of days we want the certificate valid
* newkey says we want to make a new cert and a new key at the same time
* keyout tells where to place the private key
* out tells where to place the cert

## Prompts
This will ask you a few questions about the certificate

* Country Name: UK
* State of Province: 
* Locality Name: London
* Organization Name: Applications
* Organizational Unit:
* Common Name: 123.123.123.123
* Email Address: admin@admin.co.uk

## Diffie-Hellman Group
Negotiates secrecy with clients

`sudo openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048`

This will take a while but will create a strong DH group.

- - - -

# NGINX Config for SSL
We want to configure NGINX to use our certs and keys to secure the connection to our server. Use multiple server blocks to filter requests based on security and filter out bad requests without a Host

````bash
# Return 444 and close if no Host header
server {
    listen 80 default server;
    return 444;
}

# Redirect HTTP to HTTPS
server {
    server_name domain.co.uk www.domain.co.uk;
    listen 80;
    return 307 https://$host$request_uri;
}

# Main server block
server {
    # Static Files
    location /static {
        autoindex on;
        alias /path/to/static;
    }

    # Proxypass to server
    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Host $http_host;
        proxy_ssl_server_name on;
        proxy_pass http://unix:/path/to/gunicorn.sock;
    }

    # SSL
    listen 443 ssl;

    ssl_certificate /path/to/fullchain.pem
    ssl_certificate_key /path/to/privkey.pem
    include /etc/letsencrypt/options-ssl-nginx.conf; # Usually added by certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # Usually added by certbot
}
````