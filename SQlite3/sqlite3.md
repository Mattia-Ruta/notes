# Installation
Most distros have the package

`sudo apt install sqlite3`

# Basic Setup
Start the server with:

`sqlite3`

This opens the shell `sqlite>` where commands are done with the "." notation.

## Create Database
Run `.open database.sqlite` to create the DB file where you are.

## Settings
Show header for queries

`.header on`

Change field separator to "," instead of "|"

`.mode csv`

You can set an output to a file

`.output filename.txt`

# Built-in Functions
Show databases

`.databases`

Show tables in database

`.tables`
