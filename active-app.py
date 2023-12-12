#!/usr/bin/env python
import gi
import time
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck, Gtk  # Import the Gtk module

previous_app = None

def on_active_window_changed(screen, previously_active_window):
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
			print(f"Active App Title: {app_title}")

	previous_app = active_app


def main():
	screen = Wnck.Screen.get_default()
	screen.connect('active-window-changed', on_active_window_changed)

	# Initialize Gtk and run the main loop
	Gtk.init([])
	screen.force_update()  # Ensure initial state is captured
	Gtk.main()

if __name__ == "__main__":
	main()
