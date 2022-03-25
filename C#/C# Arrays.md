# Initialisation:

```C#
// Declare array of 3 ints
int[] array = new int[3];

// Declare array with values
int[] array = new int[] {1, 2, 3};

// Declare array shortcut with values
int[] array = {1, 2, 3};
```

# Built-in Array Functions
```C#
int[] array = new int[] {1, 2, 3};

// Length/Count
Console.WriteLine(array.Length)
// => 3

// Sum
Console.WriteLine(array.Sum());
// => 6
```

## Array Convert All
Converts an array into another type

```C#
int[] nums = {1, 2, 3};

string[] strings = Array.ConvertAll(
    nums,   // From Array
    element => element.ToString()   // Convert Elements
);
```
