
from PIL import Image,ImageChops,ImageFilter
import matplotlib.image as image
import matplotlib.pyplot as plt
import numpy as np

#Image 1
x=Image.open(r'C:SYCS\Linear Algebra\face.jpg')
x.show()
#matrix representation
c=np.array(x)
print(c)


#Image 2
y = Image.open(r'C: SYCS\Linear Algebra\face2.jpg')
y.show()
#matrix representation
d=np.array(y)
print(d)


#mode of image
print("size of image:",x.size,"color of image:",x.mode)
#mode of image
print("size of image:",y.size,"color of image:",y.mode)


#rotation
varname = x.rotate(90)
varname.show()
#rotation
varname = y.rotate(90)
varname.show()


#resize
r=x.resize((300,200))
r.show()
#resize
r=y.resize((300,200))
r.show()


#flipping left to right
newflip=x.transpose(Image.FLIP_LEFT_RIGHT)
newflip.show()
#flipping left to right
newflip=y.transpose(Image.FLIP_LEFT_RIGHT)
newflip.show()


#flipping top to bottom
newflip=x.transpose(Image.FLIP_TOP_BOTTOM)
newflip.show()
#flipping top to bottom
newflip=y.transpose(Image.FLIP_TOP_BOTTOM)
newflip.show()

