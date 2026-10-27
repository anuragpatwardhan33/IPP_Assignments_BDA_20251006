# Image Processing using Python, Assignment 2

This repository contains Python programs for the Image Processing lab assignments.

## Programs

1. **Program 1 — Read and Display an Image Using OpenCV**  
   Reads `flower.jpg`, prints the image dimensions and data type, and displays the image.

2. **Program 2 — Display Image Dimensions and Data Type**  
   Reads `scene.jpg` and prints its height, width, number of channels, and data type.

3. **Program 3 — Convert a Color Image to Grayscale**  
   Converts `scene.jpg` to grayscale and saves the result as `output_gray.jpg`.

4. **Program 4 — Display an Image Using Pillow**  
   Opens and displays `sunset.png` using Pillow and Matplotlib.

5. **Program 5 — Resize an Image to 50%**  
   Resizes `scene.jpg` to half its original width and height and displays both images.

6. **Program 6 — Crop the Center 200 × 200 Pixels**  
   Crops a 200 × 200 region from the center of `scene.jpg` and displays the cropped image.

7. **Program 7 — Rotate an Image 90° Clockwise**  
   Rotates `scene.jpg` 90 degrees clockwise and displays the result.

8. **Program 8 — Flip an Image Horizontally**  
   Flips `car.jpg` from left to right and displays the original and flipped images.

9. **Program 9 — Convert an Image to HSV**  
   Converts `scene.jpg` to HSV and displays the Hue, Saturation, and Value channels.

10. **Program 10 — Calculate Mean Squared Error (MSE)**  
    Converts `img1.jpg` and `img2.jpg` to grayscale and calculates the MSE between them. Both images must have the same dimensions.

## Requirements

- Python 3
- OpenCV
- Matplotlib
- NumPy
- Pillow

## Install Dependencies

Run this command in the repository folder:

```bash
python -m pip install opencv-python matplotlib numpy Pillow
```

## Run a Program

Run the required program from the repository folder. For example:

```bash
python Program_01_Read_Display_Image.py
```

Replace the filename with the program you want to run.

Keep each required input image in the same folder as its Python script:

- Program 1: `flower.jpg`
- Programs 2, 3, 5, 6, 7, and 9: `scene.jpg`
- Program 4: `sunset.png`
- Program 8: `car.jpg`
- Program 10: `img1.jpg` and `img2.jpg`

The programs print an error message if a required image is missing or cannot be read.
