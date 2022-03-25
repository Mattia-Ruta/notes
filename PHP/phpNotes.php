<?php  //Use this tag to write php code within HTML
/*?> to end */
//If you have an entire document only with PHP, don't include the ending tags


/*Installing PHP*/
//Going on website, you can download the latest build on www.php.net
//After you install the folder, make sure to update PATH
//Open System Environment Variables and edit PATH to include PHP root folder
//If you open the terminal, you can see if php was installed using php -v

/*Starting Development Server*/
//cd into the folder that contains the php root directory you want to use for the web server
//Inside terminal, you can start a local server using the following line:
//php -S localhost:8000
//Once you start the webserver, you can go to the site localhost:8000 in your web browser
//That will be the root directory so open the file you want to use in the browser with localhost:8000/file.php
//If you want to open a php file using your browser, fill in the path in the url field:
//localhost:8000/file.php
//-------------------------------------------------------------------------------

/*Basic Commands*/
echo "Hard Coded Text";
echo("Hard Coded Text");
//Input any string to be printed to the page within <body></body>

//Shorthand for one line HTML code
<?="<p>Quick HTML</p>";?>

//Shorthand to include value in HTML
<p>Result: <?=$var;?></p>

//You can add vars together in the same line
<p><?=$var1 . " and " $var2;?>

//You can use HTML within echo
echo "<h1>TITLE</h1>";

//Formmated strings
echo "<h1>Number is ${numberVar}</h1>";

//Functions inside echo
echo "Result is:" . funcToDo($var);

//Date() is a built in function
echo Date('h:i:s:u, F I');
//Prints 02:53:00:000000, October 1
/*
Date Formatting:
h: 12hr format
H: 25hr format
i: Minutes
s: Seconds
u: MicroSeconds
a: Lowercase am or pm
I: Full text for the Day
F: Full text for the Month
j: Day of the Month
S: Suffix
Y: Year in 4 digits
*/

//User input saved into a var
$name = readline(">> ");
//Will print >> to terminal and wait user input

//Checks if a file or directory exists
file_exists($fileName); //Returns true or false

//Requiring other php pages
require 'model.inc.php';
require_once('file.php'); //Requires a file in the same directory

//-------------------------------------------------------------------------------

/*Autoloading function before an object gets called*/
spl_autoload_register(function($class) {
	//Gets called before an object is created
	//$class gets passed in, which is the name of the class
	//new Person(); will pass in Person as $class

	//for Person.php:
	require_once($class . '.php'); //Adds basic .php extension to class name
})
//To be cleaner, can create function after loading with string
spl_autoload_register('FunctionName');
function FunctionName($className) {
	//Path has name of folder containing the Person.class.php file
	$path = "classes/";
	//Ending after classname in file
	$extension = ".class.php";
	//Joins everything together, $fullPath is className.class.php
	$fullPath = $path . $className . $extension;
	//Includes the fullpath everytime an object is created
	include_once($fullPath);
}
//If you create a header file for autoloading, be sure to include it:
include 'headers/autoloader.php';
//headers is the name of the folder it's in

//You can put var implimentation in the included file and set values in current page
include 'variableTemplate.php';
$varinOtherPage = 5;

//Including other pages like classes
include 'folder/class.php';

//Shows all info on a var
var_dump($var);

//String to lower case
strtolower($var);

//String to upper case
strtoupper($var);

//String Length
strlen($var);

//String Indexing
$var[0];

//String Replace
str_replace("ReplaceThis", "With This", $varToModify);
//First

//Info on PHP
phpinfo();

//Adding Strings
echo "string" . " other string " . " last string."

//Enabling strict mode so type hinting is type declaration
declare(strict_types = 1); //To disable, set to 0

//Absolute value
abs($numVar);

//arg1 to the arg2 power
pow(2, 4);

//Square root
sqrt(144);

//Returns higher number or lower number
max($numLow, $numHigh);
min($numLow, $numHigh);

//Rounding Numbers to standard rules
round(3.2);

//Always rounds up
ceil(3.3);

