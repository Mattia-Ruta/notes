
# File Permissions
* r | Read
* w | Write
* x | Execute (Also applies to open dir)

## Flags
* d | Directory
* s | Set UID - User gets permissions of user or group of file when executing
* t | Sticky Bit - Sets so only file owner can rename or delete file
* l | Link - Symbolic Link

# CHMod
Permissions numbers
* 0 - Nothing
* 1 - Execute
* 2 - Write
* 4 - Read

# facl
Commands to add extra permissions for files and directories

Usage:

`getfactl [Options] file.sh`

`sudo setfacl [Options] u:<user>:<permissions> file.sh`

Options
* -m | Modify permissions
* -x | Remove permissions

Add extra user to file permissions and let them read and write to file

`sudo setfacl -m u:user:rw file.sh`

# Sticky Bit
The purpose of sticky bit is to secure a directory multiple users/groups have access to. 
It lets only the owner of the file/directory delete or rename it.
