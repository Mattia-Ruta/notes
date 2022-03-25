# Installation
Installing parts of the LAMP stack
Linux Apache MySQL PHP

## Apache2
Install Apache2
`sudo apt update`
`sudo apt install apache2`

## PHP
Install PHP and Mods
`sudo apt install php libapache2-mod-php php-mcrypt php-mysql`

## MariaDB/MySQL
Install MariaDB
`sudo apt install mysql-server`

Run secure installation
`mysql_secure_installation`

# Setup and Configuration

## Apache2
You'll have to set a global server name
`sudo nano /etc/apache2/apache2.conf`

Add a line at the bottom of the file for the ServerName
`ServerName 127.0.0.1`

Or you can name the server
`ServerName example.com`

To add a site to your server, you'll need to add it to the `sites-available` dir
`sudo nano /etc/apache2/sites-available/site.com.conf`

Inside this conf, add VirtualHost

````bash
<VirtualHost site.com:80>
  ServerAdmin admin@gmail.com
  ServerName site.com
  ServerAlias www.site.com
  DocumentRoot /var/www/html/site.com/public_html
</VirtualHost>
````
80 is the default port for HTTP

Enable Site using conf file
`sudo a2ensite site.com.conf`

Disable a Site if you need
`sudo a2dissite site.com.conf`

Check with Apache that the syntax is okay
`sudo apache2ctl configtest`

Always restart Apache when making changes to config
`sudo systemctl restart apache2`

Check the status of Apache service
`sudo systemctl status apache2`

## PHP
By default Apache looks for an HTML file first, you can adjust the priority list
`sudo nano /etc/apache2/mods-enabled/dir.conf`

```bash
<IfModule mod_dir.c>
  DirectoryIndex index.html index.cgi index.pl index.php index.xhtml index.htm
</IfModule>
```

Remember to restart Apache after adjusting conf files

## PHPMyAdmin
Install PHP Myadmin
`sudo apt install phpmyadmin`

Include conf in `/etc/apache2/apache2.conf`:
```bash
Include /etc/phpmyadmin/apache.conf
```

Remember to restart apache after adjusting conf files

Once PHPMyAdmin is installed, you should be able to view it
http://localhost/phpmyadmin
Login using db credentials

# Serving PHP Files
By default Apache will look in `/var/www/html` for files in the <DirectoryIndex> list
Adding a `info.php` file with just

```php
<?php
phpinfo();
```
And navigating to servername/info.php should show a PHP info page