//Always rounds down
floor(3.3);

//You can catch the errors in a var:
try {
	//Trying something that will throw an error
	$person1->SetName(1); //Trying to set a forced string as an int
}
catch (TypeError $e) {
	//Will print string plus the error message
	echo "Error!!!: " . $e->getMessage();
}

//-------------------------------------------------------------------------------

/*Variables*/
//$ indicates you want to make a variable
$name = "John";
$age = 5;
//You can reference the var again by using the $ symbol

$originalVar = 1;
//Assigning new var to an existing value creates a copy
$copyVar = $originalVar;

//Referencing original var so changing one will change the other
$newName =& $originalVar;

//Prints an entire page of info of current php version
phpinfo();

//Const variables that cannot change
CONST PI = 3.14;
//Keep all caps so it's obvious that it cannot change!

//Define a constant
define('PI', 3.14159);//Returns false if failed

//Var types:
"String"; //String
50; //Integers
30.0; //Floats/Double
false; //Bools
NULL; //Nulltype

//Strings
$stringy = "Normal String";
$longString = <<<EOT
This is a very long string. $var1 can be used too!
You can also print {$var3->array[1]}.
You can also use special chars like this: \x41
EOT;//Must be the first char in line, no indentation
//\x41 will print the letter A
$otherLongString = <<<EOD
You can also use EOD!
EOD;

//-------------------------------------------------------------------------------

/*Functions*/
//Empty function with no value to return
function SaySomething() {
	echo "Say Something";
}

//Can return a value from a function
function ReturnFunction() {
	return 5;
}

//Passing a var as an argument only creates a copy
function Change($varf) {
	$varf = "New Value";
	//This only creates a copy and is a local scope
	//Original var doesn't change the value
}

//Passing a var as reference changes the original value
function Change(&$varf) {
	$varf = "New Value";
}

//Saving Function value in a var
$returnVar = ReturnFunction();

//Arguments for Functions
function PrintName($name = "Default Name") {
	echo "Hello, $name";
}

//-------------------------------------------------------------------------------

/*Arrays*/
$myArray = array(0, "string", 5.2);
$shortArray = [0, 1, 2];
$nestedArray = ["first", "second", ["third", "fourth"]];
$nestedArray[3][0] //returns "third"

//Length of array elements
echo count($myArray);

//Print an array with elements and index
print_r($myArray);

//Converts array into a string
implode(", ", $arrayToUse);
//First argument goes in between elements
//Second argument is the array to print

//Add element to array
$myArray[] = "New Element";

//Removes first element
array_shift($myArray);
//All elements in the array get shifted back 1 index
//$myArray[1] becomes $myArray[0]

//Removes last element and returns the element itself
$singleElement = array_pop($myArray);

//Adds elements to beginning of array and returns Count() of array
$countArray = array_unshift($myArray, "New Index0");

//Adds elements to end of array and returns Count() of array
$countArray = array_push($newArray, "Added1", "Added2");
//First argument is array in question
//Any additional argument adds that element to array

/*Associative Arrays/Dictionary*/
$myArray = ["key" => "value", "key2" => "value2"];

//Printing an AA
print_r($myArray);

//Deleting a key and value pair
unset($myArray["Key"]);

//-------------------------------------------------------------------------------

/*Superglobals*/
//Global variables that are available at all scopes
$GLOBALS;

$_SERVER;

//Array of vars using query params in URL
$_GET;

//Array of vars passed using a form or POSTing data
$_POST;
$studentName = $_POST["studentName"];
//Access data put within forms in HTML by using their tag name

$_FILES;

$_COOKIE;

$_SESSION;

//Contains get, post, and cookie vars
$_REQUEST;

$_ENV;

//-------------------------------------------------------------------------------

/*Forms and POSTing data */
//Forms are done through HTML tags
//To use data POSTed, you need a name attribute
<input type="text" name="varName">
//This inputs "varName" into the $_POST array
//It's also within $_REQUEST

//Be sure to specify your form is using POST
<form method="POST"></form>

