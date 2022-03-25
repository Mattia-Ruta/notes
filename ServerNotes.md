# General Server Notes

## Initialising Server

Once you have a server ready, connect to it via SSH using the user @ server IP

`ssh root@123.123.123.123`

Make sure you update and upgrade

`sudo apt update`

You can change the device name to something meaningful

in /etc/hostname, change localhost to anything you want

`computerName`

Name the hosts/IP the same name
in /etc/hosts

`127.0.1.1  computerName`

Restart the server to save changes

Make sure to add a user that isn't root \
`sudo useradd -m newuser`

-m creates a home directory

Add user to sudoers \
`visudo`

Add user to file \
`username ALL=(ALL) NOPASSWD:ALL`

- - - -

## Gunicorn and NGIX

### Gunicorn
Install Gunicorn

`sudo pip3 install gunicorn`

Create config file for gunicorn
Normally named gunicorn.conf.py
conf files are usually places inside /etc

````python
command = '/home/user/project.co.uk/appenv/bin/gunicorn'
pythonpath = '/home/user/project.co.uk'
bind = '123.12.123.123:8000'
workers = 3
````
Be sure to use python environment or wherevner gunicorn is located
pythonpath is for main project location
bind to server's IP and port

Running gunicorn using conf file

`gunicorn -c gunicorn.conf.py project.wsgi`

### NGINX
Install NGINX

`sudo apt install nginx`

Config file for NGINX

````bash
server {
  listen 80;
  server_name 123.123.123.123;

location /static/ {
  root /home/user/project/static/;
}

location / {
  proxy_pass http://123.123.123.123:8000;
  }
}
````

- - - -

## Basic Server Commands

Check the uptime

`uptime`
