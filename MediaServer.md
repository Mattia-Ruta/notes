# Dependencies for All
Install dependencies

`sudo apt install gnupg ca-certificates`

Install Mono by going to their site and following directions

https://www.mono-project.com/download/stable/#download-lin

```bash
sudo apt install gnupg ca-certificates
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
echo "deb https://download.mono-project.com/repo/ubuntu stable-focal main" | sudo tee /etc/apt/sources.list.d/mono-official-stable.list
sudo apt update
sudo apt install mono-devel
```

Test it works using basics

https://www.mono-project.com/docs/getting-started/mono-basics/

Install Radarr dependencies

`sudo apt install mediainfo`

## Mono
Mono is the package used to run these services, you can test they work by running the .exe's using mono.

`mono /opt/Radarr/Radarr.exe`

- - - -

# SABNZBDPlus | Downloader
Downloader process

Add Repo to Aptitude

`sudo add-apt-repository ppa:jcfp/nobetas`

Update and Upgrade Aptitude

`sudo apt update`

`sudo apt upgrade`

Install package

`sudo apt install sabnzbdplus`

Open and start using

`sabnzbdplus`

Maps to localhost:8085 or

http://127.0.0.1:8081/sabnzbd

To allow others to connect to server, open port by editing config:

`sudo nano /etc/default/sabnzbdplus`

And adding a host as `0.0.0.0`

Make sure to restart process when editing this file

- - - -

# Radarr | Films
App for Films

Download tar file for Radarr
*Make sure you're in Downloads*

`curl -L -O $( curl -s https://api.github.com/repos/Radarr/Radarr/releases | grep linux.tar.gz | grep browser_download_url | head -1 | cut -d \" -f 4 )`

Open tar file

`tar -xvzf Radarr.*.linux.tar.gz`

Move Radarr to /opt

`sudo mv Radarr /opt`

Add Radarr to systemd by creating a service

`sudo nano /etc/systemd/system/radarr.service`

Create the radarr.service file:

````bash
[Unit]
Description=Radarr Daemon
After=syslog.target network.target

[Service]
User=mattia
Group=mattia

Type=simple

ExecStart=/usr/bin/mono --debug /opt/Radarr/Radarr.exe -nobrowser
TimeoutStopSec=20
KillMode=process
Restart=on-failure

[Install]
WantedBy=multi-user.target
````

Enable the Service
`sudo systemctl enable --now radarr.service`

- - - -

# Sonarr | Series
App for TV Series

Add Sonarr key

`sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 0xA236C58F409091A18ACA53CBEBFF6B99D9B78493`

Add Sonarr package to Aptitude

`echo "deb http://apt.sonarr.tv/ master main" | sudo tee /etc/apt/sources.list.d/sonarr.list`

Update packages

`sudo apt update`

Install Sonarr (Originally nzbdrone)

`sudo apt install nzbdrone`

Create the sonarr.service

`sudo nano /etc/systemd/system/sonarr.service`

Add service file:

````bash
[Unit]
Description=Sonarr Daemon
After=network.target

[Service]
User=mattia
Group=mattia

ExecStart=/usr/bin/mono --debug /opt/NzbDrone/NzbDrone.exe -nobrowser

Type=simple
TimeoutStopSec=20
KillMode=process
Restart=on-failure

[Install]
WantedBy=multi-user.target
````

Enable the service

`sudo systemctl enable --now sonarr.service`

# Lidarr | Music
App for music

Download tar
*Make sure you're in downloads*

`wget https://github.com/lidarr/Lidarr/releases/download/v0.7.2.1878/Lidarr.master.0.7.2.1878.linux.tar.gz`

Install using tar

`tar -xvzf Lidarr.*.linux.tar.gz`

Move Lidarr to /opt

`sudo mv Lidarr /opt`

Create lidarr.service

`sudo nano /etc/systemd/system/lidarr.service`

````bash
[Unit]
Description=Lidarr Daemon
After=syslog.target network.target

[Service]
User=mattia
Group=mattia

Type=simple

ExecStart=/usr/bin/mono --debug /opt/Lidarr/Lidarr.exe -nobrowser
TimeoutStopSec=20
KillMode=process
Restart=on-failure

[Install]
WantedBy=multi-user.target
````

Enable service

`sudo systemctl enable --now lidarr.service`

- - - -

