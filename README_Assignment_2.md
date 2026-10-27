# Assignment 2

## Image Processing Lab Programs

This repository contains 10 Image Processing programs implemented in Python using OpenCV, Pillow, NumPy, and Matplotlib.

## Programs Included

1. **Read and Display an Image Using OpenCV** — Reads `flower.jpg`, prints its dimensions and data type, and displays the image.
2. **Display Image Dimensions and Data Type** — Prints the height, width, channels, and data type of `scene.jpg`.
3. **Convert a Color Image to Grayscale** — Converts `scene.jpg` to grayscale and saves `output_gray.jpg`.
4. **Display an Image Using Pillow** — Opens and displays `sunset.png`.
5. **Resize an Image to 50%** — Resizes `scene.jpg` to half its original width and height.
6. **Crop the Center 200 × 200 Pixels** — Crops and displays the central 200 × 200 area of `scene.jpg`.
7. **Rotate an Image 90° Clockwise** — Rotates `scene.jpg` clockwise by 90 degrees.
8. **Flip an Image Horizontally** — Flips `car.jpg` from left to right.
9. **Convert an Image to HSV** — Displays the Hue, Saturation, and Value channels of `scene.jpg`.
10. **Calculate Mean Squared Error (MSE)** — Calculates MSE between grayscale versions of `img1.jpg` and `img2.jpg`.

## Files

- `Assignment_2_Image_Processing.ipynb` — Jupyter Notebook containing all 10 programs.
- Individual `.py` files — Each program is also provided as a separate Python script.
- Image files — Input images required by the programs.

## Requirements

- Python 3
- OpenCV (`opencv-python`)
- Pillow
- NumPy
- Matplotlib

Install the required packages with:

```bash
python -m pip install opencv-python pillow numpy matplotlib
```

## How to Run

1. Download or clone this repository.
2. Keep the required input images in the same folder as the notebook or Python scripts.
3. Open `Assignment_2_Image_Processing.ipynb` in Jupyter Notebook.
4. Run the cells from top to bottom.

Alternatively, run an individual script from a terminal, for example:

```bash
python Program_01_Read_Display_Image.py
```

Replace the filename with the program you want to execute.

## Input Images Required

- Program 1: `flower.jpg`
- Programs 2, 3, 5, 6, 7, and 9: `scene.jpg`
- Program 4: `sunset.png`
- Program 8: `car.jpg`
- Program 10: `img1.jpg` and `img2.jpg`

The two images used in Program 10 must have the same dimensions.
