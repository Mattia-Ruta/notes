# Installation
Use NPM to install

`sudo npm install -g create-react-app`

# Create App
Create app in current directory

`create-react-app <appname>`

or Typescript app (NPX is the Node Package Excecute command)

`npx create-react-app <appname> --template typescript`

This creates the app <appname> which you can CD into

# First Steps
Inside the project run development server

`npm run`

As you save the code it auto-compiles if you have the dev server running using Babal

Useful library for React apps.. icons!

`sudo npm install react-icons --save`

Then import and use

```typescript
import { FaBeer } from "react-icons/fa";

class Question extends React.Component {
    render() {
        return <p>The beer icon: <FaBeer /></p>
    }
}
```
