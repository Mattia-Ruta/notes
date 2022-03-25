--Connecting to a database using a hostname and username
mysql -h hostName -u username -p
--You can connect to dbs on the same machine by running without host
mysql -u username -p
--Will ask to enter password. Make sure you know it for the sqldatabases

--cnf files are configeration files meant to set connection settings for mysql
--/etc/mysql
--/etc/mysql/mariadb.conf.d/50-server.cnf
--/etc/mysql/my.cnf
--Make sure to restart mariadb service anytime you change the cnf file!!!! sudo service mariadb restart
--If you're running a mysql server, check the 50-server file first and uncomment log_error = /var/log/mysql/error.log
--If you can't connect to server, try adjusting bind-address or commenting it out in the cnf files

--Can try adding these lines to 50-server if nothing is working
--local_infile=1
--sql_mode=
--skip-networking=0
--skip-bind-address

--To check the vars used for mysql, print the defaults:
--mysqld --print-defaults

--Import mysql backup ---------------------------------------------------------------

-------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------
--Once you see the mysql shell running, you can use SQL commands
--Checks current version and shows current date
select version(), current_date;
select version(); select now(); --You can run multiple queries at the same time, separated by;
select user(); --Shows current user
select database(); --Shows current db
select wronglineuhohpleasestop \c --Using \c stops the current multiple-line query, same as ^C
select @@global.storage_engine; --Shows default storage engine
--To show engine used for a specific table
select tableName, engine from information_schema.tables where table_schema='nation', table_name='countries';

--Creating and Using Databases
show databases; --Lists current databases
show tables; --Lists tables in current db
show full tables from dbName; --Lists tables and their types from db
show warnings; --Shows current warnings
show engines; --Shows available engines for dbs
show indexes from tableName; --shows assigned PK for a table

--Switch databases
use dbName;

--Creating a superuser for db administration
create user 'admin'@'localhost' identified by 'password123';
--Instead of localhost can use % to be accessed from anywhere
--But do not because security concerns

--Granting all permissions for all dbs
grant all privileges on *.* to 'superuse'@'%' with grant option;
--Granting permissions to create db for admins
grant all on newDBName.* to 'your_mysql_name'@'your_client_host';
--Make sure to refresh permisions for mysql
flush privileges;


create database dbName; --DB names are case sensitive
--Make sure to USE database if you want to access it

drop database dbName; --Deletes db, optional: drop database if exists dbName

--Create a table for sets of information ---------------------------------------------
--If creating or dropping a table, you can check if it exists
create table if exists tableName ();
create table or replace tableName (); --If it exists already, it will replace it

create table tableName (
  --Character Fields
  gender char(1), --Saves one char
  name varchar(64), --Basic char field, arg is char limit, maxlimit is 65535 chars

  binCode binary unique, --fixed-length binary code, unique means it can't appear twice
  binCode varbinary, --variable length binary code

  notes text, --small non-binary string
  notes mediumtext, --medium non-binary string
  answer longtext, --large field for large strings

  is_staff tinyint(1), --BOOLEAN, is either 0 or 1

  --Date and Time fields
  birthday date, --Datefield CCYY-MM-DD
  time time, --timefield hh:mm:ss
  datetime datetime, --CCYY-MM-DD hh:mm:ss
  date_time timestamp, --CCyy-mm-dd hh:mm:ss
  year year, --year value in CCYY or YY format

  --Integers
  num int auto_increment, --integers only
  num_lim int(5), --int's with a limit to 5 numbers
  num smallint,
  num bigint,
  num float,
  amount decimal(10, 2), --float with arg1 being digits and arg2 decimal places

  unique(field), --Makes sure the field is unique, like names or ID etc
  unique(field1, field2), --More than one field together is unique
  primary key(num), --sets a field as the PK

  -- Index Fields ------------------------------
  index SHORT_DESC_IND(name); --Short descending index using name column

  --Key Fields ----------------------------------
  PRIMARY KEY(num), --can set primary key to a column in a separate line
  primary key(num, name), --combo primary keys, having two fields as the primary key

  --key columns - you can also use multiple keys as a combo as a primary key
  emp_id int PRIMARY KEY auto_increment, --You don't need to specify NOT NULL for PK
  other_table_id --foreign key (key to different or same table in same db)

  --For foreign keys, CREATE FIELD FIRST, then adjust after using alter table
  foreign key(manager_id) references foreignTable(emp_id) ON DELETE SET NULL, --Sets a field as foreign id
--on delete, SET NULL or CASCADE, needed for foreign keys!!
--for foreign keys, inserting data it's better to set null then update after once you update the foreign table's entry
);

