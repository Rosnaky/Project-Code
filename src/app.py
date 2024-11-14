from flask import *
from fileinput import filename
import os
from dotenv import load_dotenv
from threading import Thread
import time

# import custom modules
import screenshot
import imageProcessing

# Variables
MAX_ELAPSED_TIME = 10
CODE_IMAGES_DIR_PATH = os.getenv("IMAGES_DIR_PATH")

load_dotenv()
FILE_UPLOAD_DIR = os.getenv("FILE_UPLOAD_DIR_PATH")

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")


@app.route("/success", methods = ["POST"])
def success():
    if request.method == "POST":
        f = request.files["file"]
        f.save(os.path.join(FILE_UPLOAD_DIR, f.filename))

        time.sleep(5)

        redirect("/code")

        return render_template("fileUploadSuccess.html", filename=f.filename)


@app.route("/code", methods=["POST"])
def code():
    if request.method == "POST":
        f = request.files["file"]

        # Create thread to get images
        get_images_thread = Thread(target = screenshot.getScreenshots(
            MAX_ELAPSED_TIME=MAX_ELAPSED_TIME, code_file_path=FILE_UPLOAD_DIR, 
            images_dir_path=CODE_IMAGES_DIR_PATH))
        
        get_images_thread.start()



if (__name__ == "__main__"):
    
    # remove all images in images dir
    imageProcessing.pruneImageDir(CODE_IMAGES_DIR_PATH)

    app.run(host="0.0.0.0", port=8000)