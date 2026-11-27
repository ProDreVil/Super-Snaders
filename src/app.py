from flask import Flask, render_template
from flask import send_from_directory
from pathlib import Path

app = Flask(__name__, template_folder="../web/templates", static_folder="../web/static")

@app.route("/")
def index():
    return render_template("index.html")

ASSET_FOLDER = Path(__file__).resolve().parent.parent / "assets"

@app.route("/assets/<path:filename>")
def serve_assets(filename):
    return send_from_directory(ASSET_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)