--Column attributes----------------------------------
create table tableName (
  name varchar(64) NOT NULL, --Field cannot be null
  person_id int PRIMARY KEY AUTO_INCREMENT, --Sets field as primary key, not null and unique by default
  surname varchar(64) UNIQUE, --has to be unique
  major varchar(64) DEFAULT 'English Major', --Setting a default value
  fullname varchar(101) --creates field based on other fields
    as (concat(surname, ', ', name)) virtual, --virtually generates field: 'Surname, Name'
)

--Describe information of fields in a table
describe tableName;

--Populating information in a table-------------------------------------------------
--If you want to load a .txt file into a table, create the file.txt and fill with lines:
field1  field2  \n  1997-12-09
--Use tabs for field separation and \n for null fields

--Once you have a txt file, load it into the table:
load data local infile '/path/pet.txt' into table tableName;
--If using windows, make sure to include how lines are terminated:
load data local infile '/path/pet.txt' into table tableName lines terminated by '\r\n';

--If raw inputting, use INSERT and VALUES-----------------
insert into tableName(field1, field2) values (
  'field1 value', 'field2 value'
)

--Make sure the columns are exactly the same as in the table you're inserting
insert into tableName values (
  'field1 value', default, 'f', '1993-03-30', NULL
);

--For Mariadb and MySQL you can insert a row by columns
insert into tableName
  set name = 'John',
  surname = 'Doe';

--Setting new values to a row, make sure you set a condition
update transactions
  set field1 = 'new value', field2 = 'new value 2'
  where id = 845935;

update tableName set birth = '1985-09-31' where name = 'Bowser';
--Finds table and sets the birth field to new value
--Finds the row where the name is Bowser to set the new data

--Renaming a column or adjust value of column
update tableName
  set field1 = 'new value'
  where field1 = 'old value';
update students
  set major = 'Biology'
  where major = 'Bio';

--replacing parts of values in multiple rows
update contacts
  set phone = replace(phone, '(408)', '(510)')
--will change all phonenumbers and replace any 408 codes with 510

--Deleting rows
delete from tableName where id = 554; --Deletes any row with the id of 554

--Deletes every row from a table, CAREFUL!!
delete from tableName; --Will delete every row in the table!! careful!!
truncate table table_name; --Deletes every row in a table more effeciantly

-- Indexing ----------------------------------------------------------------------
--Index basically creates an index like a book, telling you an important field to make searching faster
-- id or pk counts as an index because it's what's used to look up rows
-- Standard index for one column
create index index_name on tableName (column_name);

--Indexes can be unique, like a pk or id field
create unique index index_name on tableName (column_name);

--Can use multiple columns for an index
create index index_name on tableName (column1, column2);

--Dropping index
drop index index_name;

--Running queries ----------------------------------------------------------------
select dataToSelect from tableName where conditionsToSatisfy;

select * from tableName; --Grabs everything from a table
--Comparisons are same as others, =, <, <=, NOT EQUALS IS <> in SQL!!
select * from tableName where birth >= '1998-07-31'; --Finds any date after specified
select * from tableName where name = 'Name' and gender - 'f'; --Multiple conditions
select * from tableName where name = 'Name' or birth >= '1997-04-31'; --Or statement
select * from tableName if(500 < 1000, 'yes', 'no'); --If statement, if(condition, if true, if false)
--Checking if NULL
select * from tableName where death is not NULL; --Checking if a field is NULL

--Checking an int in between two values
select * from tableName where area between 100000 and 200000; --low first then high
select * from tableName where area not between 50 and 150; --Not between values

