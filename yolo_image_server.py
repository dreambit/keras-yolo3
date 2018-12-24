import sys
import argparse
from yolo import YOLO, detect_video
from PIL import Image

from flask import Flask
app = Flask(__name__)

yolo = YOLO()

@app.route("/")
def detect_img():
    yolo.detect_image(Image.open('C:\\Users\\r.orlechuk\\Pictures\\2.jpg'))
    return 'YES'

if __name__ == "__main__":
    app.run(threaded=False)