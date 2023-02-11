# Setup and Configuration

## Installing Typescript
After installing nodejs, use NPM to install typescript

`sudo npm i -g typescript`

(I for install and G for global)

Once TS is installed, check the version

`tsc -v`

## Configuring Compiler
Create the config file for project

`tsc --init`

```json
"target": "es2016", // JS version to use
"rootDir": "./src", // Source TS dir to use
"outDir": "./dist", // Compiled dir for JS files
"removeComments": true, // Min's JS files and removes comments
"noEmitOnError": true,  // Aborts compiling if it finds errors
"sourceMap": true,  // Creates source maps for debugging
```

[Extra Options]

```json
"noImplicitAny": false, // Turns off strict type hinting for Any type
"noUnusedParameters": true, // Add strict standard where all params must be used
"noImplicitReturns": true,  // Forces all functs to return something
"noUnusedLocals": true, // Forces all declared vars to be used
```

Once config file is set up, you can compile all TS files into JS

`tsc`

## Configuring Debugger in VSCode
1. Click on Run and Debug tag on left
2. Click on `create a launch.json file`
3. Select `Node.js` in dropdown
4. In launch.json change type to "node"
5. Add `"preLaunchTask": "tsc: build - tsconfig.json",` under program
