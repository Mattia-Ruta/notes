#PHP and MYSQL

## Connection

### Opening Connection
Create a new mysqli object using credentials

```php
$host = 'localhost';
$user = 'username';
$password = 'password123';
$database = 'db';

$mysqli = new mysqli($host, $user, $password, $database);
```

Check if the connection succeeded and kill if not

```php
if ($mysqli->connect_error) {
    die('Could not connect to database' . "\r\n");
}
```

### Closing Connection
Close connection to database

`$mysqli->close();`

- - - -

## Running Queries

```php
$sql = "
  select *
  from tablename
  where condition
"
$result = $mysqli->query($sql);
```
Result saves in a variable which can be retrieved
Row is row number while value is the array which holds the field and value of the field

```php
foreach ($result->fetch_all(MYSQLI_ASSOC) as $row => $value) {
  echo $value['field'];
}
```
