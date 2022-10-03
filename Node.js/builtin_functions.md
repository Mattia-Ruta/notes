# Variable
Global variables

```javascript
__dirname;
__filename;
require() // To use modules from CommonJS
module // Info about current module or file
process // Info about environment where program is executed
```
# Modules
Every file is a module in Node
The module global object has info on current module, including exported functs and vars.

```javascript
// module.js
// Set only one thing as default export from module to make public
module.exports = var1;
// Multiple vars and functs as an object
module.exports = {var1, var2};
// Or initiate a var directly in exports
module.exports.var1 = var1;

console.log(module.exports);    // Accessible through module var
```
Then use require() or import to pull exported variables

```javascript
// Import whole module with exports as an object within
const exportedModule = require("./module");
// Pull just specific vars or functs from module
const {var1} = require("./module");

// New way, import from module
import MyClass as ClassName from "moduleName";

// exportedModule.<var>
console.log(exportedModule.var1);
```

# Built in Functions
## Set Interval
Pass a function into setInterval() to run it every <arg2> miliseconds

```javascript
setInterval(
    () => {
        console.log("test");
    },
    1000    // Run every second
)
```
