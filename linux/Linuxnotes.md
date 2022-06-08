# General Linux and Linux Server Notes


## Check Linux Version
`lsb_release -a`

Pretty-print version with info

`screenfetch`
# Users and Groups
## Add User
Make sure to add a user that isn't root

`sudo adduser [Options] newuser`

Adding a System User

`sudo adduser --system --no-create-home systemuser`

Add user to sudoers

`sudo visudo`

Add user to file

`username ALL=(ALL) NOPASSWD:ALL`

## Delete User
General Use

`sudo deluser [Options] user`

## Change Password for User

Change for current user

`passwd`

Using Root user, change password for other user

`sudo passwd username`

# Create Group

`sudo groupadd [Options] new_group`

Options

* -f | Force - Will force create even if it exists
* -s | System - Will create a system group and assign a group ID from system range

# Add User to Group

`sudo usermod -a -G groupName userName`

* -a | Append - Will append to group the user
* -G | Group - Groups to append to

- - - -

## Symbolic Links (Like shortcuts on Windows)
Links a copy or symbol to an original file

-s | Symbolic Link

General Use

`ln -s /full/path/original /full/path/link`

Remove Link (Doesn't affect original file)

`rm /path/to/link`

## Downloading and opening .deb packages
cd into the /tmp folder or ~/Downloads and get package:

`wget https://packages.site.com/package.deb`

General Use:

`dpkg [Options] package.deb`

Options
-c | Contents, shows contents in ll format
-I | Info, check info for the package
-i | Install, to install packages
-l | List, to list installed packages
-r | Remove, to remove package except conf files
-P | Purge, removes package and conf files

Installing package:

`sudo dpkg -i package.deb`

- - - -

# Changing Keymappings
Print characters to find KeyCode and KeySym Name for keys

`xmodmap -pk`

Run commands to change characters

`xmodmap -e "keycode 29 = z"`

`xmodmap -e "keycode 52 = y"`

To keep between reboots, create following file ~/.config/autostart/swap.desktop

```bash
[Desktop Entry]

Name=Swap
Exec=xmodmap -e "keycode 29 = z" && xmodmap -e "keycode 52 = y"

Terminal=false

Type=Application
```

- - - -

## Surfshark-vpn
Start VPN

`sudo surfshark-vpn`

Stop VPN

`sudo surfshark-vpn down`

Check Status

`sudo surfshark-cpn status`

## TR
Translate translates or deletes characters from an output



## SSH - Key Generation
Generate Public and Private Keys

General Use

`ssh-keygen [options]`

Options

-t | Type, rsa is standard
-b | Bitlength, 4096 is a safe length
-C | Comment, like a title for the key

## SSH - Adding Key to Remote Server
Add key on local to remote server

General Use \
`ssh-copy-id [Options] user@remote-ip`

Options \
-i | IdentityFile, public key to add \
-n | No Key, dry run and just print what it would add \
-p | Port, specify port (Default 22)

Add key to remote server \
`ssh-copy-id -i ~/.ssh/private_key mattia@192.168.15.118`

## SSH - Server Setup
Server SSH config file is:

/etc/ssh/sshd_config

Some options to consider:

Use Password to connect:

`PasswordAuthentication yes`

Use Public Key to connect:

`PubkeyAuthentication yes`

Anytime you change config, make sure to restart ssh server \
`sudo systemctl restart sshd`

- - - -

## Format Harddrives
Format the drive and mount it to the OS

*Make sure you use the right drive, this will format it!*

Use cfdisk for an easy graphical way

`sudo cfdisk /dev/sda`

Create filesystem and format to ext4 system - Default for Linux and good until 50TB or so

`sudo mkfs -t ext4 /dev/sdb`

- - - -

## Mount and Unmount

Create the directory to mount to

`sudo mkdir /mnt/drive_name`

Be sure to give yourself permission to use it

`sudo chown -R user:group /mnt/drive_name`

Mount drive to folder

`sudo mount /dev/sdb /mnt/drive_name`

Check UUID of Harddrives

`sudo blkid`

Nano into /etc/fstab and add your HD UUID so it will auto-mount
add your harddrive and mount point

`UUID="afd7cf7e-a24c-4b34-8cfb-1a030418b5cd" /mnt/media ext4 defaults,nofail 0 2`

Unmount

`sudo umount /mnt/drive_name`

Mount all HDDs in fstab file

`sudo mount -a`

# Disk Usage
Check disk usage for current directory

General Use

`du [Options] <dir>`

Options

* -s | Summary - Displays a summary for files
* -h | Human - Makes human readable

# Journalctl Logs
Rotate logs

`sudo journalctl --rotate`

Clear logs using days

`sudo journalctl --vacuum-time=2days`

Clear logs using size

`sudo journalctl --vacuum-time=100M`

- - - -

# CRON
Running crons are jobs done at specific times

## Install/Enable
Install if not installed already

`sudo apt install cron`

To enable crons run

`sudo systemctl enable cron`

## Editing Crontab
To edit user crontab

 `crontab -e`

To add an entry, it needs to be formatted a certain way

```
MM | HH | Day of Month | Month | Day of Week | Command
dom - 1 to 31
mon - 1-12 or JAN-DEC
dow - 0-6 or SUN-SAT

Shortcuts like @daily, @hourly, @reboot or @monthly can work
```

*Make sure to use absolute paths, even for the commands*

To check which command path run (For example bash)

`which bash`

Then use that absolute path in the cron

```
m h dom mon dow command
* 5 * * * /usr/bin/bash /location/of/script.sh >> /location/of/output.log
```
In this example, the cron will run every day at 05.00 and output to a log

 - - - -

### Extend LV
To extend the LV, you'll need to extend the PV and VG first

Extend PV to max size:
`sudo pvresize /dev/sda3`

Find absolute path to LV you want to resize by running

`sudo lvdisplay`

Expand LV to max size (using full LV path):
`sudo lvresize -l 100%FREE /dev/mapper/ubuntu--vg-ubuntu--lv`

Expand Filesystem in LV to max:
`sudo resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv`

- - - -

## RSync
Tool for copying and moving files \
*This won't re-copy files that exist in destination already, so you can run the same command multiple times*

General Use \
`rsync [Options] <src> <dest>`

src: without trailing \ will copy the folder, while with the trailing \ copies the contents of that folder

Options

a | Archive, keeps permissions and copies recursively, best used with \
n | --dry-run, Just prints what it would copy over \
P | Progress, shows progress, good for remote connections \
v | Verbose, shows more info \
z | Compresses files, good for remote connections \
--delete | Will delete files on dest, meant to make them mirror each other

Copy files locally \
`rsync -avP source/ dest/` \
Will show progress while copying files

Copy files to remote server \
`rsync -avzP /var/log user@123.123.123.123:/var/backup` \
If you don't specify a destination dir, it'll default to /home/user/

Copy files without archiving, recursivly \
`rsync source/ dest/` \
This will not copy permissions

Mirror two directories, src to dest  \
*THIS WILL DELETE EXTRA FILES IN DEST* \
`rsync -avP --delete --dry-run /var/log/ /mnt/backup/` \
*Use with caution, always dry run first*


## SSHFS - SSH Filesystem
Mount Remote Servers

`sshfs remote@remoteIP:/path/dir/remote /path/dir/local`

## Glances
General Check drives and RAM usage

`sudo apt install glances`

Glance at system running tasks and CPU, memory usage, etc

`glances`

## ZFS - Package for Harddrive management and Volume Manager
Zeta File System

`sudo apt install zfsutils-linux`

List drives and RAID arrangement

`zpool status`

- - - -

## Temperature Management

LM Sensor

`sudo apt install lm-sensors`

Check temperatures

`sensors`
