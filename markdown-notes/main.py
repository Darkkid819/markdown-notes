import sys
import webbrowser
import subprocess
import os
import threading
from file_watcher import FileWatcher
from web_server import start_web_server
import config


def open_default_editor(file_path):
    if sys.platform == "win32":
        os.startfile(file_path)
    elif sys.platform == "darwin":
        subprocess.call(("open", file_path))
    else:  # Assume Unix/Linux
        subprocess.call(("xdg-open", file_path))


def command_listener():
    while True:
        command = input("Enter 'export [optional_path]' to export HTML, or 'quit' to exit: ")
        cmd_parts = command.split(maxsplit=1)
        action = cmd_parts[0]

        if action == 'export':
            export_path = cmd_parts[1] if len(cmd_parts) > 1 else config.EXPORTED_HTML_FILE
            with open(export_path, 'w') as file:
                file.write(open(config.HTML_FILE).read())
            print(f"Exported HTML to {export_path}")
        elif action == 'quit':
            os._exit(0)


def main():
    open_default_editor(config.MARKDOWN_FILE)

    threading.Thread(target=start_web_server, daemon=True).start()

    webbrowser.open_new("http://127.0.0.1:5000/")

    watcher_thread = threading.Thread(target=lambda: FileWatcher(config.MARKDOWN_FILE, config.HTML_FILE).start(),
                                      daemon=True)
    watcher_thread.start()

    command_listener()


if __name__ == "__main__":
    main()
