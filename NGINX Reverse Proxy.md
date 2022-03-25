# Installation
Install as Aptitude package \
`sudo apt install nginx`

- - - -

# Server Setup
NGINX 

## Sites Available
In /etc/nginx/sites-available you can create a new server block for your site

`sudo nano /etc/nginx/sites-available/project.conf`

`Listen` - Set the port the server will listen on.
If you have multiple server {} blocks, it will use the server based on the `server_name`, but if it can't match a request it will default to the first in the list or the one set as `default_server`.

`server_name` - The name of the server {} block, NGINX will use these names in the request to decide which server to use

### Location Configuration

`location` (favicon.ico)- These settings turn off error reporting if a favicon is missing

`location` - Passes a specific request depending on the request. `/` is root so domain.co.uk resolves here, running the configuration in the {} block for that request. `domain.co.uk/static/` instead resolves to the /static {} block, where it serves the files from the alias directory configured

```
server {
    # Listen on port 80, can set this setup as default server
    listen 80 default_server;

    server_name domain.co.uk www.domain.co.uk;

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

- - - -

# Reverse Proxy Configuration

You can have NGINX be the middle ground between a backend application and the front-facing server. A reverse proxy is when the application makes a proxy instead of the client/user. In this case an app listening on port 99 is using NGINX to proxy requests so the requests to the server is maintained by NGINX

````bash
server {
    listen 80;
    server_name domain.co.uk;

    # Place to pass all requests to
    location / {
        proxy_pass http://123.123.123.123:99;
    }

    # Proxy Header Settings
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

    # (Optional) Log Settings
    access_log /var/log/nginx/sitename.log;
}

````

The proxy will take all incoming requests on port 80 and forward them to the link you provide

# Enabling SSL and HTTPS

## Install
Install certbot and the Python3 plugin for renewals

`sudo apt install certbot`

`sudo apt install python3-certbot-nginx`

## Running Certbot
Run certbot and make sure you use the correct module for the server you have. You also need a domain that maps to the IP and can connect to it

`sudo certbot --nginx -d lupino-server.co.uk`

## Renewal
It will try to renew SSL certificates when it runs out but you can test if the renewal would work

`sudo certbot renew --dry-run`