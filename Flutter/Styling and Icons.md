# Styling

## Padding

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
See the `Container()` widget for more options

You can also use the `SizedBox` widget which is empty space

```dart
SizedBox(height: 20)
```

## Centering and Placement

You can centre a column by rightclicking, selecting refactor, and wrap with Center

- - - -

## [MainAxisAlignment](https://api.flutter.dev/flutter/rendering/MainAxisAlignment.html) and [CrossAxisAlignment](https://api.flutter.dev/flutter/rendering/CrossAxisAlignment.html)

Main Axis runs as the main direction, so horizontal for row and vertical for column.The cross axis, however, runs the opposite--so vertical for row and horizontal for column.

```dart
Row(
    mainAxisAlignment: MainAxisAlignment.center,    // Horizontal
    crossAxisAlignment: CrossAxisAlignment.center,  // Vertical
)

Column(
    mainAxisAlignment: MainAxisAlignment.center,   // Vertical
    crossAxisAlignment: CrossAxisAlignment.center,  // Horizontal
)
```

These apply to both the Main Axis and Cross Axis.
* start - Default for a row, aligns them from left
* center - Centers items
* end - Aligns from right
* spaceBetween - Spaces them all out evenly from both sides [0  0]
* spaceEvenly - Spaces them out evenly, including from the sides of the first and last item [ 0 0 ]
* spaceAround - Spaces evenly, with some extra space on the sides

## Sizing

You can adjust the size of `Container()`, `Expanded()`, etc

```dart
Container(
    color: Colors.blue,
    height: 100,
    width: 100,
)
```

## [TextStyle](https://api.flutter.dev/flutter/painting/TextStyle-class.html)

With the `TextStyle` Widget you can style text

```dart

var style = TextStyle(
    color: Colors.white,
    letterSpacing: 2.0,  // Space between each letter
    fontSize: 20.0,
    fontWeight: FontWeight.bold,
);

Text(
    "Text",
    style: style,
);
```

# Colors

Colors class has built in colours and colour theme

```dart
// Built-in colours
Colors.red

// Deeper red
Colors.red[600]

// From specific value
Color.fromARGB(255, 255, 0, 0); // 0-255 A (Opaqueness) RGB
```

- - - -

# [Icon](https://api.flutter.dev/flutter/widgets/Icon-class.html)

Represents an icon to render.

The [Icons](https://api.flutter.dev/flutter/material/Icons-class.html) class contains all the icons

```dart
// Some built-in icons
Icon(
    Icons.airport_shuttle,   // Auto-suggest has previews for this
    color: Colors.lightBlue,
    size: 50,
)
```
