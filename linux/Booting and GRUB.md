# GRUB Defaults
The `/etc/default/grub` file has configs for booting defaults.

## GRUB_TIMEOUT
Length of time GRUB selection menu is displayed - good for if you have multiple GRUBs

## GRUB_DEFAULT
Default kernel that is booted by default. This is the index referenced in grub.cfg

You can set this to a specific kernel instead of the index like

`4.8.13-300.fc25.x86_64`

## GRUB_CMDLINE_LINUX_DEFAULT
Normally set to "quiet splash" but if set to an empty string will boot in verbose mode

*Make sure to run update grub to save*
`sudo update-grub`

# Basic Commands
Change to console during boot with ctl-alt-F7

- - - -

# Window Managers

If you want to revert back to default (Like Cinnamon for Mint), remove the package

`sudo apt remove plasma-desktop --autoremove`

And extra packages

`sudo apt remove kde* --autoremove`

`sudo apt remove plasma* --autoremove`

Reset splash screen

`sudo update-alternative --config default.plymouth`

Update initramfs and GRUB

`sudo update-initramfs -u`

`sudo update-grub`

If it uses a different Desktop Display Manager, like sddm for KDE, disable and stop the service

`sudo systemctl disable sddm`

`sudo systemctl stop sddm`

Make sure to reboot when finished

`sudo reboot now`