//You can move the user to a new page when they submit the form:
<form action="thankyouPage.php">
//This only works if the file is in the same directory!
//Action works in both GET and POST methods!
//If you put same file, it will return to same page with complete form

//Make sure you create a submit button for the form
<input type="submit">

//Once you close off the form, use PHP to access data submitted!

//Within PHP:
//If method was GET and textinput was named searchRequest
$_GET["searchRequest"];

//If method was POST and input was username
$_POST["username"];

//-------------------------------------------------------------------------------

/*Conditionals and statements*/
if (true) {
  //Do Something
}
else {
  //Else Statement
}

//Standard >= and <= conditionals work in PHP
if (5 > 1) {
  return "5 is greater than 1";
}
elseif ($var1 === 5) {
  return "This var is equal to 5!!";
}
elseif ($var1 !== 5) {
  return "This var is not equal to 5!!";
}
elseif ($var1 == 5) {
  return "This is also true";
}
else if (true) {
  //else if also works, but elseif is more universal
}
else if ($var1 === 2 && $var2 === 2) {}
else if ($var1 === 2 || $var1 === 2) {}
//Using == is equal but not as strict
//Using == is identical and best practice

//Switch statements
switch ($varChar) {
  case "A":
    echo "Great!";
    break;
  case "B":
    echo "Good";
    break;
  case "C":
    echo "Fair";
    break;
  case "F":
    echo "See me!";
    break;
  default:
    echo "Not Valid Grade";
}

//break breaks the statement but you can omit:
switch ($dayOfWeek) {
  case "Mon":
  case "Tue":
  case "Wed":
    echo "Beginning";
    break;
  case "Thu":
  case "Fri":
  case "Sat":
  case "Sun":
    echo "End";
    break;
  default:
    echo "Not Valid";
}

//Ternary operator
$isClicked = false;
$linkColour = $isClicked? "purple" : "blue";
//$var? questions if that var is true or false
//true : false
$numVar < 12? "true statement" : "false statement";
function ReturnBool($boolVar) {
  return $boolVar? true : false;
}

//-------------------------------------------------------------------------------

/*Loops*/
//For Loop
//Init a counter, check condition, happens after every iteration
for ($i = 1; $i <= 5; $i++) {
	//Will iterate and loop until $i is 5
}
//Loop through an array to print each index
$nums = array(1, 2, 3, 4, 5);
for ($i = 0; $i < count($nums); $i++) {
	echo $num[$i]; //Prints value at index each iteration, i = 0, then i = 1, etc
}

//Foreach Loop
//Loop through an associative array
foreach ($array as $key => $value) {
//key and value are temp vars for the loop to iterate
//you can name them what you want but remember they're key => value
	//Prints every value inside array
	echo $array[$key];
}

//Foreach Loop with reference
//Changes original array in question
foreach ($array as &$key => &$value) {
}
//Make sure you unset $key reference var
unset($key);

//While Loop
$num = 1;
//Will loop over the code until condition is met
while ($num <= 5) {
	echo "$index is less than 5, I'll add 1 now <br>";
	$index++;
}

//DoWhile Loop
//Do will excecute once then checks while condition, if true will loop again then checks again, etc
$index = 6;

//Excecutes once then checks condition at end to see if will loop again
do {
	echo "$index <br>"; //Will print 6 before adding
	$index++;
}
while ($index <= 5); //Since index is 7 now, it won't loop the do statement again

//-------------------------------------------------------------------------------

/*Classes*/
class NewClass {
	public $info = "Some Info";
	private $name;

	//Lets you inheret the var and adjust with that new class
	protected $takeOverVar = "Meant to be inhereted and adjusted";

	public function GetName() {
		return $this->name; //You don't put $ for properties
	}
}

//You can inheret classes
class InheretedClass extends NewClass {
	public function ChangeName($newName) {
		$this->takeOverVar = $newName; //Inhereted variable
	}
	//To override function just re-write the function with new code
	public function GetName() {
		//New Function Code
	}

