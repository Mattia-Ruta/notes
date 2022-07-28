# Installation
`sudo apt install network-manager`

# Switching to NetworkManager from Netplan
If current setup is using netplan instead of nmcli, check the /etc/netplan/*.yaml file

Change to this to change manager to nmcli

```bash
network:
  version: 2
  renderer: NetworkManager
```

*Make sure you're not SSH'd into a computer before changing this!*

Then apply using `sudo netplan apply`

Restart nmcli to apply changes

`sudo systemctl restart NetworkManager`

# Network Devices - Hardware
Use nmcli to find info on hardware and what they're connected to

`nmcli`

General Status

`nmcli general` or `nmcli g`

Compact list of devices

`nmcli device` or `nmcli d`

Once you get a list you can find more info on a specific device

`nmcli device show enx0050b627afcf`

This will also print info on which DNS servers it's using

# Changing DNS
`nmcli c` will show connections, copy ID and use for following

`nmcli c mod <UID> ipv4.dns "1.1.1.1 1.0.0.1"`

`nmcli c mod <UID> ipv4.ignore-auto-dns yes`

`nmcli c mod <UID> ipv6.dns "2606:4700:4700::1111 2606:4700:4700::1001"`

`nmcli c mod <UID> ipv6.ignore-auto-dns yes`

Now reset connection

`nmcli c down <UID>`

`nmcli c up <UID>`

Check with /etc/resolv.conf to make sure it worked. 

If not edit file `/etc/resolv.conf` and add

```bash
nameserver 1.1.1.1
nameserver 1.0.0.1
```


# Connections
Print all connections, including past WiFi connections

`sudo nmcli connection`

## Add Connection
Add a new connection using ethernet device

Make sure you get dev name from device list using `nmcli d`

`nmcli con add type ethernet con-name connection-name1 ifname eth0`

Or add one with static IP

`nmcli con add type ethernet con-name connection-name2 ifname enp0s3 ip4 192.168.1.50/24`

## Modify Connection
Modify connection by adding DNS ipv4

`nmcli con mod conn1 ipv4.dns "1.1.1.1 1.0.0.1"`

Set Auto-Connect on or off

`nmcli con mod conn1 connection.autoconnect no`

Add users to allow connection modification

`nmcli con mod conn1 connection.permissions user:user1,user2,user3`

*Make sure to reset connection after modifying it*

`nmcli con down conn1`

`nmcli con up conn1`

## Up / Down Connections
Connect to a connection using up, or disconnect using down

`nmcli con down con1`

Or two commands at once

`nmcli con down conn1 ; nmcli con up conn2`

## Search and Connect to WiFi
Search WiFi signals around

`nmcli d wifi list`

Connect to WiFi from list using BSSID or SSID

`nmcli d wifi connect <SSID>`

Enter password when prompted or use following to ask in CLI

`nmcli --ask d wifi connect <SSID>`
