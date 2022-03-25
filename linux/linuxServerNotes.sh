#Before doing anything, make sure you have Apache2 installed

#Updates the system
sudo apt update
#Check where a binary is installed
which ssh


#Installs apache2
sudo apt install apache2

#Checks to see if it installed correctly
sudo apache2ctl configtest
#Will run a configeration test and return error for server name
#If servername error, you have to set it

#You can edit the config file
sudo nano /etc/apache2/apache2.conf
#At the end of the file, add this line:
ServerName 127.0.0.1
#This sets the servername to the IP

#Check the configeration test again to see if your IP worked

#Once the syntax is okay you can restart apache2
sudo systemctl restart apache2
#^Restarts apache2^

#To be able to edit the root folder you have to set permissions
sudo chmod 777 /var/www/html

#Now you have to install the MySQL server
sudo apt install mysql-server

#You can install php libraries for SQL server
sudo apt install php libapache2-mod-php php-mcrypt php-mysql

#You can change php priority over HTML files by editing config
sudo nano /etc/apache2/mods-enabled/dir.conf
#Once inside this file, add index.php to the DirectoryIndex
#Make sure index.php is before index.html!
#Delete the second iteration of index.php later in the line

#Restart apache2 to save those changes
sudo systemctl restart apache2

#Now you can create an index.php file in the html folder!
#Install phpmyadmin to controll sql server etc
sudo apt install phpmyadmin
#Say yes to the prompts and put the password for the sql server

#Communicate to apache2 that an SQL server exists
sudo nano /etc/apache2/apache2.conf
#Go to the bottom of the document, after ServerName
Include /etc/phpmyadmin/apache.conf

#Restart apache2 again because you edited config files
sudo systemctl restart apache2

#Now the phpmyadmin account should be working
#Go to localhost/phpmyadmin/ to see if the admin site works
#Login with username root and the password of the SQL server
