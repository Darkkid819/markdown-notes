import os

current_dir = os.path.dirname(os.path.abspath(__file__))

MARKDOWN_FILE = os.path.join(current_dir, "assets", "notes.md")
HTML_FILE = os.path.join(current_dir, "assets", "notes.html")
EXPORTED_HTML_FILE = os.path.join(os.path.expanduser("~"), "notes.html")
