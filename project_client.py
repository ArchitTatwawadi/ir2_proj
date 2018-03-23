import requests
import json
import cv2

cam = cv2.VideoCapture(0)
while True:
    ret, im =cam.read()
    url = "192.168.1.4:5000/data"
    payload = {'the_file':im}
    r = requests.post(url, data=payload)
    if r.text['Name'] ==None:
        pass
    else:
        if r.text['Name'] == "<Insert name and motion>"
        ##Enter code for setting motor positions
        
