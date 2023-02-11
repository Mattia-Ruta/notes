# Install Docker - Rootless
It's safer to use rootless.. 

# Pre-req's

Make sure the following packages are installed (apt):
1. uidmap
2. dbus-user-session


Install them and re-login to save

Check /etc/subuid and /etc/subgid for UID and GID

# Install Docker
If you have Docker installed system wide already, check if you have the rootless setup already..

Same place as Docker, usually /usr/bin/

Try `dockerd-rootless-setuptool.sh` as a non-root user

If you don't have that command, try downloading the script from https://get.docker.com/rootless

Running the script as a non-root user, it will install a socket and create a user service

Locations:

* Socket - $XDG_RUNTIME_DIR/docker.sock (usually /run/user/$UID)
* Daemon Config - ~/.config/docker

# Setup and Environment Variables

Make sure to export the environment variable needed for docker

`export DOCKER_HOST=unix://$XDG_RUNTIME_DIR/docker.sock`

This gives Docker the location of the socket to connect to

Add to ~/.bashrc to avoid it disappearing

# Starting Daemon and Maintainance
Now you can start the daemon as a non-user!

Make sure the system daemon isn't running

`sudo systemctl stop docker.socket`

`sudo systemctl stop docker.service`

Start the user daemon

`systemctl --user start docker`

Once it's all started you can enable the service

`systemctl --user enable docker`

`sudo loginctl enable-linger $(whoami)`

Test docker works by running a quick hello-world

`docker run hello-world`

If all is good and non-root user can use docker, you can disable the system-wide socket/service

`sudo systemctl disable docker.socket`

`sudo systemctl disable docker.service`

- - - -

# Install Docker Compose Plugin
You will have to install using the repo.. check the following link:

https://docs.docker.com/compose/install/compose-plugin/#install-using-the-repository

It will probably say to make the directory for 

`DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}`

`mkdir -p $DOCKER_CONFIG/cli-plugins`

Find the curl command (something like curl -SL https://github.com/docker/compose/releases/download.......)

Make the plugin executable

`chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose`

Test with a version call

`docker compose version`

# Maintainance 
The service will be saved per user, check status

`systemctl --user status docker`


