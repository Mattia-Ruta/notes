# Using Modules
Import <package> from <module>

```javascript
import React from "react";
import ReactDOM from "react-dom";
```

# Rendering Raw Elements on a Template
Create elements using JSX and saving to a variable, then rendering using ReactDOM

```javascript
import {createRoot} from "react-dom/client";

const container = document.getElementById("root");
const root = createRoot(container);
const heading = <h1>Heading Element</h1>;
 
root.render(heading);
```

# Conditional Statements
Using &&, if any element isn't a bool, it will return the last element

```javascript
true && "string"
// Returns "string"

true && "string" && 1
// Returns 1

// Truthy
1
"string"

// Falsey
0
""
```

- - - -

# React and Typescript
in APP.tsx you can combine Typescript and JSX

## State
Now you can use `useState()` to register a var

```javascript
import React, { useState } from "react";

function Example() {
    // [var name, function hook to update] = useState(initial value)
    const [count, setCount] = useState(0);

    return (
        <div>
            <p>Current value: {count}</p>
            <button onClick={
                () => {
                    // Generic function to call hook to update var
                    setCount(count + 1);
                }
            }>
                Click Here
            </button>

            {/* Pass var into component */}
            <TestComponent count={count} />
        </div>
    )
}

export default Example;
```
