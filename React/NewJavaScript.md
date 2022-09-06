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
