# Installation
Use NPM to install SQLite3

`npm install sqlite3`

# Connecting
Connect to a database in memory

```javascript
// Require Module
const sqlite3 = require("sqlite3").verbose();

// In memory database
let db = new sqlite3.Database(":memory:");

// Or use a DB file in the same directory
let db = new sqlite3.Database("file.sqlite");

// Be sure to add error checking
let db = new sqlite3.Database(":memory:", (err) => {
    if (err) console.error(err.message);
    console.log("Successfully connected to the database");
});

// Always close the DB when you're done
db.close();
```
