from PIL import Image,ImageDraw
import numpy as np
import argparse

parser=argparse.ArgumentParser()

# adding arguments

Mode = parser.add_mutually_exclusive_group(required=True)
Mode.add_argument('--text',action='store_true',help='Output the image made of ascii characters to a text file')
Mode.add_argument('--image',action='store_true',help='Output the coloured image made using custom string to a png file')


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


def convertToAscii(img):
    """
    Write ASCII characters to file
    """
    # opening file
    f = open(outputPath.split('.')[0]+'.txt', "w")

    for j in range(height):
        for i in range(wid):
            img1 = img.crop((i, int(j), i+1, int((j+1))))
            f.write(asci[int((avg(img1)*9)/255)])
            print(asci[int((avg(img1)*9)/255)],end="")
        print("\n",end="")
        f.write("\n")


    f.close()

def writeTextToImage(TextInput,bgColor):
    """
    Make a coloured image of custom string
    """
    imgnew=Image.new(mode="RGB",size=(widd*6,9*int(widd*((height*9)/(wid*20)))),color=bgColor)
    for j in range(int(img.size[1])):
        for i in range(int(img.size[0])):
            img1 = img.crop((i, int(j), i+1, int((j+1))))
            img2=ImageDraw.Draw(imgnew)
            x=img1.getpixel((0,0))
            img2.text((i*6, j*9), TextInput[i%(len(TextInput))] , fill=(x))
    imgnew.save(outputPath.split('.')[0]+'.png')


if args.text:
    wid,height=img.size
    imgg = convertGray(img)
    convertToAscii(imgg)
if args.image:
    bgColor=(0,0,0)
    if args.invertColor:
        bgColor=(255,255,255)
    Text=input("Enter the string you want to see on image : ")
    writeTextToImage(Text,bgColor)