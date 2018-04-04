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
import difflib
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
       
def compareFiles(file_1, file_2):   #example:   file_1='file_1.py', file_2='./subdir/file_2.py'
    with open(file_1) as text1:
        with open(file_2) as text2:
            d = difflib.Differ()
            diff = list(d.compare(text1.readlines(), text2.readlines()))
            with open('diff.txt', 'w') as diff_file:
                _diff = ''.join(diff)
                diff_file.write(_diff)
    
#     # The ndiff() function produces essentially the same output
#     with open(file_1='text1.txt') as text1, open(file_2='text2.txt') as text2:
#         diff = difflib.ndiff(text1.readlines(), text2.readlines())
#     with open('diff.txt', 'w') as result:
#         for line in diff: result.write(line)
