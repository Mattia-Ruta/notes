# Variable
Global variables

```javascript
__dirname;
__filename;
require() // To use modules from CommonJS
module // Info about current module or file
process // Info about environment where program is executed
```

## Strings
Template Literals

```typescript
const name = "Test Name";
// Input vars using backticks and ${}
console.log(`My name is ${name}`);
```

- - - -

# Modules
Every file is a module in Node
The module global object has info on current module, including exported functs and vars.

```typescript
// TS way of exporting
const var1 = "var";
export { var1 };

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

// New way, import from module - if default
import MyClass as ClassName from "moduleName";

// Or pull from multiple exports
import { var1 } from "path";

// Import built-in modules using import
import os from "os";

// exportedModule.<var>
console.log(exportedModule.var1);
```

# Built-in Functions
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

- - - -

# Built-in Modules
## OS
Has some good built in info on the OS

```typescript
import os from "os";

// uid, gid, username, homedir, and which shell
const user = os.userInfo();

// System uptime in seconds
const uptime = os.uptime();

// System Info
os.type()   // Linux, Windows, etc
os.release()    // 5.4.0-126-generic
os.totalmem()   // Total memory
os.freemem()    // Free memory
```

## PATH
Pathing module, similar to Py Path

```typescript
import path from "path";

// Returns separator used for filepaths, like / for linux
path.sep;

// Normalise dirs and filename to a path, will be /folder/sub_folder/file.csv
const filePath = path.join("./folder", "sub_folder", "file.csv");

// With the filepath you can find just the base of it (file from file.txt)
const base = path.basename(filePath);

// Resolve to an absolute path using current file
const absolute = path.resolve(__dirname, "folder", "sub_folder", "test.txt");
```

## FileSystem - FS
Manipulate filesystem using FS module

```typescript
import fs from "fs";

// Read file sync - will wait to finish before continuing
const file = fs.readFileSync("./file.txt", "utf8");

// Write to file - rewrites file by default if exists, use 'a' flag to append instead
fs.writeFileSync(
    "./file.txt",
    "This is the data to write",
    { flag: "a" }
);

// Asynchronise way runs the callback function when complete
fs.readFile(
    "./test.txt",
    "utf8",
    (e, data) => {
        if (e) {
            console.log(e);
        } else {
            console.log(data);
        }
    }
);
```
You can read and write to streams in memory instead of using variables
```typescript
import { createReadStream } from "fs";
const stream = createReadStream("./path/to/file.txt");
stream.on("data", (chunk) => {
    // Log every 64b chunk
    console.log(chunk);
})

```

## HTTP
Spin up a basic server
```typescript
import http from "http";

const server = http.createServer(
    (request, response) => {
        response.write("HTTP Response");    // Basic HttpResponse
        response.end(); // End response and send
    }
)

server.listen(8000);
```
