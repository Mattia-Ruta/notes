#Notes about networking in bash

#Returns ports currently open on given argument
nmap localhost

#If you're inside a dir you can search for any lines that contain part of a word
cd /etc/mysql
grep -snri '127.' .
