# Linux Tools for Manipulating Data

## GREP
Search for keywords

General Use
`grep [options] "keyword" /dir/`

Piped from file
`cat file.csv | grep "keyword"`

Options
* -i | Ignore Casing like upper or lower case
* -s | Suppress messages of no files found
* -n | Show Line Number for result, good for searching code files
* -r | Recursive - Searches files within folders as well
* -w | Will return the full word instead of searching within others
* -v | Inverts search, excludes keyword and prints everything without it

* ^ | In front of keyword will search beginning of each line for keyword
* | At end of keyword will search ends of each line for keyword

Use:
`grep "^keyword" file.csv`
Returns:
`keyword: rest of line`

Keyword Filters:
. | Any character can fit here, ex "..ch" finds "tech"

## Advanced searching
Use `-rni` flags to search all files recursively for a pattern in a directory

`grep -rni "pattern" .`

## TR
Translate translates or deletes characters from an output

General Use
`cat file.csv | tr [Options] [SET1] [SET2]`

-d | Delete, removes character specified and makes SET2 optional
-s | Squeeze, removes all duplicated characters in SET1

Remove quotation marks from results
`cat file.csv | tr -d '""' file.csv`

Make output to upper
`cat file.csv | tr [:lower:] [:upper:]`
`cat file.csv | tr [a-z] [A-Z]`

## Word Count
General Use
`wc [options] file.csv`

Pipe commands into wc to read
`grep "keyword" file.csv | wc`

Returns 'newline, word, bytecount, filename'
`849 298030 4655340 file.csv`

Options
-l | Prints just the number of lines
-w | Prints just the number of words
-c | Prints just the number of bytes
-m | Prints just the number of characters

Pipe directory into wc to count number of files
`ls | wc -l`

## Cut
Cut parts of lines from files and print results

General Use
`cut [option] file.csv`

-f | Fields, specify which field to cut, can be list
-d | Delimiter, default is TAB, but can specify (like comma etc)
-c | Characters, specify which character to cut, can be list
--compliment | Will print everything except fields you specify

Use of Fields
Print 1st and 3rd field in every line using default TAB delimiter
`cut -f 1,3 file.csv`

Print up to 4th field, still using TAB
`cut -f -4 file.csv`

Use of Delimiters
Delimiters are the character used to seperate fields in a line, default is TAB but can be ';' or ',' or ' ' etc

Change to commas for delimiters and print just the first field
`cut -f 1 -d ',' file.csv`

## Sort
Sorts a file and arranges it in a certain order, default is alphabetical and case sensitive

General Use
`sort [options] file.csv`

Options
-n | Numerically, will sort by numerical values
-r | Reverse, will reverse order and do ASC instead
-u | Unique, will remove duplicates
-k | Column, specify which column to sort by
-M | Month, will sort by month in year as opposed to alphabetically

Sort and remove all duplicates
`sort -u file.csv`

Sort by second Column in file
`sort -k 2 file.csv`

## Uniq
Unique filters out repeated lines in a file that are next to each other
*Be sure to use sort and pipe into uniq*

General Use
`sort | uniq [options] file.csv`

Options
-c | Count, tells how many times a line was repeated
-d | Prints the repeated lines and not lines that are unique
-u | Prints the unique lines and not repeated lines
-i | Ignore Case, makes the search case insensitive
-w | Only compares N characters in a line

## Head and Tail
Head shows beginning of text files.
Tail shows end of text files.

Defaults to 10 lines

General Use
`head file.csv`
`tail file.csv`

Options
-n | Number of lines to print, shorthand is just -10

Print first 50 lines in a file
`head -n 50 file.csv`
`head -50 file.csv`

Print last 50 lines in a file
`tail -50 file.csv`

Print lines in a file from a specific line
`tail -n +2 file.csv`
`tail +2 file.csv`

Follow file as it prints to find the last 10 lines
*This opens a flow of data from the file and updates as the file updates*
`tail -f file.log`
Useful for following logs

## AWK
Aho, Weinberger, and Kernighan made this to print specific things from lines in a file
Print every line of a file and specify things to customise
Default delimiter is whitespace

General Use
`awk -F, '{print $0}' file.csv`

Options
-F | Field Separator/Delimiter character

Fields in a file are saved as variables
`$0` is the entire line, `$1` is the first field, etc until `$NF` which is last field
`awk '{print $1, $4}'`
Prints field 1 and 4 in every line

BEGIN and END
Run before and after the main logic
`awk 'BEGIN {print "First\nSecond"} {print $0} END {print "Done"}' file.csv`

Conditionals
You can check if a field is compared to a number to print it
`awk -F, '$3 >= 1000 {print $1}' file.csv`

Searching
You can search an expression to print a line
`awk '/1200/ {print $0}' file.csv`
Will print entire line if it finds a pattern of 1200 in the line
You can use `/^1200/` to check if it starts with that pattern in the line instead of checking the whole line

## OD
Octal Dump writes file into a stream into stdout

General Use

`od [Options] file.csv`

Options
-t | Type, set the format of the output

Read a file and look for printable characters like backspace and return carriage

`od -t c file.csv`

## diff
Shows difference between two files

General Use

`diff [Options] file1.csv file2.csv`

Options

* -u | Unified - Shows + or - for any OS
* --color | Colour - Colours red and green

Find difference between two files that becomes colour-coded

`diff --color -u file.csv file2.csv`
