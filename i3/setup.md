## Computer Setup

Required packages:
- pactl
- feh
- xrandr
- lxappearance
- xss-lock
- brightnessctl (if using laptop)

### Brightness Control Setup

`sudo usermod -aG video user`

`sudo usermod -aG input user`

### Fonts Setup

`mkdir ~/.fonts`

Install Yosemite San Francisco font by downloading the zip and moving the .ttf files to ~/.fonts

Run lxappearance and save something to generate gtk files

Edit the font name to "System San Francisco Display 10" in:
- ~/gtk-2.0
- ~/.config/gtk-3.0/settings.ini

### i3Status Setup

Create a new directory for the config file

`mkdir ~/.config/i3status`

And create a config file here

### Enabling Tap-To-Click

Run the following command:

```bash
sudo mkdir -p /etc/X11/xorg.conf.d && sudo tee <<'EOF' /etc/X11/xorg.conf.d/90-touchpad.conf 1> /dev/null
Section "InputClass"
        Identifier "touchpad"
        MatchIsTouchpad "on"
        Driver "libinput"
        Option "Tapping" "on"
EndSection

EOF
```

Then logout and in again to apply

## Adding Flatpak

Add Flatpak programs to D-Menu by copying into the /usr/bin/ dir

`sudo ln -s /var/lib/flatpak/exports/bin/com.google.Chrome /usr/bin/`
