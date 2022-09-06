# Basic Component
Extend React.Component and return an element which is rendered

Inside the src dir, create a dir for components called `components`.

Inside this dir have every component separate by file `component.jsx`

```javascript
import React, {Component} from "react";

class Counter extends Component {
    render() {
        // Element to render to screen
        return <h1>Test Text</h1>;
    }
}

export default Counter;
```

# Calling Components
Inside JS code now, you can pull components to render to the page

```javascript
import Counter from "./components/counter";

const container = document.getElementById("root");
const root = createRoot(container);
 
// Render the Counter component inside the root container
root.render(<Counter />);
```

## Using Properties
You can create a component that takes in params

```javascript

```
