from skimage import color
from scipy import misc
from skimage.transform import pyramid_reduce
import numpy as np
import pdb

stride = (10,10)
img_path = './img2_crop.jpg'
window_size = (120,100)#heuristically chosen for this image


img = color.rgb2gray(misc.imread(img_path))
h,w = img.shape

delta_x,delta_y = stride

x_list = range(0,w-window_size[1]+1,delta_x)
y_list = range(0,h-window_size[0]+1,delta_y)


lis=[]
for w in x_list:
    for h in y_list:
        #downscale value also heurestically chosen
        im = pyramid_reduce(img[h:h+window_size[0],w:w+window_size[1]],downscale=5)
        lis.append( np.array(im[2:21,:19] * 255, dtype = np.uint8) )

import pickle
pickle.dump( lis, open( "test-windows.pkl", "wb" ) )
#lis = pickle.load( open( "test-windows.pkl", "rb" ) )


##Finding-windows
k = len(lis)/10 #no of chunks, jobs
iterator = range(0,len(lis)-k,k)
from joblib import Parallel, delayed
from parr_test import myfunc

pdb.set_trace()
results = Parallel(n_jobs=-1)(delayed(myfunc)(lis[i:i+k]) for i in iterator)


if len(lis[iterator[-1]+k:]) >= 2:
    results.append(myfunc(lis[iterator[-1]+k:]))

detects = np.concatenate(results)

##Plotting result
windows=[]
for w in x_list:
    for h in y_list:
        windows.append((h,w))

ind = np.where(detects==1)[0]

ws1=[]
for i in ind:
    ws1.append(windows[i])

#http://www.nafisahmad.com/2014/10/how-to-draw-rectangle-with-more-then.html
from PIL import Image, ImageDraw
pil_img = Image.open(img_path)
dr = ImageDraw.Draw(pil_img)
for h,w in ws1:
    cor = (w,h,w+window_size[1],h+window_size[0])
    dr.rectangle(cor, outline="red")

pil_img.save('final.png')