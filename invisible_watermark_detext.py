import cv2
import numpy as np
import matplotlib.pyplot as plt 

def invis_test(img):
    
    #frequency domain analysis
    
    if len(img.shape) == 2:  
    # grayscale → make RGB
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

    elif img.shape[2] == 4:  
        # RGBA → RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
        img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    elif img.shape[2] == 3:  
        # BGR → RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    print(np.where(img>0))
    img=np.float32(img)
    dct = cv2.dct(img)
    block = dct[:32, :32]
    energy = np.sum(block**2) / (block.shape[0] * block.shape[1])
    print("DCT energy:", energy)
    mean_energy=38.719982
    std_dev=19.242796*2

    energy_deviation = abs(energy - mean_energy)

    energy_confidence = min(energy_deviation / std_dev,1.0)



    #least significant bit
    
    img=np.uint8(img)
    lsb = img & 1
    unique, counts = np.unique(lsb, return_counts=True)
    print(counts)
    lsb_ratio = counts[0] / (counts[0] + counts[1])  # fraction of 1s

    lsb_bias = abs(lsb_ratio - 0.5)
    print("LSB bias:", lsb_bias)

    return  lsb_bias,energy_confidence

    #good
#invis_test(r'D:\watermark_detect2\africa-animal-big-carnivore-87410.jpeg')