# Define a Promise
Create callback that returns anything after it's done, either by resolve or reject.

```javascript
let dbPromise = new Promise(
    (resolve, reject) => {
        // Run code here
        //..

        // You can pass anything into the resolves and rejects, in this case just a string
        if (success) resolve("Success Message");
        else reject("Fail Message");
    }
);
```

# Calling Single Promise
Now you can call the promise and run functions in success or failure
```javascript
dbPromise().then(
    // Success callback, msg is passed from resolve() arg
    (msg) => {
        console.log(`Success!: ${msg}`);
        // You can return a promise in a then
    }
).catch(
    // Failure callback, msg is passed from reject() arg
    (msg) => {
        console.error(`Error!: ${msg}`);
    }
);
```

# Calling Multiple Promises

## Run All Promises
Call all promises using Promise.all passed in using an array

```javascript
// Pass in array of all promised to do before the then() callback
Promise.all([
    promise1,
    promise2,
    promise3
]).then(
    // All messages from all resolve() args are saved in an array
    (messages) => {
        console.log(messages);
    }
).catch(
    (messages) => {
        console.error(messages);
    }
)
```

## Race! Run Callback after first Promise
Using Promise.race(), the then() callback is called after the first promise resolves.
```javascript
// Will run .then() after first one finishes, ignoring the rest
Promise.race([promise1, promise2]).then((msg) => {console.log(msg)});
```

- - - -

# ASync Await
The await keyword waits until a promise is resolved before continuing

Creating an async function returns a Promise
```javascript
// You await promises
let waitPromise = () => {
    return new Promise((resolve, reject) => {
        if (true) resolve();
        else reject();
    });
}

// General use
async function order() {
    try {
        console.log("starting");
        // Calls promise and won't continue in block until promise resolves
        await waitPromise().then(() => console.log("waitPromise() resolved!"));
    } catch (err) {
        console.error("Error: ", err);
    } finally {
        console.log("Runs even if failed");
    }
}

// Call funct like normal
order()
    // You can chain then() functs for after function runs
    .then(() => console.log("After done"));
// Since order() is async, the rest of the code will run while order runs
console.log("Will run before order() finished");
```

```javascript
// These run at the same time
const wesData = axios.get("https://wesdata.co.uk");
const scottData = axios.get("https://scottdata.co.uk");

// Wait for both data promises to come back before continuing
const [wes, scott] = await Promise.all([wesData, scottData]);
// Now you have access to both wes and scott vars with the data
console.log(wes.name);
console.log(scott.name);
```

## Error handling
Try / Catch works well even with async

```javascript
try {
    const wes = await axios.get("https://wesdata.co.uk");
    console.log(wes);
} catch (err) {
    console.log(err);
}
```
