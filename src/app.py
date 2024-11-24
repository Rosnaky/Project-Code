import os
os.system("export DISPLAY=:1")

from flask import *
from fileinput import filename
from dotenv import load_dotenv
from threading import Thread
import time
import imageDisplay

# import custom modules
import screenshot
import imageProcessing
import buffer
import keyboard


# Variables
load_dotenv()

buffer = buffer.Buffer()
MAX_ELAPSED_TIME = 1
RELATIVE_CODE_IMAGES_DIR_PATH = os.getenv("IMAGES_DIR_RELATIVE_PATH")
CODE_IMAGES_DIR_PATH = os.getenv("IMAGES_DIR_PATH")
FILE_UPLOAD_DIR = os.getenv("FILE_UPLOAD_DIR_PATH")
STATIC_DIR_PATH = os.getenv("STATIC_DIR_PATH")

# end Variables

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")


@app.route("/success", methods = ["POST"])
def success():
    if request.method == "POST":
        # remove all images in images dir
        imageProcessing.pruneDir(CODE_IMAGES_DIR_PATH)
        
        f = request.files["file"]
        f.save(os.path.join(FILE_UPLOAD_DIR, f.filename))
        
        file_path = os.path.join(FILE_UPLOAD_DIR, f.filename)
        def screenshot_task():
            screenshot.getScreenshots(
                MAX_ELAPSED_TIME=MAX_ELAPSED_TIME,
                code_file_path=file_path,
                images_dir_path=CODE_IMAGES_DIR_PATH,
                buffer=buffer
            )
        global screenshot_thread
        screenshot_thread = Thread(target=screenshot_task)
        screenshot_thread.start()
        
        return render_template("fileUploadSuccess.html", filename=f.filename)


@app.route("/code/<filename>/<imageIndex>")
def code(filename, imageIndex):
    
    imageIndex = int(imageIndex)
    imageIndex = imageProcessing.validateImageIndex(CODE_IMAGES_DIR_PATH, imageIndex)
    image_path = os.path.join(STATIC_DIR_PATH, f"codeImages_pic_{imageIndex}.png")
    
    def open_image():
        os.system("sudo pkill display")
        time.sleep(0.1)
        imageDisplay.open_image(image_path=image_path, buffer=buffer)
    
    if len(os.listdir(CODE_IMAGES_DIR_PATH)) > 0:
        global open_image_thread
        open_image_thread = Thread(target=open_image)
        open_image_thread.start()
        # open_image(image_path)

    return render_template("code.html", filename=filename, imageIndex=imageIndex, maxIndex=len(os.listdir(CODE_IMAGES_DIR_PATH)),
                        #    filepath=os.path.join("/utils/codeImages", filename)
                        )



if (__name__ == "__main__"):
    
    #* enable on prod
    #os.system("sudo pkill code")

    # open blank image
    # async def open_initial_image():
    #     await imageDisplay.open_image(os.path.join(STATIC_DIR_PATH, "initial-image.png"))
    # open_initial_image()

    imageDisplay.open_image(os.path.join(STATIC_DIR_PATH, "initial-image.png"), buffer)
    
    port = 8000
    # app.run(host="0.0.0.0", port=port)

    while 1:
        try: 
            app.run(host="0.0.0.0", port=port)
        except:
            port += 1
            continue
        break
