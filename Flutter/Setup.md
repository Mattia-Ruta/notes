# Flutter Setup

## Initial

1. Download Flutter SDK from the Flutter Website
1. Install Android Studio or another IDE
1. Check the install using `flutter doctor`

## Starting New Project

`flutter create new_app`

Now you can open the new directory in an IDE

## Pubspec.yaml file

Main project file for the Flutter process.
This tells the dependencies needed to run the application.

You can map custom fonts to their .ttf files using the `fonts` prop

```yaml
fonts:
    - family: IndieFlower   # Custom name for this font to refer to
    fonts:
        - asset: fonts/Schyler-Regular.ttf  # Location of fonts file, make sure this exists

```

- - - -

## Troubleshooting

If when running `flutter doctor` you get the missing cmdline-tools,
In Android Studio go Tools > SDK Manager > SDK Tools, then tick `Android SDK Command-line Tools`


