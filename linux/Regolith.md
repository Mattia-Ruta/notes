When installing Regolith, there seems to be a couple of initial issues..

Pipewire fix

`sudo touch /usr/share/pipewire/media-session.d/with-pulseaudio`

Bluetooth fix

`sudo rfkill unblock bluetooth`

Then restart bluetooth server

`sudo systemctl stop bluetooth`

`sudo systemctl restart bluetooth`
