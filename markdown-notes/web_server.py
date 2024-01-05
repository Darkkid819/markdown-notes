from flask import Flask, render_template_string
import threading
import config

app = Flask(__name__)


@app.route('/')
def index():
    try:
        with open(config.HTML_FILE, 'r') as file:
            html_content = file.read()
        return render_template_string(html_content)
    except FileNotFoundError:
        return "<p>HTML content not available yet.</p>"


def run_server():
    app.run(debug=True, use_reloader=False)


def start_web_server():
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()
