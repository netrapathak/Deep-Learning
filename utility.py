from __future__ import absolute_import
from __future__ import print_function
from PIL import Image
import numpy as np
import pickle
import string
import csv
import sys
import urllib
import scipy
import pandas
import os
# import cv2
# from sklearn.utils import shuffle
# from sklearn.preprocessing import Normalizer # Normalize data (length of 1)


def downloadImage(imgUrl,imgPath):
    os.system("wget -O " + imgPath + " " + imgUrl)


def writeToCsv(filePath,csvData):

    # csvData: list; filepath: without extension
    with open(filePath+".csv", 'a') as csvfile:
       spamwriter = csv.writer(csvfile, delimiter=',',
                                quoting=csv.QUOTE_MINIMAL)
       spamwriter.writerow(csvData)
       csvfile.flush()
       
 
