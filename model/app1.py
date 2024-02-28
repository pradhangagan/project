from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def upload_form():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def upload_image():
    # Get the uploaded image file
    image_file = request.files["image"]

    # Prepare data for the POST request
    files = {"image": (image_file.filename, image_file.read())}

    # Send the POST request to the FastAPI endpoint
    response = requests.post("http://127.0.0.1:8000/upload-image", files=files)

    # Display the response on the web page
    return render_template("index.html", message=response.json()["message"])