--Check if value of row is inside given list
select * from tableName where country in ('UK', 'IT', 'FR'); --can also say NOT IN

--Create column with the count of rows with that column, be sure to group results
select name, count(name) from people group by name;

select name, birth from tableName; --Shows specified fields from table
select distinct owner from pet; --Omits duplicated fields, like different entries have same info
select name, birth from pet order by birth desc; --Order results by a field, DESC is optional for descending order
select name, species, birth from pet order by species, birth desc; --Order by field then those by second field

--Will shorten rows to show one value per row, so duplicates don't show
select distinct year from yearsTable group by year; --Useful for seeing groups of rows

--Customising results and organising -------------------------------
order by name DESC; --orders the results by name field desc or asc
order by name, student_id; --orders by name first, same names will be ordered by student_id next

limit 5; --limits results to only 5 rows, make sure to order results
limit 1, 5; --skips arg1 rows and returns arg2 rows after skipping
limit 5 offset 1; --Same as above, skips 1 to return 5 results

select * from table \G; --Prettifies the results, good for lots of columns

--Grouping results and returning functions -------------------------
group by name; --groups rows by column given

--groups rows by surname and shows how many rows in that group
select surname, count(surname) from people group by surname;

--sums values of columns and returns the result in a new column which you can name
select role, sum(salary) 'total salary' from people group by role;
--sums the salary of people based on their role and returns the sum in the column called total_salary

--Returns min value in salary col based on role, grouping them together
select role, min(salary) min_salary from people group by role;
--Also works with max() and avg()
select role, avg(salary) from people group by role;

--You can limit grouped results by condition, like if there are more than 1 row with a role
select role, count(role) from people group by role having count(role) > 1;

--SubQueries -------------------------------------------------------
--You can nest a query in another one for specific results
select name, area from countries
  where country_id in (
    select country_id from countries where area > 50000
  );
--will create a result list from where/in statement of countries over 50000 area
--Then will query that result to return the results

--Good example is to find a row with the largest value
select * from countries
  where area = (
    select max(area) from countries
  );

--Dates ------------------------------------------------------------------------------
--Dates have a lot of functionality in sql, usually by YYYY-MM-DD
select name, birth, MONTH(birth) from pet; --Only checks the month aspect of birth
--Dates are broken down into: year(), month(), dayofmonth()

--To add time to a date and let it roll over into JAN if it's over 12
select * from table where MONTH(birth) = MONTH(date_add(curdate(), interval 1 MONTH));
--month() pulls just the month from the function within
date_add(); --Adds time to a given date by the interval given
--arg1 is the date in question, to give time to
--arg2 is the amount to give

--You can also use MOD() to retain numbers in a limit, like restricting to 12 for months
select name, birth from pet where MONTH(birth) = mod(MONTH(curdate()), 12) + 1;
--Since MOD() restricts from 0 to 11, you have to add 1 to to make it from 1 to 12
--MOD(floor, cieling) - lowest int to highest int

--Pattern Matching ---------
--Use like to find fields with letters you know
select * from table where name LIKE 'b%'; --name starts with b and % includes any char including no characters
where name like '%fy'; -- finds names that end in fy like fluffy, etc
where name like '%w%'; --finds any name that contains a w
where name like '_____'; --number of underscores means how many characters the name contains
--\ is the escape character, so if searching for a word that contains an underscore, you'd write the following:
where name like '\_%'; --if looking for any name beginning with an underscore

--ALTER TABLE functions------------------------------------------------------------------------------------------
lock tables table_name write; --lock tables so you can only access them
unlock tables; --Make sure to unlock them again!
describe tableName; --Shows fields and information about them
alter table table_name rename to new_table_name; --Rename table to something new

--Adding columns to tables -------------------------
alter table table_name
  add column newcol int, --add new column, newcol is name and define it
  add column newcol2 int after newcol, --adds second new column after named one
  add column newcol3 int first; --adds column to first of columns in table

--Adjusting keys -----------------------------------
alter table table_name
--if adjusting PK, make sure to drop existing one first
drop primary key,
add column student_id int not null primary key auto_increment;

--Adjusting Columns already in tables ---------------
alter table table_name

