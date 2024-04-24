import inspect
import streamlit as st
from PIL import Image
import io
import matplotlib.pyplot as plt

# Import image processing functions
from image_processing import (image_negative, gamma_correction, logarithmic_transformation,
                              contrast_stretching, histogram_equalization,
                              intensity_level_slicing, bit_plane_slicing)

def load_image(image_file):
    """Load the uploaded image file."""
    image = Image.open(io.BytesIO(image_file.read()))
    return image

def show_images(images, titles, cmap=None):
    fig, axes = plt.subplots(1, len(images), figsize=(20, 10))
    if len(images) == 1:
        axes = [axes]  # Make it iterable if only one image
    for ax, image, title in zip(axes, images, titles):
        ax.imshow(image, cmap=cmap)
        ax.title.set_text(title)
        ax.axis('off')
    return fig

def display_images(original, processed, process_name):
    """Display the original and processed images."""
    col1, col2 = st.columns(2)  # Creates two columns
    with col1:
        st.image(original, caption='Original Image', use_column_width=True)
    with col2:
        st.image(processed, caption=f'{process_name} Image', use_column_width=True)

# Streamlit UI
st.title('Image Processing Techniques')

# Processing method selection in the sidebar using radio buttons
process_choice = st.sidebar.radio("Select Processing Method", 
                                  ["Image Negative", "Gamma Correction", "Logarithmic Transformation",
                                   "Contrast Stretching", "Histogram Equalization",
                                   "Intensity Level Slicing", "Bit Plane Slicing"])

# Display description and code toggle for each processing technique
description = {
    "Image Negative": "This process inverts all the colors of an image. Each pixel's value is subtracted from the maximum intensity value, effectively turning light areas dark and vice versa, which can be useful for enhancing hidden details or for certain artistic effects.",
    "Gamma Correction": "Adjusts the overall brightness of an image without losing the integrity of its original contrast. By applying a non-linear transformation to the intensity, it can correct exposure problems in images that are too dark or too bright. The gamma value dictates the level of correction applied.",
    "Logarithmic Transformation": "This method is used to expand the values in darker regions while compressing the higher intensity values. The transformation uses the logarithm of pixel values, which enhances details hidden in shadows and is particularly effective in brightening up underexposed images.",
    "Contrast Stretching": "Also known as normalization, this technique improves the contrast in an image by stretching the range of intensity values it contains to span a desired range of values. It makes the darkest pixels darker and the brightest pixels brighter, which can help in improving the visual quality of an image that has dull colors.",
    "Histogram Equalization": "Aims to enhance the contrast of an image by modifying the intensity distribution of the histogram. This method redistributes the most frequent intensity values across the available range, which generally increases the global contrast of images, especially when the usable data of the image is represented by close contrast values.",
    "Intensity Level Slicing": "Highlights a specific range of intensities in an image while dimming others. This technique can be used to focus on objects or regions of particular interest by enhancing specific intensity bands, making it useful in both artistic and practical applications such as medical imaging.",
    "Bit Plane Slicing": "This technique decomposes an image into its binary bit planes, highlighting the contribution of specific bits to the total image appearance. It can be used for image compression and analysis, allowing us to see the importance of each bit in the context of the image's overall visual quality."
}


# Define processing methods
process_methods = {
    "Image Negative": image_negative,
    "Gamma Correction": gamma_correction,
    "Logarithmic Transformation": logarithmic_transformation,
    "Contrast Stretching": contrast_stretching,
    "Histogram Equalization": histogram_equalization,
    "Intensity Level Slicing": intensity_level_slicing,
    "Bit Plane Slicing": bit_plane_slicing
}



expander = st.expander(f"{process_choice} Description and Code")
with expander:
    st.write(description[process_choice])
    st.code(f"# Example processing code for {process_choice}\n {inspect.getsource(process_methods[process_choice])}")

# Configure sidebar parameters based on processing choice
if process_choice == "Gamma Correction":
    gamma = st.sidebar.slider("Gamma", 0.1, 5.0, 1.0)
elif process_choice == "Contrast Stretching":
    low, high = st.sidebar.slider("Percentiles for Stretching", 0, 100, (2, 98), step=1)
elif process_choice == "Intensity Level Slicing":
    low = st.sidebar.number_input("Low Intensity", min_value=0, max_value=255, value=100)
    high = st.sidebar.number_input("High Intensity", min_value=0, max_value=255, value=200)
elif process_choice == "Bit Plane Slicing":
    plane = st.sidebar.slider("Bit Plane", 0, 7, 0)

# Upload image in the main area
uploaded_file = st.file_uploader("Upload an Image", type=['png', 'jpg', 'jpeg'], key="uploader")

if uploaded_file is not None:
    image = load_image(uploaded_file)
    # Process based on selection
    if process_choice == "Image Negative":
        processed_image = image_negative(image)
    elif process_choice == "Gamma Correction":
        processed_image = gamma_correction(image, gamma)
    elif process_choice == "Logarithmic Transformation":
        processed_image = logarithmic_transformation(image)
    elif process_choice == "Contrast Stretching":
        processed_image = contrast_stretching(image, low, high)
    elif process_choice == "Histogram Equalization":
        processed_image = histogram_equalization(image)
    elif process_choice == "Intensity Level Slicing":
        processed_image = intensity_level_slicing(image, low, high)
    elif process_choice == "Bit Plane Slicing":
        processed_image = bit_plane_slicing(image, plane)

    # Display results
    display_images(image, processed_image, process_choice)
