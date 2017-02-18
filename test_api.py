import cv2
import numpy as np
import requests
import base64

url ="http://127.0.0.1:8000/KopiSelection/"

#img = cv2.imread('/Users/iampamungkas/Downloads/cherries.jpg',0)

#image = cv2.imread("/Users/iampamungkas/Downloads/cherries.jpg")
payload = {"image": open("/Users/iampamungkas/Downloads/IMG_1582.jpg", "rb")}

#payload = {"path": "/Users/iampamungkas/Downloads/cherries.jpg"}

r = requests.post(url, files=payload).json()

#print "/Users/iampamungkas/Downloads/cherries.jpg: {}".format(r)

img = base64.b64decode(r["image"])
npimg = np.fromstring(img, dtype=np.uint8)
source = cv2.imdecode(npimg,1)

cv2.imshow("Nyoba",source)
cv2.waitKey(0)