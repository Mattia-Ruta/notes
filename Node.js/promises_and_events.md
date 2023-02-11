# Promises
Promises await the result of a callback
```typescript
const getText = (path) => {
    return new Promise(
        (resolve, reject) => {
            runFunctionHere(error, data) => {
                if (error) {
                    // Call reject to reject the promise
                    reject(error);  // Saves error as message why it failed
                } else {
                    // Call resolve to fufill the promise with data
                    resolve(data);
                }
            }
        }
    )
}
```
## Promise Built-in Functions
You can attach callbacks to promises depending on situation
```typescript
const prom = new Promise(...);

// Attach a function for if an error occurs
prom.catch(
    (reason) => {
        // Log reason for failed promise
        console.log(`Error: ${reason}`);
    }
);

// Attach a function for success
prom.then(
    (response) => {
        // Log returned response from promise funct
        console.log(response);
    }
);

// Attach a funct to run regardless of ending
prom.finally();

// You can chain multiple callbacks to the promise
prom.fetch()
    .then()
    .catch();
```

- - - -

# Events
Use the events module to create an event using the EventEmitter class
```typescript
import { EventEmitter } from "events";

const customEmitter = new EventEmitter();

// Attach callback to event listener.. make sure to add listener before invoking!
customEmitter.on(
    // Name of event to listen for
    "response",
    // Callback when event invoked / emitted
    (arg1, arg2) => {
        // You can use arguments passed from events
        console.log(`Data Received: ${arg1} and ${arg2}`);
    }
);

// Pass in name of event being emitted and any args you want to pass along
customEmitter.emit("response", "arg1", "arg2");

```
