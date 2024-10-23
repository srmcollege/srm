
from PIL import Image,ImageChops,ImageFilter
import matplotlib.image as image
import matplotlib.pyplot as plt
import numpy as np
#Image 1
x=Image.open(r'C:\Linear Algebra\face.jpg')
#Image 2
y = Image.open('C:\Linear Algebra\face2.jpg')


#Multiplication.
from PIL import Image,ImageChops,ImageFilter
import matplotlib.image as image
import matplotlib.pyplot as plt
import numpy as np
#Image 1
x=Image.open(r'C:\Linear Algebra\face.jpg')
#Image 2
y = Image.open('C:\Linear Algebra\face2.jpg')
#Multiplication of Images
multi=ImageChops.multiply(x,y)
multi.show()



#Addition.
from PIL import Image,ImageChops,ImageFilter
import matplotlib.image as image
import matplotlib.pyplot as plt
import numpy as np
#Image 1
x=Image.open(r'C:\Linear Algebra\face.jpg')
#Image 2
y = Image.open('C:\Linear Algebra\face2.jpg')
#Additon of Images
add=ImageChops.add(x,y)
add.show()



#Subtraction.
from PIL import Image,ImageChops,ImageFilter
import matplotlib.image as image
import matplotlib.pyplot as plt
import numpy as np
#Image 1
x=Image.open(r'C:\Linear Algebra\face.jpg')
#Image 2
y = Image.open('C:\Linear Algebra\face2.jpg')
#Subtraction of Images
subtract=ImageChops.subtract(x,y)
subtract.show()


#Resize.
p=x.resize((500,500))
#converting in grey scale
g=x.convert('L')
g.show()

p=y.resize((500,500))
#converting in grey scale
g=y.convert('L')
g.show()



#Inverting Image.
invert=ImageChops.invert(x)
invert.show()
pix=y.load()
for i in range(y.size[0]):
    for j in range(y.size[1]):
        if pix[i,j] != (255) and i<150 and j<120:
            pix[i,j]=(255,255,0)
y.show()

invert=ImageChops.invert(y)
invert.show()
pix=x.load()
for i in range(x.size[0]):
    for j in range(x.size[1]):
        if pix[i,j] != (100,30,70) and i>200 and j>150:
            pix[i,j]=(40,80,70)
x.show()



#Linear Combination of images.
from PIL import Image
import numpy as np
def imresize(img, size):
    im = Image.fromarray(img)
    return np.array(im.resize(size))
# Load images
image1_path = (r'C:\Linear Algebra\face1.jpg')
image1_path.show()
# Load images
image2_path = (r'C:\Linear Algebra\face2.jpg')
image2_path.show()


# Convert images to numpy arrays
i1 = np.array(im11)
i2 = np.array(im12)

# Resize images
u = imresize(i1, (400, 400))
v = imresize(i2, (400, 400))

# Linear combination of images
c = 2
d = 4
a = (c * u) + (d * v)

# Ensure the resulting array is within valid image range and convert to uint8
a = np.clip(a, 0, 255).astype('uint8')

# Create and show the resulting image
linimg = Image.fromarray(a)
linimg.show()




