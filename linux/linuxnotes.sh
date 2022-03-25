#grep - Searching tool
cd /path/to/dir
grep "search" .

#-i | Ignore Casing like upper or lower case
grep -i "name" .

#-s | Suppress messages of no files found
#-n | Show LineNumber for result, good for searching code files
#-r | Recursive - Searches files within folders as well
#-w | Will return the full word instead of searching within others
cat file.csv | grep -w "1233" | wc #WIll feed into WordCount and return how many entries found

#Networking
#Print available IPs and mapping for local machine
cat /etc/hosts
#You can edit this file to map local addresses to an IP
127.20.0.1 https://websitelink #Comment for where it goes

#netstat - Network Statistics tool to see what IPs and port you have open on machine
sudo netstat -tulpn

#Searching for something specific
sudo netstat -tulpn | grep -e "Local Address" -e "maria"

#Symbolic links are like shortcuts that link a copy to an original file
ln -s /full/path/to/original /full/path/to/link
