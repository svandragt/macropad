#!/usr/bin/env python
from gi.repository import Wnck, Gtk
import gi

gi.require_version('Wnck', '3.0')
previous_app = None


def on_active_window_changed(screen):
    """
    :param screen: The screen on which the active window has changed
    :return: None
    """
    global previous_app
    # Initialize Wnck and GTK
    while Gtk.events_pending():
        Gtk.main_iteration()
    screen.force_update()

    active_window = screen.get_active_window()
    if not active_window:
        return
    else:
        active_app = active_window.get_application()
        if active_app != previous_app:
            app_title = active_app.get_name()
            for sep in [' - ', '.']:
                if sep in app_title:
                    app_title = app_title.split(sep)[-1]
            app_title = app_title.title()
            if app_title.strip() == '':
                print(f"Empty title for : {active_app.get_pid()}")
            print(f"Active App Title: '{app_title}'")
            print(active_app.get_pid())

    previous_app = active_app


def main():
    """
    Connects to the default Wnck.Screen, sets up a callback function for the 'active-window-changed' signal,
    initializes Gtk, captures the initial state of the screen, and starts the Gtk main loop.

    :return: None
    """
    screen = gi.repository.Wnck.Screen.get_default()
    screen.connect('active-window-changed', on_active_window_changed)
    # Initialize Gtk and run the main loop
    Gtk.init()
    screen.force_update()  # Ensure initial state is captured
    Gtk.main()


if __name__ == "__main__":
    main()
