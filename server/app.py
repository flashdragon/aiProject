from flask import Flask, request, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
from PIL import Image
import base64
from io import BytesIO
import json
import cv2
import itertools
import numpy as np
from time import time
from makelandmark import makelandmark
from rank import recommend
import mediapipe as mp
import matplotlib.pyplot as plt

app = Flask(__name__)
CORS(app)


@app.route('/', methods = ['POST'])
def translateimage():
    f = request.files['file']
    f.save("./dataset/"+secure_filename(f.filename))
    sample_img=cv2.imread("./dataset/"+secure_filename(f.filename))

    l=makelandmark(sample_img)
    
    answer=recommend(l,'./dataset/data')
    print(answer)
    return answer


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=False)