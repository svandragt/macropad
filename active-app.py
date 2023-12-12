#!/usr/bin/env python
import gi
import time
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck, Gtk  # Import the Gtk module

Wnck.Screen.get_default()

last_app = None
while True:
	# Initialize Wnck and GTK
	while Gtk.events_pending():
		Gtk.main_iteration()

	# Get the active window
	screen = Wnck.Screen.get_default()
	screen.force_update()
	#  TODO Wnck.Screen.signals.active_window_changed(screen, previously_active_window)¶
	active_window = screen.get_active_window()


	# Get the window title
	if not active_window:
		active_app = None
		print("No active window found.")
	else:
		active_app = active_window.get_application()
 
		if active_app != last_app:
			app_title = active_app.get_name()
			for sep in [' - ', '.']:
				if sep in app_title:
					app_title = app_title.split(sep)[-1]
			print(f"Active App Title: {app_title}")

	last_app = active_app
	time.sleep(1)
