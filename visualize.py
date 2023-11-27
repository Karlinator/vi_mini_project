import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt

import os
import random

def visualize(image):
    image_str = 'output/' + image + '/' + os.listdir('output/' + image)[0]
    test_load = nib.load(image_str).get_fdata()
    
    fig, axs = plt.subplots(2, 3)
    
    axs[0, 2].imshow(test_load[:,:,80])
    axs[0, 2].set_title('Prediction')
    
    image_lab = 'data/Task01_BrainTumour/labelsTr/'+image+'.nii.gz'
    label = nib.load(image_lab).get_fdata()
    axs[1, 2].imshow(label[:,:,80])
    axs[1, 2].set_title('Label')
    
    image_str = 'data/Task01_BrainTumour/imagesTr/'+image+'.nii.gz'
    test_load = nib.load(image_str).get_fdata()
    
    
    
    test = test_load[:,:,80]
    # plt.imshow(test)
    axs[0, 0].imshow(test[:,:,0])
    axs[0, 0].set_title('Channel 0: T1')
    axs[0, 1].imshow(test[:,:,1])
    axs[0, 1].set_title('Channel 1: T1c')
    axs[1, 0].imshow(test[:,:,2])
    axs[1, 0].set_title('Channel 2: T2')
    axs[1, 1].imshow(test[:,:,3])
    axs[1, 1].set_title('Channel 3: FLAIR')
    plt.show()
    
def visualize_data(image):
    image = 'data/Task01_BrainTumour/imagesTs/'+image+'.nii.gz'
    test_load = nib.load(image).get_fdata()
    
    fig, axs = plt.subplots(2, 2)
    
    print(test_load.min())
    
    test = test_load[:,:,80]
    # plt.imshow(test)
    axs[0, 0].imshow(test[:,:,0])
    axs[0, 0].set_title('Channel 0: T1')
    axs[0, 1].imshow(test[:,:,1])
    axs[0, 1].set_title('Channel 1: T1c')
    axs[1, 0].imshow(test[:,:,2])
    axs[1, 0].set_title('Channel 2: T2')
    axs[1, 1].imshow(test[:,:,3])
    axs[1, 1].set_title('Channel 3: FLAIR')
    plt.show()
    
    
if __name__ == "__main__":
    # image = random.choice(os.listdir('output/'))
    image = 'BRATS_176'
    # visualize_data(image)
    visualize(image)