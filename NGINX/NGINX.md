# Basic Usage

## Installation 

`sudo apt install nginx`

## Basic Commands
Use systemctl to command NGINX

General Use

`sudo systemctl [Command] nginx`

Commands

* start
* stop
* status
* restart | Restarts complete server
* reload | Reloads config and restarts gracefully

You can also restart the server through NGINX command signals

`sudo nginx -s [restart | reload]`

# Configuration
Inside /etc/nginx/sites-available lives your config files.
Normally a site stays in /var/www/html or /data/www, which you'll have to specify.
You can also server static files, usually in /data/static.


```bash
server {
    location / {
        root /data/www;
    }

    location /images {
        root /data;
    }
}
```
