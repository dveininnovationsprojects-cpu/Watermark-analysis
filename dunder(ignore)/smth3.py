import cv2
import matplotlib.pyplot as plt
import numpy as np
from imwatermark import WatermarkEncoder
img=open('test_water.webp','rb')
nparr = np.frombuffer(img.read(), np.uint8)
img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
encoder=WatermarkEncoder()
encoder.set_watermark('bytes', 'secret_key'.encode('utf-8'))
watermarked=encoder.encode(img,'dwtDct')
cv2.imshow('w',watermarked)
plt.show()
cv2.waitKey(0)

img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
cv2.imshow('gray',img)
plt.show()
cv2.waitKey(0)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
plt.show()
cv2.waitKey(0)