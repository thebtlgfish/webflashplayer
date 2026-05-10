from flask import Flask, render_template, request, url_for
import os

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/games")
def index():
    filename = request.args.get("file", "flyguy.swf")
    swf_dir = os.path.join(app.static_folder, "swfs")
    safe_path = os.path.normpath(os.path.join(swf_dir, filename))
    if not safe_path.startswith(os.path.abspath(swf_dir)) or not os.path.isfile(safe_path):
        filename = "flyguy.swf"
    swf_url = url_for('static', filename=f"swfs/{filename}")
    return render_template("player.html", swf_url=swf_url, swf_name=filename)

if __name__ == "__main__":
    app.run()
