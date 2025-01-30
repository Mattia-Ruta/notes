# Images and Assets

## [Image](https://api.flutter.dev/flutter/widgets/Image-class.html)

Renders an image, either via `NetworkImage` or `AssetImage`.

```dart
Image.network("https://onlineimage.png")
```

## [AssetImage](https://api.flutter.dev/flutter/painting/AssetImage-class.html)

Represents an image included in the project's assets.

Create an `assets` folder in the project with subfolders if needed. Drop in images.

In pubspec.yaml, add the dir to the `assets` property

```yaml
flutter:
    assets:
        - assets/
```
Be sure to reload project by clicking on "Get Dependencies"

Now you can reference the image using a relative URL to the image

```dart
Image.asset("assets/icons/citymapper.png"),
```

## [CircleAvatar](https://api.flutter.dev/flutter/material/CircleAvatar-class.html)

Circle with an image inside, great for a user profile image

```dart
CircleAvatar(
    backgroundImage: AssetImage("assets/image.png"),
    radius: 40.0,   // Size of the image
)

// You can also not have an image, but just text inside like initials
CircleAvatar(
    backgroundColor: Colors.grey,
    child: const Text("MR"),
)
```
