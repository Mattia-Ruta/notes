# Main Notes

## File Structure

Main entrance point is the `lib/main.dart` file.
You can add folders to the project, like `fonts`

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

## Running Application

In dev, you can run by running the command `flutter run`

## Shortcuts and Menus

Flutter outline can be enabled by ctrl-clicking a Class name
