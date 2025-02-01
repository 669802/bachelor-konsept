from flask import Flask, render_template, request, redirect, url_for
import os
import subprocess

app = Flask(__name__)
UPLOAD_FOLDER = "input"
ALLOWED_EXTENSIONS = {"txt", "csv", "json", "xml"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Sjekk om filtypen er tillatt
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            return "❌ Ingen fil valgt", 400

        file = request.files["file"]
        if file.filename == "":
            return "❌ Ingen fil valgt", 400

        if file and allowed_file(file.filename):
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(file_path)

            # 🟢 Kjør pipelinen etter opplasting
            subprocess.run(["python3", "main_pipeline.py"], check=True)

            return redirect(url_for("upload_success", filename=file.filename))

    return render_template("index.html")

@app.route("/success/<filename>")
def upload_success(filename):
    return f"✅ Filen {filename} er lastet opp og behandlet!"

if __name__ == "__main__":
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True, port=5000)