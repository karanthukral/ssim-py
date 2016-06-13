# Imports
from PIL import Image
import numpy
import ImageOps
import requests
import yaml
from StringIO import StringIO

import ssim

'''
Get 2D matrix from an image file, possibly displayed with matplotlib
@param path: Image file path on HD
@return A 2D matrix
'''
def build_mat_from_grayscale_image(img):
    img=ImageOps.grayscale(img)
    imgData=img.getdata()
    imgTab=numpy.array(imgData)
    w,h=img.size
    imgMat=numpy.reshape(imgTab,(h,w))

    return imgMat

with open("config.yml", 'r') as stream:
    try:
        config = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)
print(config)
response = requests.get(config['image_1'])
img1 = Image.open(StringIO(response.content))
response = requests.get(config['image_2'])
img2 = Image.open(StringIO(response.content))

imgMat1 = build_mat_from_grayscale_image(img1)
imgMat2 = build_mat_from_grayscale_image(img2)

SSIMIndex = ssim.compute_ssim(imgMat1, imgMat2)
print "SSIM = ", SSIMIndex
