
import numpy as np
import cv2
from matplotlib import pyplot as plt
import glob, os
import time
from numpy import vstack



file0='nrec0739.tif'
file1="rec0739.tif"
file2="Carcharodon_carcharias_PLJ__rec0739.tif"

img0= cv2.imread(file0,0)
img1= cv2.imread(file1,0)
img2= cv2.imread(file2,0)

imd=np.multiply(img1,img2)

im3=img1-img2
index=np.where(im3>220)
im3[index]=0
index=np.where(im3>2)
im3[index]=255

index=np.where(im3<3)
im3[index]=0
im3=im3/255



im3=np.multiply(im3,img2)
index=np.where(im3!=0)
asd=im3[index]

dx=30
dy=30
x=300
y=510
img2 = cv2.blur(img2,(5,5))
#plt.hist(asd.ravel(),20)
img2=img2[x:x+dx,y:y+dy]
plt.imshow(img2)
plt.show()

plt.hist(img2.ravel(),20)
#plt.imshow(im3)
plt.show()


