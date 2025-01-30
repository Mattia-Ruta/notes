# Built-In Widgets

## [AppBar](https://api.flutter.dev/flutter/material/AppBar-class.html)

Title bar that goes on the top, under the status bar

```dart
AppBar(
  backgroundColor: Theme.of(context).colorScheme.inversePrimary,
  title: Text(widget.title), // Or any text
  centerTitle: true,  // To center the text
)
```

## [ElevatedButton](https://api.flutter.dev/flutter/material/ElevatedButton-class.html)

Raised button with text and a callback

```dart
ElevatedButton(
    onPressed: () {},
    child: Text("Button Text"),
    color: Colors.lightBlue,    // Colour of the button, not the text
)
```

There is also the `FlatButton` class.

You can also use an icon + text for the elevated button:

```dart
ElevatedButton.icon(
    onPressed: () {},
    label: Text("Button Text"),
    icon: Icon(Icons.add_circle_outline),
)
```

Or just use an icon which is clickable

```dart
IconButton(
    onPressed: () {},
    icon: Icon(Icons.alternate_email),
    color: Colors.amber,
)
```

## [Card](https://api.flutter.dev/flutter/material/Card-class.html)

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

## Divider

Adds a horizontal rule

```dart
Divider(
    height: 60.0,   // Space it takes up, not the thickness of the line
    color: Colors.grey,
    thickness: 5.0, // Actual thickness of the line
)
```

## [Floating Action Button](https://api.flutter.dev/flutter/material/FloatingActionButton-class.html)

Bottom right button

```dart
FloatingActionButton(
  child: Text("Button Text"),
  onPressed: () {}, // Required, gets called when pressed
  backgroundColor: Colors.red,
)
```

## [Text](https://api.flutter.dev/flutter/widgets/Text-class.html)

Basic text widget, you can add styling using textTheme

```dart
@override
Widget build(BuildContext context) {
    final theme = Theme.of(context);

    // Styling Text using text themes
    final style = theme.textTheme.displayMedium!.copyWith(
        color: theme.colorScheme.onPrimary, // This will style the text based on what looks good on primary colour
        fontSize: 20.0,
        fontWeight: FontWeight.bold,
        letterSpacing: 2.0,
        color: Colors.grey[600],
        fontFamily: "IndiFlower",   // You can add custom fonts via pubspec.yaml
    )
    // More on styling text in the Styling and Icons.md file

    return Text(
        "Text to render",
        style: style,
        semanticsLabel: "Semantic Text" // For accessibility
    );
}
```

There are built-in text theme elements for typography

```dart
textTheme.displayMedium // Meant for big display text
```
- - - -

# Containers, Col's and Rows

## [Column](https://api.flutter.dev/flutter/widgets/Column-class.html)

```dart
Column(
    mainAxisAlignment: MainAxisAlignment.center,    // Vertical
    crossAxisAlignment: CrossAxisAlignment.center,    // Horizontal
    children: [
        Text("test")
    ]
);
```

## [Container](https://api.flutter.dev/flutter/widgets/Container-class.html)

Basic container Widget.
The size of the container restricts itself to the size of the child it contains

```dart
/* Padding will add spacing around the child of the Container obj,
    while Margin adds space around the container obj itself.

    The EdgeInsets class has some built in functions,
    and can be used for both padding and margin.
    - all(float) - All sides
    - fromLTRB(float, float, float, float) - Left, Top, Right, Bottom
    - symmetric(horizontal: float, vertical: float) Not positional */
padding = EdgeInsets.all(20.0);
margin = EdgeInsets.fromLTRB(10.0, 20.0, 30.0, 40.0);

Container(
    color: Colors.grey[400], // Background colour of the entire container
    padding: EdgeInsets.all(20.0)   // Will add space in between all children inside
    margin: EdgeInsets.all(30.0)    // Will add space around the container itself
    child: Text("test") // Child of the container
)
```

If you want a container with *just* Padding or Margin, use the `Padding()` Widget

```dart
Padding(
    padding: EdgeInsets.all(20.0),
    child: Text("Text inside the container"),
)
```

## [Expanded](https://api.flutter.dev/flutter/widgets/Expanded-class.html)

Expands size of the child as big as it can go inside the row, column, etc

```dart
Expanded(
    child: Container(
        padding: EdgeInserts.all(30.0),
        color: Colors.red,
        child: Text("test"),
    )
)
```

You can use the flex property to give more space to specific Expanded containers.
The flex breaks down the sizing into the sum of all the flexes in the row/col.
This works great for giving more space to images in a row

```dart
// This breaks the row into 12 and assigns the space to the children based on the flex property
Row(
    children: <Widget>[
        Expanded(
            flex: 6,    // Makes the image bigger than the text elements
            child: Image.asset("assets/image.png"),
        ),
        Expanded(
            flex: 3,
            child: Text("Small cell"),
        ),
        Expanded(
            flex: 3,
            child: Text("Also small cell"),
        )
    ]
)
```

## [Row](https://api.flutter.dev/flutter/widgets/Row-class.html)

Represents a CSS row with multiple children, which will line them up in a row

```dart
Row(
    children: <Widget>[
        Text("First Child"),
        Text("Second Child"),
    ]
)
```

## [Scaffold](https://api.flutter.dev/flutter/material/Scaffold-class.html)

Main container type

```dart
return Scaffold(
  appBar: AppBar(),
  body: Center(),
  floatingActionButton: FloatingActionButton(),
);
```

# Positioning and Adjustment

## MainAxisAlignment

You can position children using the MainAxisAlignment consts.
Most Widgets have a `mainAxisAlignment` property you can adjust

```dart
return Scaffold(
  body: Column(
    mainAxisAlignment: MainAxisAlignment.center // Vertical Alignment
  )
)
```
