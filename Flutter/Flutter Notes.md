# Main Notes

## File Structure

Main entrance point is the `lib/main.dart` file

- - - -

## Main.dart

This is where the entrance point of the app starts.

```dart
import "package:flutter/material.dart";

// Needed for App to run
void main() {
    // MyApp class below
    runApp(MyApp());
}

// StatelessWidget is the base component for everything in Flutter
class MyApp extends StatelessWidget {
  const MyApp({super.key});

  /*
    Every Widget comes with a build method,
    override this to add logic to the building of the widget
  */
  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (context) => MyAppState(),  // Subscribes to ChangeNotifier object
      child: MaterialApp(
        title: "App Name",
        theme: ThemeData(
          useMaterial3: true,
          colorScheme: ColorScheme.fromSeed(seedColor: Colors.red),
        ),
        home: MyHomePage(), // Sets main widget to run when built
      )
    )
  }
}

// ChangeNotifier provides "notifications" or invokes events
class MyAppState extends ChangeNotifier {
  var currentWord = WordPair.random();

  void next() {
    // When this gets called, it will create a new word
    current = WordPair.random();

    // This invokes the actual event so subscribed functs will run
    notifyListeners();
  }
}

class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    /* Pulls current state and subscribes var to state events.
      This means the build() funct will be called every time the event gets invoked */
    var appState = context.watch<MyAppState>();

    /* We want to extract just the var.
      This is so we don't keep accessing the entire MyAppState obj.
      Don't use the entire appState var all the time
    */
    var word = appState.current

    return Scaffold(
      body: Column(
        children: [
          Text("A Random Word:"),
          Text(word.asLowerCase),
          ElevatedButton(
            onPressed: () {
              print("button pressed");  // Log to console

              // Trigger state change
              appState.next();
            },
            child: Text("Generate Word")
          )
        ]
      )
    )
  }
}
```
### Extracting Widgets

If you have a bit of code you want to create a new widget for:
1. Highlight the code you want to extract (ex: `Text(word)`)
1. Right-Click and click on `Refactor`
1. Click on `Extract Widget`
1. Name the new widget

This will then appear below the code extracted as a new widget

## Styling

### Padding

Easy way to add padding is:
1. highlight a widget class (like `Text`)
1. Right-Click and click on `Refactor`
1. Click `Wrap with Padding`

This also works for wrapping with columns, rows, etc

```dart
...
return Padding(
  padding: const EdgeInsets.all(8.0),
  //padding: const EdgeInsets.only(top: 20),  // for specific sides
  child: Text("original text widget"),
);
...
```

### Colors

Colors class has built in colours and colour theme

```dart
// Built-in colours
Colors.red

// From specific value
Color.fromARGB(255, 255, 0, 0); // 0-255 A (Opaqueness) RGB
```

## Built-In Widgets

### Text

Basic text widget, you can add styling using textTheme

```dart
@override
Widget build(BuildContext context) {
  final theme = Theme.of(context);
  final style = theme.textTheme.displayMedium!.copyWith(
    // This will style the text based on what looks good on primary colour
    color: theme.colorScheme.onPrimary,
  )

  return Text("Text to render", style: style);
}
```

### Card

Rounded corners card with background colour from theme

```dart
// Be sure to extract theme from the context
final theme = Theme.of(context)
Card(
  color: theme.colorScheme.primary,
  child: Padding(
    padding: const EdgeInsets.all(20),
    child: Text("Text inside the card")
  ),
);
```

- - - -

More info on main page stuff
```dart
class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      // This call to setState tells the Flutter framework that something has
      // changed in this State, which causes it to rerun the build method below
      // so that the display can reflect the updated values. If we changed
      // _counter without calling setState(), then the build method would not be
      // called again, and so nothing would appear to happen.
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called, for instance as done
    // by the _incrementCounter method above.
    //
    // The Flutter framework has been optimized to make rerunning build methods
    // fast, so that you can just rebuild anything that needs updating rather
    // than having to individually change instances of widgets.
    return Scaffold(
      appBar: AppBar(
        // TRY THIS: Try changing the color here to a specific color (to
        // Colors.amber, perhaps?) and trigger a hot reload to see the AppBar
        // change color while the other colors stay the same.
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: Text(widget.title),
      ),
      body: Center(
        // Center is a layout widget. It takes a single child and positions it
        // in the middle of the parent.
        child: Column(
          // Column is also a layout widget. It takes a list of children and
          // arranges them vertically. By default, it sizes itself to fit its
          // children horizontally, and tries to be as tall as its parent.
          //
          // Column has various properties to control how it sizes itself and
          // how it positions its children. Here we use mainAxisAlignment to
          // center the children vertically; the main axis here is the vertical
          // axis because Columns are vertical (the cross axis would be
          // horizontal).
          //
          // TRY THIS: Invoke "debug painting" (choose the "Toggle Debug Paint"
          // action in the IDE, or press "p" in the console), to see the
          // wireframe for each widget.
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text(
              'You have pushed the button this many times:',
            ),
            Text(
              '$_counter',
              style: Theme.of(context).textTheme.headlineMedium,
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: const Icon(Icons.add),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}

```

## Running Application

In dev, you can run by running the command `flutter run`

