# Create Standard Class
Usually in an `includes/classname.inc.php` file
```php
class Name {
    // Property
    public $prop;
    protected $prop2;
    private $prop3;

    // Static Property
    public static $prop4;

    // Constructor
    function __construct($param) {
        $this->$prop = $param;
    }

    // Method
    function get_prop(): int {
        return $this->prop;
    }
}
```
# Extending a Class
Inherit a base class

```php
class NewClass extends Name {
    // Override $prop var
    public $prop = 'New Value';

    // Class Constructor
    public function __construct($param) {
        $this->prop = $param;

        // Call Parent Class construction
        parent::__construct($param);
    }
}
```

## Overriding Properties and Methods
Redefining properties and methods in the new class will override them. 


- - - -

# Class Visibility
`Private` makes properties and methods *only accessible from the class itself* so it cannot be called from outside the class itself. You can copy a private var and return/echo that from a method.
If you inherite the class, a private property *CANNOT* be accessed. You would need to make it protected.

`Protected` lets a property or method be accessed by classes that inherit the original class that contains it

`Public` lets you access it outside the class

- - - -

# Calling a Class
Static methods and properties

```php
// Create object
$obj = new Class();

// Access public property
$obj->prop;

// Access public method
$obj->method();

// STATIC
Class::$property;
Class::static_method();
```