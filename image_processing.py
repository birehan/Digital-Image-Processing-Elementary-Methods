import numpy as np
from skimage import img_as_float, img_as_ubyte, exposure
from skimage.exposure import rescale_intensity

def image_negative(image):
    """Apply negative transformation to an image."""
    image = np.asarray(image)
    return 255 - image

def gamma_correction(image, gamma=1.0):
    """ Apply gamma correction to an input image."""
    image = img_as_float(image)
    return img_as_ubyte(np.power(image, gamma))

def logarithmic_transformation(image, c=1):
    """Apply logarithmic transformation to enhance dark regions."""
    image = np.array(image, dtype='float32')
    image = c * np.log(1 + image)
    image = 255 * (image - np.min(image)) / (np.max(image) - np.min(image))
    return image.astype(np.uint8)

def contrast_stretching(image, low_percentile, high_percentile):
    """Apply contrast stretching based on percentiles."""
    image = np.asarray(image)
    p2, p98 = np.percentile(image, (low_percentile, high_percentile))
    return img_as_ubyte(rescale_intensity(image, in_range=(p2, p98)))
   
def histogram_equalization(image):
    """Apply histogram equalization to the image."""
    image = np.array(image)
    if len(image.shape) == 2:  # grayscale image
        equalized_img = exposure.equalize_hist(image)
    else:  # RGB image
        channels = [exposure.equalize_hist(channel) for channel in np.rollaxis(image, 2)]
        equalized_img = np.dstack(channels)
    return img_as_ubyte(equalized_img)
 
def intensity_level_slicing(image, low, high):
    """Highlight intensities within a specified range and dim others."""
    image = np.array(image)
    mask = ((image >= low) & (image <= high)).astype(np.uint8)
    return mask * 255

def bit_plane_slicing(image, plane):
    """Slice image to show specific bit plane."""
    image = np.array(image)
    mask = 1 << plane
    sliced_image = np.bitwise_and(image, mask)
    sliced_image = np.where(sliced_image > 0, 255, 0)  # Enhance visibility
    return sliced_image
  
