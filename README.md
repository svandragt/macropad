# Tool listing
## `active-app.py`

Uses Wnck's active-window-changed' event to detect and format the active app. The goal here is to auto switch to an application specific page on the macropad.

```shell
$ poetry install
$ poetry run ./active-app.py
Active App Title: Terminal
Active App Title: Firefox
Active App Title: Terminal
```

### Known issues

1. IntelliJ editors do not broadcast their application name, and their window name does not include the application either. Via the `Wnck.Application.get_pid()` and filtering `ps -p 94452 l | grep idea.platform.prefix=` it should be possible to get the name.

# Others


The tools have been tested with ElementaryOS and might work on other GTK based Linux desktops.
