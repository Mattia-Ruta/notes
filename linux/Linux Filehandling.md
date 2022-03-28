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
