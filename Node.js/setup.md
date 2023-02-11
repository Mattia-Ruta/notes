Go on website to download Node
Run compiled scripts using node CLI

`node script.js`

Setup TypeScript in a project by using 

`npm install --save-dev @types/node`

- - - -

# Project Setup

Set up project base

`npm init`

This creates the package.json file in the project, add the main script to start script

```json
{
  "dependencies": {
    "@types/node": "^18.8.2",
    "bootstrap": "^5.2.2"
  },
  "name": "budgets",
  "description": "Budgeting app",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "start": "node dist/index"
  },
  "author": "Mattia Ruta",
  "license": "ISC"
}
```

Now you can start the app using `npm start`
