# Install Docker - Rootless
It's safer to use rootless.. you will need to download the setup script.

Make sure the `uidmap` and `dbus-user-session` package is installed
Install the following packages:
```bash
sudo apt install uidmap
sudo apt install dbus-user-session
sudo apt install docker-ce-rootless-extras
```
Install them and re-login to save

Check /etc/subuid and /etc/subgid for UID and GID

Now you can run `dockerd-rootless-setuptool.sh` as a non-root user

If Docker is installed, you may have that command already installed.

Make sure to export the environment variables

Usually the sock is set to $XDG_RUNTIME_DIR/docker.sock by default.. usually /run/user/$UID

The daemon config is set to ~/.config/docker

`export DOCKER_HOST=unix://$XDG_RUNTIME_DIR/docker.sock`

Add to .bashrc to make it easier!

# Starting Daemon
Now you can start the daemon as a non-user..

Make sure the system daemon isn't running

`sudo systemctl stop docker.socket`

`sudo systemctl stop docker.service`

Start the user daemon

`systemctl --user start docker`

Once it's all started you can enable the service

`systemctl --user enable docker`

`sudo loginctl enable-linger $(whoami)`

- - - -

# Maintainance 
The service will be saved per user, check status

`systemctl --user status docker`


