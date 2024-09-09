import os
from pyshortcuts import make_shortcut

# Path to your Python script
script_path = os.path.abspath('main.py')

# Path to your icon file (optional)
icon_path = os.path.abspath('converter.ico')

# Create a shortcut on the desktop
make_shortcut(script_path, name='K8s Secret Converter', icon=icon_path)

print("Shortcut created on the desktop.")
