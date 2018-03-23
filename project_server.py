from flask import Flask
from flask import request
from io import BytesIO
import json
from PIL import image
import cv2
import Dataset_recognizer

app = Flask(__name__)

@app.route('/data')
def data_req():
    error = None
    if request.method == 'POST':
        f = request.form['the_file']
        name = Dataset_recognizer.face_recognizer(f)
    return json.dumps({'Name':name})

if __name__ == '__main__':
      app.run(host='192.168.1.4', port=5000)
