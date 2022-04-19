# Backing up Files
*Make sure you're in a dir you can write to*

General Use

`mysqldump [Options] <db> [table1 table2] > backup.sql`

Options
* --add-drop-database | Add line DROP DATABASE
* --add-drop-table | Add line DROP TABLE
* --all-databases | Will dump all tables in all databases
* --no-data | Will not dump rows of data, just SCHEMA
* --replace | Write REPLACE instead of INSERT
* --verbose | Verbose mode

Create an SQL backup file in command line:

`mysqldump -u user -p <database> <table1> <table2> > backup.sql`

If socket is missing, you can specify it with `--socket=/var/run/mysqld/mysqld.sock`

# Restoring from Backup

## Within Mariadb
*Make sure the database is created for the backup*

Use command `source` to load into db

`source /home/mattia/Downloads/backup.sql`

## Terminal Command
Using command line:

`mysql -u user -p <database> < backup.sql`

- - - -

# Exporting Files
## Outfile
```sql
select id, field_name
into outfile '/tmp/filename.csv'
fields
terminated by ',' -- Field Separation
enclosed by '"' -- Surround Fields
lines terminated by '\n' -- After every row
from tablename
where <condition> -- Option conditions
order by id desc;
```

# Importing Files
## Infile (From Outfile)
```sql
load data infile '/tmp/filename.csv'
into table tablename
fields
terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 rows; -- To ignore first line
```

If dates are empty strings in the infile, make sure you import them as `NULL`

## Using variables while importing
Setting fields as variables lets you ignore them or adjust them after

```sql
load data infile '/tmp/filename.csv'
into table tablename
fields 
terminated by ','
(field1, @field2, @field3)
set field3 = 'specific value';
```

`@field2` will be ignored while `@field3` will be set to the specific value.
