# Networking

## Check own IP
Returns your public IP
`curl http://icanhazip.com`

## Hosts File and IPs
Print available IPs and their mappings for local machine
`nano /etc/hosts`

Edit this file for IP mappings

```bash
127.0.0.1 domain.touse.local #Comment
```

- - - -

# IP Assignments
Check network hardware and the IPs assigned to them (Ethernet, WiFi, etc)

`ip a`

## Network Statistics
Netstat tool to see which IPs and Ports you have open on your local machine

Linux Standard

`ss`

- - - -

# Network Statistics (NetStat)
General Use

`sudo netstat`

Concise List

`sudo netstat -tulpn`

Search for specific

`sudo netstat -tulpn | grep -e "localaddress" -e "maria"`

- - - -

# Firewalls / Connections

## UWF
Built-in firewall that comes with Ubuntu

Check status of the firewall

`sudo ufw status`

Deny all incomming connections by default

`sudo ufw default deny incoming`

Allow all outgoing connections by default

`sudo ufw default allow outgoing`

Adding rules to firewall, like allowing SSH incoming only on a specific port

`sudo ufw allow 22/tcp comment 'SSH'`

You can add a comment, 22 is standard port for SSH but can change to be more secure

If running a server, allow HTTP and HTTPS incoming connections

`sudo ufw allow http`

`sudo ufw allow https`

Once you want to save your changes, enable ufw or reload if enabled already

`sudo ufw enable`

`sudo ufw reload`

To delete an existing rule listed in `sudo ufw status`
(Number is position in list)

`sudo ufw delete 1`
