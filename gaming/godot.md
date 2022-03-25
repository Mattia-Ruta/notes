# Project Setup
Adjust display and other project settings in:
`Project>Project Settings`

## Window Display Size
You can change window size here, like 480 x 720

`Display > Window`

You can change so it keeps the aspect when resizing in Stretch area here

Mode: 2d
Aspect: Keep

- - - -

# Nodes
Nodes are like GameObjects. It's like a class that gets inherited by other nodes.

## Inherited Nodes

* Node2D - Position, Rotation, and Scale

## Area Nodes - Collision Detection

* Area2D - Basic collision detection for 2D plane
* CollissionShape2D - Hitbox for 2D plane

## Animation Nodes

* AnimatedSprite - Appearance and animations for object (reqs SpriteFrames resource)

- - - -

# Animation and Sprites
To create a sprite, you will need to add the AnimatedSprite node an object.
Click on the AnimatedSprite and in the inspector you will need to add SpriteFrames. Click create, then click again to edit the Frames.

Add Animation frames on the left (or edit default) and drag the images in for the frames.

## Collision Detection
Add the CollisionShape2D node as a child to an object to create a hitbox.
In the inspector click shape and add a new shape. Use the handles to shape it to the object.

- - - -

# Scripts
You can attach scripts to objects by selecting it and pressing the 'attach script' button. Read GDScript markdown for syntax of the language.

# Player Input
Inside `Project > Project Settings > Input Map` you can set inputs to keystrokes. Add an action like `move_right` and assign the key `RIGHT` by pressing right arrow.  