import os
import time
import markdown
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MarkdownHandler(FileSystemEventHandler):
    def __init__(self, markdown_file, html_file):
        self.markdown_file = markdown_file
        self.html_file = html_file

    def on_modified(self, event):
        if event.src_path == self.markdown_file:
            with open(self.markdown_file, 'r') as file:
                markdown_content = file.read()
                html_content = markdown.markdown(markdown_content)
                with open(self.html_file, 'w') as html_file:
                    html_file.write(html_content)
            print(f"Updated HTML content in {self.html_file}")


class FileWatcher:
    def __init__(self, markdown_file, html_file):
        self.observer = Observer()
        self.markdown_file = markdown_file
        self.html_file = html_file

    def start(self):
        event_handler = MarkdownHandler(self.markdown_file, self.html_file)
        self.observer.schedule(event_handler, path=os.path.dirname(self.markdown_file), recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()
