from imwatermark import WatermarkEncoder
from imwatermark import WatermarkDecoder
import cv2 
from io import BytesIO
import numpy as np
import matplotlib.pyplot as plt
import os 

def add_vis(img,text,pos,Font,opacity,size):
    from PIL import Image, ImageDraw, ImageFont
    if Font is None:
        Font='ARIALBD.TTF'
    if pos is None:
        pos='center'
    if opacity is None:
        opacity=30
   
    #Font=os.path.join(r'c:\WINDOWS\Fonts',Font)
    img=Image.open(BytesIO(img.read())).convert('RGBA')
    options2={'small':30,'medium':50,'large':70}
    options={'bold':255,'transparent':100,'invisible':0}
    
    font = ImageFont.truetype(Font,options2[size]) # or use a .ttf font
    txt_layer = Image.new("RGBA", img.size, (255,255,255,0))
    draw = ImageDraw.Draw(txt_layer)
    bbox=draw.textbbox((0,0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = img.width -tw - 10
    y = img.height  -th- 10
    rotated=None
    if pos=='center-right':
        
        draw.text((0,0), text, fill=(255,255,255,options[opacity]), font=font)
        rotated = txt_layer.rotate(90, expand=True)
        print(txt_layer.height,' ',txt_layer.width)
        print(img.height,' ',img.width)
        print(th,' ',tw)
        x=rotated.width+tw-th
        y=th-rotated.height-100
       
        position = (x,y//2)
    elif pos=='center-left':
        draw.text((0,0), text, fill=(255,255,255,options[opacity]), font=font)
        rotated = txt_layer.rotate(90, expand=True)
        print(th,' ',tw)
        y=th-rotated.height-100
        position=(0+10,y//2)
    elif pos=='center-bottom':
        position=(x//2,y)
    elif pos=='center':
        position=(x//2,y//2)
    else:
        position=(x//2,0)
    
    draw.text(position, text, fill=(255,255,255,options[opacity]), font=font)
    if rotated:
        img.paste(rotated,position,rotated)
        img=cv2.cvtColor(np.array(img),cv2.COLOR_RGBA2BGR)
        
    else:
        watermarked = Image.alpha_composite(img, txt_layer)
        watermarked = watermarked.convert("RGBA")
   
        img=cv2.cvtColor(np.array(watermarked),cv2.COLOR_RGBA2BGR)
   
    return img