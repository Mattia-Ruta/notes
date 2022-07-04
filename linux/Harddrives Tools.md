# Printing info on HDD's
Show partitions visually mapped to their HDDS with filesystem info

`lsblk -f`

View extended info like disk model and disk identifier (for /etc/fstab)

`sudo fdisk -l`

# Formatting Harddrives

## FDisk - Create Partitions
Most common way, use /dev path for disk

*Make sure you use the right drive!!!*

`sudo fdisk /dev/sda`

This will open up fdisk which listens for commands

p | Print - Prints disk info

This will show you any partitions currently on the drive

o | DOS - Creates standard DOS partition table

Once you create the partition table, you can create the partition

n | New - Creates new partition

Once you finish, you can write your changes to the disk

w | Write - Saves changes and writes to disk

## Make Filesystem - Format Partition to Filesystem

Once you have a partition, you can format it with a Linux filesystem

`sudo mkfs.ext4 /dev/sdc1`

*Make sure you create the filesystem on the partition, not the drive (/dev/sda1 not /dev/sda)*

## Labelling a Disk
You can give a label to a partition using e2label

`sudo e2label /dev/sdb1 label`

Or give empty string to clear label ("")

- - - - 

# Mounting and Unmounting HDDs

## Mount
`sudo mount /dev/sda /dir/to/mount/to`

## Unmount
`sudo umount /dir/to/umount/from`

## Perma-Mount
This will keep the HDD mounted even after reboot

Grab the UUID of the HDD from either

`lsblk -f`

`blkid /dev/VG_Name/LV_Name`

Edit the /etc/fstab file 

`sudo nano /etc/fstab`

Add the line

```bash
UUID="234234234-sdfsdf-32324-f23f3-23f23f2" /dir/to/mnt/ ext4 defaults,nofail 0 2
```

*VERY IMPORTANT: Test it mounts correctly before restarting*

`sudo mount -a`

- - - -

# PV's, VG's, and LV's
Only use these if you want to pool more than one HDD into a filesystem

You have to partition the harddrives involved to the 'Linux LVM' type of partition

# Physical Volumes (PV)
The physical harddrive/partition to be pooled

List PV's

`sudo pvs` - Compact view

`sudo pvdisplay` - View with more info

Create a PV from a partition

`sudo pvcreate /dev/sdc1`

*Make sure you create the PV on the partition, not the drive (/dev/sda1 not /dev/sda)*

Once you create the PV it will show with `pvdisplay`

# Volume Groups (VG)
Once you have a PV, you need a VG to add it to. This is the pool the PVs combine into

List VG's

`sudo vgs` - Compact view

`sudo vgdisplay` - View with more info

Create VG with a PV

`sudo vgcreate VG_Name /dev/sdb1`

Add PV to Existing VG

`sudo vgextend VG_Name /dev/sdb1`

This will add the sdb1 PV to the VG_Name VG

# Logical Volumes (LV)
Once you have a group, you can create a logical volume inside that group

List LV's

`sudo lvs` - Compact view

`sudo lvdisplay` - View with more info

Create LV

`sudo lvcreate -L 10G -n LV_Name VG_Name` - Set name and size


[Options]

* -n | Name - Use provided name
* -L | Size - Give specific size like 10G
* -l | Size - Relative, like 100%FREE


Expand existing LV to max size (using full LV path):
`sudo lvextend -l 100%FREE /dev/VG_Name/LV_Name`

Now you can create a filesystem for the LV

`sudo mkfs.ext4 /dev/VG_Name/LV_Name`

And mount to an existing directory

`sudo mount /dev/VG_Name/LV_Name /dir/to/mount/to`

Extra LV Commands:

Delete LV

`sudo lvremove /dev/VG_Name/LV_Name`

Rename LV

`sudo lvrename /dev/VG_Name/LV_Name LV_New_Name`

- - - -

# RAID's

RAID's are managed using the `mdadm` package

## Check Arrays

General details for array

`sudo mdadm --detail /dev/md0`

Sync status for array

`cat /proc/mdstat`

- - - -
## RAID0

Stripes data across two drives. Faster than one but doubles the risk of data loss

## RAID1

Mirrors data between two drives. Safe and protects data loss but halves useable storage

Create RAID1 using two devices, naming it md0

`sudo mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sda1 /dev/sdb1`

If no errors arise, you can make a filesystem on the array

`sudo mkfs.ext4 /dev/md0`

Save RAID to conf

`sudo mdadm --detail --scan >> /etc/mdadm/mdadm.conf`

If permission denied, set to chmod 777 then back to 644

Update RAM FS

`sudo update-initramfs -u`

## RAID10

*Minimum 4 drives needed*

Stripes data across two systems which are made up of two drives in a RAID1 array. Combines RAID0 and RAID1
