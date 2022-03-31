# Change Directory

`cd path/to/directory`

Revert to last Directory

`cd -`

# Disk Usage
DU shorthand shows disk usage for current dir

`du -sh *` or `du --summarize --human-readable *`

# Tar / GZ
## Extractions

`tar [Options] file.tar`

Options
* c | Create new archive
* v | Verbose
* f | Filename
* C | Specify destination

Extract a tar file

`tar -xvf file.tar`

Extract to specific destination

`tar -xvzf file.tar.gz -C /path/to/destination`

- - - -

# Create Bootable Drive with ISO
Find out partition name and unmount

`lsblk -f`

```
sdb
|-sdb1	/media/username/usb volume
l-sdb2
```
Dismount /dev/sdb1

*Make sure you choose the right drive, this will FORMAT it*

`sudo dd bs=4M if=path/to/input.iso of=/dev/sdb conv=fdatasync status=progress`

This may take a while..