--modify changes TYPE of column, specify all types of new column
modify col_name int not null auto_increment; --See note below about NOT NULL

--change is like modify but you can rename the column, specify all types of new column
change col_name newColName int auto_increment;

--alter lets you change column options, like setting default
alter col_name set default 'new_default';

--If setting column to NOT NULL ---------------------
--Be sure to clear any null fields before forcing NOT NULL
--Sometimes like Mariadb will set NULL fields to '' if you change them
update transactions set col_name = 0 where col_name IS NULL; --Sets NULL values to 0 in column
--It may be an empty string so try '' if IS NULL doesn't work
change column col_name newColName int not null auto_increment;

--Deleting columns from tables ----------------------
drop column col_name; --deletes the column from the table

--Adding Foreign Keys to existing tables ---------------
alter table tableName
  add foreign key(fieldname) --Adds fieldname which is a foreign key
  references foreigntable(fieldname) --foreign table with the column from that table
  on delete set NULL; --What to do if it's deleted

alter table tableName
  add constraint fieldName --if adjusting an already made foreign key to add on delete
  foreign key (fieldName)
  references foreignTable (fieldName)
  on delete set NULL;

--Adding constraints after a table is created already
alter table tableName
  add constraint uniqueName
  unique(surname, name); --sets the combo of surname, name to be unique

--Deleting tables -----------------------------------------
alter table tableName rename to newTableName; --rename the table
drop table table_name; --Deletes a table from the db
truncate table_name; --Deletes all rows from a table effeciently

--Built-in Functions ----------------------------------------------------------------
sum(); --sums values together
count(); --counts rows with given column
min(); max(); --returns lowest or highest value from given column
curdate(); --Current Date
select last_insert_id(); --returns last id inserted into a table

timestampdiff(YEAR, birth, curdate()) --year part of datefield, field1, field2
select count(*) from pet; --Counts number of rows from entire table
select owner, count(*) from pet group by owner; --Counts number of pets that have same owner

--Using timestamp to create an int for number of years between birth and curdate
--as age creates a field called age to input fields into
select name, birth, curdate(), timestampdiff(year, birth, curdate()) as age from pet;

--Joining Tables -------------------------------------------------------------------------
--Joins two tables and creates a full table with both tables entries

--Inner Join ---------------
--Joins tables by a column that's populated with same IDs of each other, they can't be NULL
--columns with different names you have to assign same values
select * from parts inner join vendors on parts.vendor = vendors.vendor_id;

--To join more than 2 tables
select * from parts
  inner join vendors on parts.vendor_id = vendors.vendor_id
  inner join manufactors on parts.vendor_id = manufactors.man_id;

-- If fields are name the same, you can use 'using'
select * from views
  inner join area using(region) -- Same as area.region = views.region
  inner join carviews using (district)
group by area.region;

--if columns are named exactly the same you can use using:
select * from parts inner join vendors using (vendor_id);

--Left/Right Join ----------------
--Left table is main and tries to join right table to it
--if rows don't match in right table, it shows NULL instead
--Will show all rows from left table even if right table is NULL for them
select * from parts left join vendors on parts.name = vendors.part_name;
--Right join is exactly the same but uses right table instead

--Union -------------------------
--Joins 2 queries together by same columns, basically joining vertically
--Need the same columns and their types for it to work
(select employee_name as name, email from employees)
union all --all is default, can use distinct as well
(select customer_name as name, email from customers);

--intersect --------------------
--Joins 2 queries but only returns rows with exactly the same values
select name from guests
intersect
select name from vips
order by name;

--except -----------------------
--Joins 2 queries but subtracts a table's entries from results
select name from guests
except
select name from vips;
--will return guests who aren't on the vips table

--Inserting query results into another table-----
--results from area < 50000 from countries table
--gets inserted into the small_countries table
insert into small_countries (name, area)
  select name, area from countries
  where area < 50000;

--Table Views ------------------------------------------------------------
--You can save queries as views to make it easier to remember custom queries
create view country_details as
  select * from countries order by country;

--To recall a view, access it like a table
select * from country_details;
--To delete a view, drop it
drop view country_detials;
