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

# Others


The tools have been tested with ElementaryOS and might work on other GTK based Linux desktops.
