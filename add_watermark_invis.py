import cv2
from imwatermark import WatermarkEncoder, WatermarkDecoder
import numpy as np

def add_invis(img,secret_key):
    nparr = np.frombuffer(img.read(), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    encoder = WatermarkEncoder()
    encoder.set_watermark('bytes', secret_key.encode('utf-8'))
    watermarked = encoder.encode(img, 'dwtDct')
    return watermarked
    
def search_invis(img,secret_key):
    decoder = WatermarkDecoder('bytes', len(secret_key))
    wm = decoder.decode(img, 'dwtDct')
    return wm

