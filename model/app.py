from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def upload_form():
    """
    Renders the upload form for the user.
    """
    return render_template("index.html")

@app.route("/", methods=["POST"])
def upload_image():
    """
    Handles image upload, sends it to the FastAPI endpoint for processing,
    and displays the response on the web page.
    """

    try:
        # Get the uploaded image file
        image_file = request.files["image"]

        # Prepare data for the POST request
        files = {"image": (image_file.filename, image_file.read())}

        # Send the POST request to the FastAPI endpoint
        response = requests.post("http://127.0.0.1:8000/objectdetection/", files=files)

        # Check for successful response
        if response.status_code == 200:
            data = response.json()
         
        #     return render_template("index.html", message=data.get("message"), results=data.get("results"))
        # else:
        #     return render_template("index.html", message="Error: Failed to receive response from server.")
            

            # Access detected objects and number of detections
           

            return render_template("index.html", message=data.get("message"), detected_objects=data.get("detected_objects"), num_detections=data.get("num_detections"))
        else:
            return render_template("index.html", message="Error: Failed to receive response from server.")


    except Exception as e:
        print(f"Error handling upload: {e}")
        return render_template("index.html", message="Error: Encountered an error during processing.")
