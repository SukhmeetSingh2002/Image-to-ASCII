from PIL import Image
import numpy as np
import argparse

parser=argparse.ArgumentParser()

# adding arguments
parser.add_argument('inputImage',help='Enter the path to image')
parser.add_argument('outputFile',help='Enter the path to output File')
parser.add_argument('-w','--width',help='Enter width of output image default=75',type= int,default=75)
parser.add_argument('-i','--invertColor',help='Flag to invert color of image',action='store_true')
args=parser.parse_args()

# Setting variables
inputImagePath=args.inputImage
outputPath=args.outputFile
widd=args.width

asci = r"@%#*+=-:. " 

if args.invertColor:
    asci = r"@%#*+=-:. "[::-1] 

# opening input image
img = Image.open(inputImagePath)

# setting wid,height of image
wid,height=img.size
img=img.resize((widd,int(widd*((height*9)/(wid*20)))))
wid,height=img.size

def convertGray(img):
    """
    Converting a colored image to gray scale
    """
    imgArrayold=(np.array(img))
    arrayImage = np.zeros([height, wid], dtype=np.uint8)
    for x in range(height):
        for y in range(wid):
            aa=imgArrayold[x,y,0]/3+imgArrayold[x,y,1]/3+imgArrayold[x,y,2]/3
            arrayImage[x,y] = aa
    imgNew = Image.fromarray(arrayImage)
    return imgNew


def avg(imggg):
    return (np.average(np.array(imggg)))

img = convertGray(img)

# opening file
f = open(outputPath, "w")

for j in range(height):
    for i in range(wid):
        img1 = img.crop((i, int(j), i+1, int((j+1))))
        f.write(asci[int((avg(img1)*9)/255)])
        print(asci[int((avg(img1)*9)/255)],end="")
    print("\n",end="")
    f.write("\n")


f.close()
