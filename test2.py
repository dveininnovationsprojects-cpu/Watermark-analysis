import tensorflow as tf
import cv2
import numpy as np
from keras.models import load_model
from invisible_watermark_detext import invis_test

model = load_model("model.keras")
model.compile()

def predict(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = np.array(img,dtype=np.float32) / 255.0 #use dtype=np.uint8 for model2.keras and remove /255.0
    
    x,y=invis_test(img)
    img = cv2.resize(img,(128,128))
    img = np.expand_dims(img, axis=0)
    li=[x,y]
    k=np.array(li,dtype=np.float32)
    print(k[0])
    
    li=np.expand_dims(k,axis=0)
    prob = model.predict([img,li])[0][0]
    print(li)
    print(prob)

    return prob
#f=open(r"D:\ai-generated-abstract-water-bubbles-colorful-background-design-images-photo.webp",'rb')
#nparr = np.frombuffer(f.read(), np.uint8)
#img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#print(predict(img))
