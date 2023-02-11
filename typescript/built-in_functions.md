# Variables and Types
Type hint using : symbol

```typescript
let uninitialised;  // Is of type Any.. avoid
let variable: number = 50;
let name: string = "Test String";
let is_true: boolean = true;
```
You may see big numbers have _ to separate 000s

```typescript
let big_number: number = 120_000_000;
```

Check type of variable with ``

# Functions
General Use

```typescript
// Always declare types, default values are optional
function calculateTax(income: number = 10_000): number {
    return income * 1.2;
}
// Second param is optional
function oneArg(arg1: number, arg2?: number): void {
    // Similar to Py's or, add default value
    if ((arg2 || 2022) > 2005) {
        // Uses arg2 or 2022 if empty
    }
}

// If you declare Any type, anything can be passed in
// Only use for ambiguous params
function print_param(input: any): void {
    console.log(any);
}
```
By default, a function that doesn't return anything actually returns undefined

# Objects
Objects in TS or JS are dynamic and change.. not like classes
```typescript
let employee {
    // Properties
    readonly id: number,    // Can't overwrite but readable
    age: number,
    name?: string   // Makes optional
} = {
    // Initial values for object
    id: 1,
    age: 20
};

// Overwriting properties
employee.name = "New Name";

// Retire method
let employee {
    id: number,
    name: string,
    retire: (date: Date) => void    // Header bit for a retire() method, needs to be implemented.. basically an abstract method
} = {
    id: 1,
    name: "Test Person",
    retire: (date: Date) => {
        console.log(date);
    }
}
```

# Enumerables
Default values for members are 0, 1, 2, etc.
If you set the first member to a number, the rest will add to that (sm=1, then md would be 2, etc etc)

```typescript
const enum Size {
    Small = 1,
    Medium = 2,
    Large = 3,
}
let objSize: Size = Size.Medium;
```

# Loops
## Foreach Loops - Standard
```typescript
array = [1, 2, 3];
for (let val of array) {
	console.log(val);
}
```

- - - -

# Arrays
```typescript
let varies = [1, "2", true];   // Can have different types
let nums: number[] = [1, 2, 3]  // Only numbers
let empty: number[] = [];    // ALWAYS typehint when initialising empty arrays
```

## Foreach Loops - Arrays

```typescript
numbers.forEach(function(value) {
    console.log(value);
})
```
# Tuples
Great for grouping two values together

```typescript
let user: [number, string] = [1, "Name"];
```
Unless specified as a tuple using `[number, number]`, TS will assume you mean `number[]` as an array. It is less restrictive
