import imageio.v3 as iio
from PIL import Image
filenames = ['abhay1.jpg','abhay2.jpg']
images = []
for filename in filenames:
    images.append(iio.imread(filename))
iio.imwrite('abhay.gif',images,duration=500,loop=0)
# its also working without resizing 
#import imageio.v3 as iio
 #   filenames = ['abhay1.jpg','abhay2.jpg']
#images = []
#for filename in filenames:
 #   images.append(iio.imread(filename))
#iio.imwrite('abhay.gif',images,duration=500,loop=0)

