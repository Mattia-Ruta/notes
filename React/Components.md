# Basic Component
Extend React.Component and return an element which is rendered

Inside the src dir, create a dir for components called `components`.

Inside this dir have every component separate by file `component.jsx` or `Component.tsx`

```typescript
import React from "react";

interface IProps {
    count: number
}

// Interface tells component what to expect as params
const Compt: React.FC<IProps> = (count: IProps) => {
    return (
        <div>
            <p>{count.count}</p>
        </div>
    )
}

export default Compt;
```

# Calling Components
Inside JS code now, you can pull components to render to the page

```typescript
import Comp from "./components/counter";

const container = document.getElementById("root");
const root = createRoot(container);
 
// Render the Compt component inside the root container
root.render(<Compt />);
```

## Using Properties
You can create a component that takes in params by creating the interface for it

```typescript
// (In App.tsx)
<Run count={1} />

// (In Component.tsx)
interface Props {
    count: number
}

const Run: React.FC<Props> = (count: Props) => {
    return (
        <div>
            <p>{count.count}<p>
        </div>
    )
}
```

- - - -

# Creating Callables
You can save functions as variables to be called inside a component

```typescript
const myArray = ["obj1", "obj2", "obj3"];


const Compt: React.FC = () => {
    // Since myArray.map() returns another array, return type is array of JSX Elements
    const myFunction = (): JSX.Element[] => {
        return myArray.map(
            // for elem in myArray
            (elem) => {
                return (
                    <p>{elem}</p>
                )
            }
        )
    }

    return (
        <div>
            {/* Call my function */}
            <p>{myFunction()}</p>
        </div>
    )
}

export default Compt;
```

- - - -

# Inputs and Forms Inside Components
Render a basic form as a component

```typescript
// ... to be continued
```
