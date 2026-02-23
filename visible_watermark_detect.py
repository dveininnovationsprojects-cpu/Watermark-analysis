import cv2
import pytesseract
import matplotlib.pyplot as plt



#doesnt work very well, pytesseract is unable to pick up the watermark so cnn is preferred
def check_vis(img):
    import numpy as np
    pytesseract.pytesseract.tesseract_cmd=r'C:/Program Files/Tesseract-OCR/tesseract.exe'
    
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    thresh = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY, 11, 2
    )

    import numpy as np

     # grayscale
    
    edges = cv2.Canny(img, 50, 150)

    edge_density = np.sum(edges > 0) / edges.size
    print("Edge density:", edge_density)   
    text = pytesseract.image_to_string(thresh)
    text2=pytesseract.image_to_string(edges)
    return text,text2
