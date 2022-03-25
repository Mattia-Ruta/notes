# C Sharp

- - - -

# New Programme
To create a new programme run new with the type given.
More info: https://docs.microsoft.com/en-gb/dotnet/core/tools/dotnet-new

`dotnet new [Type] -o Name`

Types
* console | new Console Application
* webapi | ASP.NET Core Web API

* -o | Output - Names the programme dir

This will create the dotnet project folder.

The main script is `Name.cs` inside the project folder.

## Console App
Using the command `dotnet new console -o Program` you create a console app

You can specify a framework to use like .NET 6

`dotnet new console --framework net6.0 -o Program`

- - - -

# Running DotNet
To run dotnet apps you will need to create a windows executible.
Make sure you have Mono installed to run `mcs`

## MCS - Compiler
Creates an exe file from the project so you can run it

`mcs [Options] Program.cs`

Options
* -out:<filename> | Specify filename

Then you can run the .exe

`./Program.exe`

## Dotnet
Use can use dotnet to run inside the project dir

`dotnet run`

- - - -

# Mono
Mono is an open-source implementation of the .NET framework

Installation

`sudo apt install mono-complete`

Run dotnet

`mono Program.exe`

# Namespacing and Main Programme Template
If you're writing a CLI programme you should define a namespace.
A good starting point is

````C#
namespace Practice {
    class Program {
        static void Main(string[] args) {
            // Main Code Here
        }
    }
}
````

The `System` namespace has a lot of basics

# Built-in Functions
Write a line to the console

`Console.WriteLine("Write this");`

Read line from user input

`string name = Console.ReadLine();`

Explicit Casting (Double to Int)

`int myInt = (int) myDouble;`

You can Convert as well (Int to String)

`string myString = Convert.ToString(myInt);`

Current time

`Datetime.Now`

- - - -

# Math Functions
Math is super useful with many built in functions

````C#
Math.Max(5, 10); // Returns higher number
Math.Min(5, 10); // Returns lower number
Math.Sqrt(64); // Returns square root
Math.Abs(-4.7); // Absolue value
Math.Round(9.99); // Rounds to nearest whole number
````

# String Functions
Manipulating strings

````C#
string text = "string of text";
text.ToUpper(); // Makes ALL CAPS
text.ToLower(); // Make all lower case
````

Format Strings

````C#
string name = $"My name is: {surname}, {firstName}";
````

Find Character in string

````C#
string myString = "Hello";
Console.WriteLine(myString.IndexOf("e")); // Prints 1
````

- - - -
