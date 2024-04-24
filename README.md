# Digital Image Processing Elementary Methods

This repository contains implementations of elementary digital image processing methods in Python. These methods are implemented to handle both RGB and grayscale images and are accompanied by example images demonstrating the effect of each manipulation clearly.

## Table of Contents

- [Introduction](#introduction)
- [Implemented Methods](#implemented-methods)
- [Usage](#usage)
- [Examples](#examples)
- [Streamlit App](#streamlit-app)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Digital image processing is a fundamental aspect of computer vision and image analysis. It involves various techniques to manipulate and enhance digital images for better interpretation and analysis. This repository provides Python implementations of several elementary digital image processing methods, along with example images to illustrate their effects.

## Implemented Methods

1. **Image Negative**: Inverts the colors of an image, effectively turning light areas dark and vice versa.
2. **Gamma Correction**: Adjusts the overall brightness of an image without losing the integrity of its original contrast.
3. **Logarithmic Transformation**: Expands the values in darker regions while compressing the higher intensity values.
4. **Contrast Stretching**: Improves the contrast in an image by stretching the range of intensity values.
5. **Histogram Equalization**: Enhances the contrast of an image by modifying the intensity distribution of the histogram.
6. **Intensity Level Slicing**: Highlights a specific range of intensities in an image while dimming others.
7. **Bit Plane Slicing**: Decomposes an image into its binary bit planes, highlighting the contribution of specific bits to the total image appearance.

## Usage

To use the implemented methods, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/Digital-Image-Processing-Elementary-Methods.git
   ```

2. Install the required dependencies listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Python scripts to apply the desired image processing methods to your images.

## Examples

Below are some example images demonstrating the effect of each implemented method:

- **Image Negative**:

  ![Image Negative Example](https://github.com/birehan/Digital-Image-Processing-Elementary-Methods/blob/main/images/neg.png)

- **Gamma Correction**:

  ![Gamma Correction Example](https://github.com/birehan/Digital-Image-Processing-Elementary-Methods/blob/main/images/gama.png)

- **Logarithmic Transformation**:

  ![Logarithmic Transformation Example](https://github.com/birehan/Digital-Image-Processing-Elementary-Methods/blob/main/images/log.png)

- **Contrast Stretching**:

  ![Contrast Stretching Example](https://github.com/birehan/Digital-Image-Processing-Elementary-Methods/blob/main/images/contrast_stretching.png)

- **Histogram Equalization**:

  ![Histogram Equalization Example](https://github.com/birehan/Digital-Image-Processing-Elementary-Methods/blob/main/images/hist.png)

- **Intensity Level Slicing**:

  ![Intensity Level Slicing Example](https://github.com/birehan/Digital-Image-Processing-Elementary-Methods/blob/main/images/intensity.png)

- **Bit Plane Slicing**:

  ![Bit Plane Slicing Example](https://github.com/birehan/Digital-Image-Processing-Elementary-Methods/blob/main/images/bit_plane_slicing.png)

## Streamlit App

You can also visualize the effects of these methods using a Streamlit web application. To run the Streamlit app, follow these steps:

1. Navigate to the repository folder on your local machine.

2. Run the Streamlit app script using the following command:

   ```bash
   streamlit run streamlit_app.py
   ```

3. Access the app in your web browser by navigating to the URL displayed in the terminal.

4. Upload an image, select a processing method, and click on the "Process Image" button to see the results.

## Contributing

Contributions to this repository are welcome! If you have any ideas for improvement or additional methods to implement, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to customize this template as needed for your specific repository. You can also add more details or sections as you see fit. Happy coding!