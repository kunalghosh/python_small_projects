import os
import argparse
import logging
from PIL import Image
import time


def save_cropped_images(image,crop_rectangle,directory,imageName):
    # If the image is GrayScale then cropped portions which lie outside the original
    # image get filled with black.
    # And if the image is RGBA then the portion is colored white.
    cropped_image = image.crop(crop_rectangle)

    # The below show() is very irritating, would ope a lot of windows :P
    #cropped_image.show()

    #croppedFileName = directory + os.path.sep + imageName + "_" + str(int(time.time()*1000000)) + ".png"
    croppedFileName = directory + os.path.sep + imageName + "_" + "_".join(str(element) for element in crop_rectangle) + ".png"
    logging.debug(croppedFileName)
    print("."),
    cropped_image.save(croppedFileName)

if __name__ == "__main__":
    CROP_WIDTH = 20
    CROP_HEIGHT = 20

    parser = argparse.ArgumentParser()
    parser.add_argument("imagePath",help="The Complete Path to the Image file.")
    parser.add_argument("width",help="The Width of the cropped image. Default value = "+str(CROP_WIDTH)+"px.",default=CROP_WIDTH,type=int)
    parser.add_argument("height",help="The Height of the cropped image. Default value = "+str(CROP_HEIGHT)+"px.",default=CROP_HEIGHT,type=int)
    parser.add_argument("widthStep",help="The Step size while translating the cropping window width wise. Default value = "+str(CROP_WIDTH/2)+"px.",default=CROP_WIDTH/2,type=int)
    parser.add_argument("heightStep",help="The Step size while translating the cropping window height wise. Default value = "+str(CROP_HEIGHT/2)+"px.",default=CROP_HEIGHT/2,type=int)
    parser.add_argument("--loglevel",help="The Debug level",default="CRITICAL")
    parser.add_argument("-g", "--grayscale", action="store_true", help="Convert The Image to a GrayScale Image.")

    args = parser.parse_args()

    # populate CROP_WIDTH and CROP_HEIGHT from commandline arguments
    CROP_WIDTH = args.width
    CROP_HEIGHT = args.height

    # Create the directory where the cropped images would be stored
    DIRECTORY = os.path.abspath(os.path.curdir) + os.path.sep + str(CROP_WIDTH) + "_" + str(CROP_WIDTH)
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)

    # assuming loglevel is bound to the string value obtained from the
    # command line argument. Convert to upper case to allow the user to
    # specify --log=DEBUG or --log=debug
    try :
        numeric_level = getattr(logging, args.loglevel.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError('Invalid log level: %s . Choices = DEBUG, ERROR, FATAL, CRITICAL' % args.loglevel)
    except ValueError, e:
        logging.critical(str(e))

    logging.basicConfig(level=numeric_level)

    # Debug log to show what were the arguments passed by the user.
    logging.debug(args)

    # open the Image provided by the user.
    if args.grayscale:
        im = Image.open(args.imagePath).convert('L')
    else:
        im = Image.open(args.imagePath)
    
    # Use the below statement to view the image being processed.
    if args.loglevel.upper() == "DEBUG":
        im.show()
    
    IMAGE_NAME = os.path.basename(args.imagePath).replace(".","_")

    IMAGE_WIDTH, IMAGE_HEIGHT = im.size
    # Go over the image and save the sub images in a subfolder whose
    # name is the dimention of the cropped sub-Image. i.e. CROPWIDTH_CROPHEIGHT
    logging.debug("CROP_WIDTH :"+ str(CROP_WIDTH)+\
            " CROP_HEIGHT :"+ str(CROP_HEIGHT)+\
            " IMAGE_NAME :"+ str(IMAGE_NAME)+\
            " DIRECTORY :"+ str(DIRECTORY)+\
            " IMAGE_WIDTH :"+ str(IMAGE_WIDTH)+\
            " IMAGE_HEIGHT :"+ str(IMAGE_HEIGHT))

    for topLeftPixWidthWise in range(0,IMAGE_WIDTH,args.widthStep):
        for topLeftPixHeightWise in range(0,IMAGE_HEIGHT,args.heightStep):
           crop_rectangle = (topLeftPixWidthWise, topLeftPixHeightWise, topLeftPixWidthWise + CROP_WIDTH, topLeftPixHeightWise + CROP_HEIGHT) 
           logging.debug("Cropping :" + str(topLeftPixWidthWise) + " : " + str(topLeftPixHeightWise))
           save_cropped_images(im, crop_rectangle, DIRECTORY, IMAGE_NAME)

    print("Completed.")
       
