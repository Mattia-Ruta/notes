# Namespacing
Using a namespace keeps things organised.
Use the same namespace for the same project/package.

```c#
namespace Program {
    // Main function here
}

// In a different dir called Cars,
// you can create a namespace for classes having to do with cars
namespace Program.Cars {
    // Classes and Functions of Cars namespace
}

// Or create a new namespace
namespace NewSpace {
    // Classes and Functions of NewSpace
}

// Using namespaces
using Program.Cars;
using NewSpace;
```

# Acess Modifiers
Defined accessibility of classes, properties, and methods

```C#
// Can be accessed outside the class
public string test;

// Can only be accessed inside the class
private int test2;

// Private but can be used by child classes
protected int test3;
```

- - - -

# Managing Classes in Files
Any collection of classes you make should be in a namespaced directory

Project > Project.NameSpace > Class {}