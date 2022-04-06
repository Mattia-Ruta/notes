# OpenVPN for Linux CLI
## Installation
Using Surfshark, go to https://my.surfshark.com/vpn/manual-setup/main
Save your username and password

Navigate to /etc/openvpn and download configurations for Surfshark

`cd /etc/openvpn`

`sudo wget https://my.surfshark.com/vpn/api/v1/server/configurations`

Unzip configs

`sudo unzip configurations`

## Connecting

In /etc/openvpn you will see all the servers you can connect to

(Examples)
* uk-lon-st001.prod.surfshark.com_tcp.ovpn
* us-nyc-st001.prod.surfshark.com_tcp.ovpn

run openvpn using the file and enter creds from the site

`sudo openvpn uk-lon-st001.prod.surfshark.com_tcp.ovpn`
