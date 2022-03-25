# Apache

## Installing/Updating
`sudo apt update`
`sudo apt install apache2`
Install Mariadb using Mariadb notes

## Content Directory
Default directory for webhosting
`cd /var/www/html`
If you're hosting multiple sites, you can add a folder inside called the website

## Configuration
All configuration is inside
`cd /etc/apache2`

## Main Configuration
Main configurations, contains global configs
`nano /etc/apache2/apache2.conf`

## Port Configuration
Port config file
`nano /etc/apache2/ports.conf`
Default port is 80
If SSL is enabled, port 443 is also enabled

## Sites Available
Stores site-specific config files for each virtual host
`cd /etc/apache2/sites-available/`

## Sites Enabled
Stores sites that have been enabled. Apache will read the files here to complete config
`cd /etc/apache2/sites-enabled/`

## Server Logs
Logs are stored in /var/log/apache for access and error logs
`nano /var/log/apache2/access.log`
`nano /var/log/apache2/error.log`

## Enabling and Disabling a site
To enable
`sudo a2ensite DOMAIN.conf`

To disable
`sudo a2dissite DOMAIN.conf`

# Apache Server
Restart server
`sudo systemctl restart apache2`

Soft reset (For changes just in configs)
`sudo systemctl reload apache2`
