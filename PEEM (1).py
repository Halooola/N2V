#!/usr/bin/env python
# coding: utf-8

# # **Noise2Void - 2D Example for PEEM data**
# 

# #**Import necessary libraries**

# In[4]:


# We import all our dependencies.
from n2v.models import N2VConfig, N2V
import numpy as np
from csbdeep.utils import plot_history
from n2v.utils.n2v_utils import manipulate_val_data
from n2v.internals.N2V_DataGenerator import N2V_DataGenerator
from matplotlib import pyplot as plt
from skimage import io
import os
import shutil


# #**convert JPEG images to lossless TIFF format**

# In[11]:


from PIL import Image
import os

# Define the path to the directory containing the JPEG images
jpeg_directory = r'C:\Users\Hala\Desktop\Dataset2'

# Define the output directory for the TIFF images
tiff_directory = r'C:\Users\Hala\Desktop\Dataset2_tiff'

# Check if the output directory exists, if not, create it
if not os.path.exists(tiff_directory):
    os.makedirs(tiff_directory)

# Iterate through JPEG files in the directory
for filename in os.listdir(jpeg_directory):
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.JPG') or filename.endswith('.JPEG'):
        # Open the JPEG image
        jpeg_path = os.path.join(jpeg_directory, filename)
        img = Image.open(jpeg_path)

        # Convert the image to TIFF format
        tiff_path = os.path.join(tiff_directory, os.path.splitext(filename)[0] + '.tif')
        img.save(tiff_path, format='TIFF')

        print(f"Converted {filename} to TIFF format.")

print("Conversion completed.")


# #**Training data preparation**

# In[24]:


# create DataGenerator-object.
datagen = N2V_DataGenerator()


# In[27]:


# Load all the '.tif' files from the tiff_directory, the function will return a list of images (numpy arrays).
imgs = datagen.load_imgs_from_directory(directory = tiff_directory)

# Let's look at the shape of the images.
print(imgs[0].shape,imgs[1].shape)


# #**Configuration**

# In[ ]:





# #**Training**

# In[ ]:




