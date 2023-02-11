# Backup entire Server

`mariabackup --backup --target-dir=/path/to/backup/ --user=mariadbuser --password=pass`

Make sure the directory is empty or doesn't exist

# Restore from Backup

## Preparing the Backup for Restoration
`mariabackup --prepare --target-dir=/path/to/backup/`

Now that it's prepared, you can either `copy` it back or `move` it back

Move - Deletes backup

`mariabackup --move-back --target-dir=/path/to/backup/`

Copy - Keeps backup

`mariabackup --copy-back --target-dir=/path/to/backup/`

You may need to adjust permissions of the backup after it's created

`sudo chown -R mysql:mysql /var/lib/mysql/`