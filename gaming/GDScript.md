# Creating Scripts
Once you attach a script, you have to extend a base class. If you don't specify it will extend `Reference`.

```
extends Sprite
```

# Properties and Variables
Properties are inherited from their parent classes and can be shown by hovering over the property in the inspector to view the property name (usually snake_case).

Use the keyword `export` to be able to edit variables in the inspector
```
export var speed = 400
var angular_speed = PI
```
- - - -

# Main Functions 

## start(pos)



## init()
Initial function gets called when object gets created in memory

```
func _init():
    print("hello, world!")
```

## ready()
Ready function gets called when node enters the scene tree for the first time. Usually good to find screensize in this funct

```
func _ready():
    var screen_size = get_viewport_rect().size
```

## process()
Process runs *every frame* with `delta` being the time elapsed since the last frame.

Always times movement calculations against delta so movement speed is independant of framerate. If framerate drops the movement will remain stable.

```
func _process(delta):
    rotation += angular_speed * delta
```
- - - -

# Node Functions

## get_node(str node) - returns node or null
Finds the node by name relative to current object script is attached to. If it's a direct child from the object, you can just call the name. If it's in the same level as the scripted object, you can use filesystem notation for referencing the name.

```
get_node("AnimatedSprite")
$AnimatedSprite # Shorthand notation for same thing

get_node("../OtherObject")  # Object at same level in hierarchy
```

## clamp(float value, float min, float max)
Restricts values within a given range. Mostly used to keep objects inside the screen. 

## show()
Shows the node

## hide()
Hides the node

```
position.x = clamp(position.x, 0, screen_size.x)
position.y = clamp(position.y, 0, screen_size.y)
```

## emit_signal(str signal)
Invokes the signal passed in the param

- - - -

# Vectors

## Vector2
2D vector represents movement on 2D plane using two points, x and y

### Properties and Constants

* x - Right is higher x, Left is lower x
* y - Down is higher y, Up is lower y

Constants represent points to make it easy

```
Vector2.UP  # Same as Vector2(0, -1)
Vector2.DOWN    # Same as Vector2(0, 1)
Vector2.LEFT    # Same as Vector2(-1, 0)
Vector2.RIGHT   # Same as Vector2(1, 0)
Vector2.ZERO    # Same as Vector2(0, 0)
```

### Methods

Rotation - Returns vector rotated by phi radians. Pass in rotation property to rotate object relative to its own current rotation

```
Vector2.UP.rotated(rotation) * speed
```

- - - -

# Player Input
After mapping keys to actions, you can detect if an action happened using action_pressed

```
func _process(delta):
    # Reset velocity to 0 every frame
    var velocity = Vector2.ZERO

    # Check if move_right actioned happened
    if Input.is_action_pressed("move_right"):
        velocity.x += 1
```

Also make sure you normalise the velocity if the char is moving diagonally

```
if velocity.length() > 0:
    velocity = velocity.normalized() * speed
```

- - - -

# Animation Scripting
You can set which animation frames to use by setting the `animation` property. *Make sure the name is exactly the same as the animation name*

```
$AnimationSprite.animation = "walking_animation"
```

You can play/stop animations in scripts by calling `play()` or `stop()`

```
$AnimationSprite.play()
```

You can flip animation images using `flip_h` and `flip_v` (flipping vertically and horizontally) bools

A common setup for sprites flips:

```
if velocity.x != 0:
		$AnimatedSprite.animation = "walking"
		$AnimatedSprite.flip_v = false
		$AnimatedSprite.flip_h = velocity.x < 0
	elif velocity.y != 0:
		$AnimatedSprite.animation = "up"
		$AnimatedSprite.flip_v = velocity.y > 0
```

- - - -

# Signals (Events)
Declare a signal on the top of the script, similar to events in C#. once it's declared you can see it in the `Node` tab next to the inspector

```
signal hit
```

In the `Node` tab, you can see all the signals the object can emit. Click `Connect...` to subscribe functions to events.

* body_entered(body: Node) - Invoked when a Body node contacts the object

Once you connect a signal to a method, it will create the event method subscribed to that signal.

```
func _on_Player_body_entered(body):
    # Runs when body_entered signal gets invoked
    emit_signal("other_signal")

    # Disables the collision until it's safe to turn on again
    $CollisionShape2D.set_deferred("disabled", true)
```

Invoke signals using `emit_signal` and use the name as a string

- - - -

# Debug and Testing
Run currently open script using `F6`