	//Methods that can return bool based on an object's properties
	function HasHonours() {
		if ($this->gpa >= 3.5) { //checks specific object when you do $object->HasHonours();
			return true;
		}
		else {
			return false;
		}
	}
}

class Person {
	public $name;
	public $age;
	var $height; //Can use generic var tag, which is naturally public but not used
	public static $drinkingAge = 18;

	//To create constructors you need to use __construct (2 underscores)
	public function __construct($name, $age) {
		$this->name = $name; //$this refers to current object in question being created
		$this->age = $age; //Open way of setting a property
		$this->SetAge($age); //Using Set Function to filter invalid properties

		echo "$name was Created!";//Can run regular lines everytime object of class is created
	}
	public function __destruct() {
		//Code is run after the constructer
	}
	//Set function in a class
	public function SetAge($age) {
		if ($age > 0) {
			$this->age = $age;
		} else {$this->age = null}
	}
	public static function SetDrinkingAge($newAge) {
		self::$drinkingAge = $newAge; //To access static property inside class
	}
}
//Within class script, use an object to instatiate properies and methods
$object = new NewClass;
echo $object->info; //Access method or property within an object
unset($object); //Destroys the object
Person::$drinkingAge; //To access a static property
Person::SetDrinkingAge(21); //To use a static method

//Creating a namespace
namespace People;
//This means that if you reference a class inside, you have to include namespace
$person1 = new People\Person("John", 50);

//-------------------------------------------------------------------------------

/*URL Parameters*/
//If you use GET method, you can input data into URL or grab from GET method forms
//site.php?var=value&var2=value
//Useful for bookmarking or searching so user can come back to specific page

/*Checkboxes from HTML*/
<form action="site.php" method="POST">
	//Creates array called fruits for checkboxes
	//value is value if this checkbox is ticked for var in name
	Apples: <input type="checkbox" name="fruits[]" value="apples"><br>
	Pears: <input type="checkbox" name="fruits[]" value="pears"><br>
	<input type="submit">
</form>

//To gather the values collected within fruits[], must reference in POST
$fruits = $_POST["fruits"]; //Must leave out [] for arrays

//-------------------------------------------------------------------------------

/*DATABASES*/
//Database Information needed to connect
$dbServername = 'localhost';
$dbUsername = 'root';
$dbPassword = '';
$dbName = 'dbName';

//Start connection using credentials stated
$conn = mysqli_conect($dbServername, $dbUsername, $dbPassword, $dbName);
if ($conn->connect_error) { //Checks if an error occured when connecting to db
	die("Connection Failed" . $conn->connect_error); //Kills connection and displays db error
}


//Within HTML to show db information
include_once 'includes/dbh.inc.php';
//Be sure to include the connection information to the HTML page

//Prepare query for db
$sql = "SELECT * FROM dbTable;";

//Saves query result inside $result
$result = mysqli_query($conn, $sql); //Uses connection and sql query to pull data from db
if (mysqli_num_rows($result) > 0) { //Runs if there was any information pulled from db
	while ($row = mysqli_fetch_assoc($result)) { //$row becomes an array with the query
		echo $row['column'];
	}
}


/*Built-in mysql functions for queries*/
mysqli_num_rows($result); //Checks how many rows were retrieved from the db
mysqli_fetch_assoc($result); //Creates an array from db query, column => value. ex: (id => 6, date => '2016-08-09') etc



/**
* vcars website
*
*Copyright (C) Used Car Sites Limited
* @package vcars
*/
require '../../includes/core.php';
$view->makeId = get_make_id($url);
$makemodel = get_make_model();

//get latest reviews
$sql = "SELECT
				*
				FROM
				user_reviews
				WHERE
				makeid=:makeid
				AND
				approved = 1
				SORT BY
					id DESC
					LIMIT " . count($view->models);
$result = $db->executeQuery(sql, array(':makeid' => $view->makeId));
$view->latestReviews = [];
while (($row = $result->fetch()) !== false) {
	$view->latestReviews[] = $row;
}









?> //End php code with this end tag
