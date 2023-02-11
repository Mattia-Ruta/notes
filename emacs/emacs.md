Install with `sudo apt install emacs-nox`
C-<char> means Ctrl-<char>
M-<char> means Meta-<char> (Alt)
Settings file is in ~/.emacs

# Basics
SAVE: `C-x C-s`
Exit: `C-x C-c`
Ctrl-C in emacs: `C-g`

Find a file: `C-x C-f`
Suspend emacs: `C-z`
Resume with `fg` or `%emacs`

Kill all windows except current `C-x 1`
Change mode: `M-x text-mode`

Help commands: `C-h`
Close help window: `C-x 1`

Show menu bar: `F10` or `M-x menu-bar-open`

- - - -

# Movement

## Scrolling
Page Up: `M-v`
Page Down: `C-v`

## Cursor Movement
      ^
    `C-p`
<`C-b` `C-f`>
    `C-n`
      V

`M-a` Beginning of sentence | End of sentence `M-e`

`C-a` Home |<< >>| End `C-e`

`M-<` Beginning of buffer || End of buffer `M->`

Move cursor to middle of screen: `C-l` then again to top

# Text Commands
Use `C-u <num>` to repeat next command 8 times (or characters if next is char)

Delete all chars from curser to end of line: `C-k`

Set mark: `C-Space` then `C-w` to cut highlighted text

Paste: `C-y`
Undo: `C-/` or `C-x` or `C-x u`

- - - -

# Buffers
List buffers: `C-x C-b` - Then `C-x 1` to hide list
Switch to buffer: `C-x b` (You'll need to know the buffer name to switch to)
or defaults to last buffer

`*Messages*` buffer shows messages from emacs

Save some buffers: `C-x s` - Will ask which buffers to save

Recovering file if crashed, open file to recover and `M-x recover-this-file`

# Searching
Initiate a search: `C-s` then again to find next iteration or `C-r` to go backward
(`C-g` to cancel)

# Windows / Panes
Move cursor to top because new window shows on bottom - `C-l C-l`

New window opens current file: `C-x 2`
Or open other file instead: `C-x 4 C-f`

Scroll bottom window without leaving top window: `C-M-v`
Switch between windows: `C-x o`
Close other window; `C-x 1`

## Frames (Windows)
New frame `C-x 5 2`
Close frame `C-x 5 0`

- - - -

# Packages with Melpa
Install Melpa package list
```lisp
(require 'package)
(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/") t)
(package-initialize)
```

List packages with `M-x package-refresh-contents`
Then `M-x package-list-packages`

Put cursor on line for package you want to install and press `i` to mark for installation
Or put `u` to mark for upgrade
Then press `x` to initiate install

- - - -

# Colour Theme
Place cursor over a font face to change and press `C-u C-x =` to open editor
