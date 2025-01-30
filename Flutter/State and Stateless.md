# State and Stateless Widgets

## [StatelessWidget](https://api.flutter.dev/flutter/widgets/StatelessWidget-class.html)

Static Widget that doesn't change after initialisation

```dart
class GreenFrog extends StatelessWidget {
  const GreenFrog({ super.key });

  @override
  Widget build(BuildContext context) {
    return Container(color: const Color(0xFF2DBD3A));
  }
}
```

## [StatefulWidget](https://api.flutter.dev/flutter/widgets/StatefulWidget-class.html)

Dynamic Widget that can have data changed over time.
You can convert a Stateless widget into a Statefull one using the context actions

```dart
class Test extends StatefulWidget {
  const Test({super.key});

  @override
  State<Test> createState() => _TestState();
}

class _TestState extends State<Test> {
  int level = 0;

  void addLevel() {
    setState(() {
      level++;
    });
  }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: const Text("RPG ToDo"),
        centerTitle: true,
      ),
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: <Widget>[
          const Text("Current Level:"),
          Row(
            children: <Widget>[
              Text("$level"),
              ElevatedButton.icon(onPressed: () {addLevel();}, label: const Text("Add"), icon: const Icon(Icons.add),),
            ],
          ),
        ],
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          addLevel();
        },
        child: const Icon(Icons.add),
      ),
    );
}
```

- - - -

# Manipulating Data

## Lists

In a `State`, you can have a list of data, such as a list of strings

```dart
class _QuoteListState extends State<QuoteList> {
    List<String> quotes = [
        "quote1",
        "quote2",
        "quote3",
    ];

    // You can use map() to loop through the list and render a Widget per element
    @override
    Widget build(BuildContext context) {
        return Scaffold(
            body: Column(
                // Since children expects a list, just return a list version of the map return
                children: quotes.map((quote) => Text(quote)).toList(),
            ),
        );
    }
}
```



```dart
Column(
    children: quote
)
```
