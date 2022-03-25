# Built-in Functions

## Printing

### print_r
Print info about objects or arrays

`print_r($object, return=false)`

Set return to true to return a string representation of an array or object

`print_r($object, true);`

- - - -

# Maths Functions
Random - Returns a random number in between two values (inclusive)
```php
rand();  // Random num between 0 and getrandmax()
rand(5, 10);  // Random num between 5 and 10

# sFTP Connections
Connect to sFTP server and retrieve files using PHP's SFTP class

```php
// Using phpseclib's PHP class
use phpseclib\PHP;

// Credentials
$server = "123.123.123.123"
$username = "username";
$password = "password";
$port = 2020;

$sftp = new SFTP(
    $server,
    $port, // Omit to default to 22
);

// Check if login succeeds
if (!$sftp->login($username, $password)) {
    // Log error here or die
}

// Change directory in server
$sftp->chdir("dir_to_change_to");

// GET files
$sftp->get(
    $remote_file,
    $local_file, // Rename local file here
)

```
