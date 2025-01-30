# State Functionality

## MyAppState (Extends ChangeNotifier)

This is used to provide change notifications and represents app state

Vars and methods here can be accessed elsewhere in the code

```dart
class MyAppState extends ChangeNotifier {
    var WordPair current = WordPair.random();

    var WordPair[] favourites = <WordPair>[];
}
```
