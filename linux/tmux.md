# TMUX
For multiple terminal windows built into terminals (servers)

- - - -

# Installation
`sudo apt install tmux`

## Configuration
Create the file `~/.tmux.config` for settings

Then edit the file, for example

```bash
# Status Bar
set -g status-fg green
set -g status-bg black

# History Limit
set -g history-limit 10000

# Pane Navigation
bind -n M-Left select-pane -L
bind -n M-Right select-pane -R
bind -n M-Up select-pane -U
bind -n M-Down select-pane -D

# Mouse Mode
set -g mouse on

# Hostname Colour
set -g default-terminal "xterm-256color"
```

For Colour, edit ~/.bashrc and uncomment colour prompt:

```bash
force_color_prompt=yes
```

- - - -

# Sessions
Every tmux session can have as many windows as you like

## Create Session
Generic Name

`tmux`

Custom Name

`tmux new -s session_name`

## Detaching / Attaching from Session
Detach from current session 

`ctrl-B d` for Detach

Attach to a session

`tmux attach-session -t 0`

Attach to last session 

`tmux attach`

## List Sessions
`tmux ls`

- - - -

# Inside Sessions

## Scrolling
Scroll through the window using 

`ctrl-B [` then arrow keys--`esc` to exit

## Panes
Split Window into two panes next to each other
*Add pane to the right*

`ctrl-B %`

Split Window into two panes on top of each other
*Add pane to the bottom*

`ctrl-B "`

NEXT

`crtl-B o`

PREV

`ctrl-B ;`

Close current pane

`ctrl-B x` or `exit`

## Windows (Can have multiple panes in each window)
New Window

`ctrl-B c`

List Windows

`ctrl-B w`

Switch to specific Window (by window number)

`ctrl-B 0`

Rename Current Window

`ctrl-B ,`

