# Installation
Make sure to update and upgrade your system

`sudo apt update`

`sudo apt upgrade`

Add Repo key to OS (Only on Ubuntu 20.04)

`sudo apt-key adv --fetch-keys 'https://mariadb.org/mariadb_release_signing_key.asc'`

Add Repo to system

`sudo add-apt-repository 'deb [arch=amd64] http://mariadb.mirror.globo.tech/repo/10.5/ubuntu focal main'`

Update and install

`sudo apt update`

`sudo apt install mariadb-server mariadb-client`

Now you can run installation

`sudo mysql_secure_installation`

- - - -

# System Checks

`sudo systemctl status mariadb`
