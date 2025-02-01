## Setup for Laptops

### Firefox - Enable Touch

For Firefox, if touch scrolling doesn't work, you'll need to enable it in advanced configuration:

1. In Firefox, open about:config
1. Set `dom.w3c_touch_events.enabled=1`

You can also add the following line to `/etc/security/pam_env.conf`:

`MOZ_USE_XINPUT2 DEFAULT=1`
