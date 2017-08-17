from keras.models import load_model
from PIL import Image
from keras.optimizers import RMSprop, Adam, Adagrad
import os
import numpy as np

model = load_model('model.h5')

# Define the below parameters same as when model trained
model.compile(loss='categorical_crossentropy', optimizer='RMSprop', metrics=["accuracy"])
img_width = 120
img_height = 30
img_channels = 1

print (model.summary())

test_dir = '.././Testing/'
files = os.listdir(test_dir)

for file in files:
    im = Image.open(test_dir+file)
    img = np.array(im.resize((img_width, img_height)))
    try:
        img = (img.flatten()).reshape(1, img_width, img_height, img_channels)
        img /= 255
        pred = model.predict(img, verbose=1)
        print pred
    except Exception as e:
        print file
        print e
