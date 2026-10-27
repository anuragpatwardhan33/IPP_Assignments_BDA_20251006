"""
Program 10: Calculate Mean Squared Error (MSE) Between Two Grayscale Images

Objective:
Read two images, convert them to grayscale, and calculate the Mean
Squared Error (MSE) between them.

Required files:
    img1.jpg
    img2.jpg

Place both images in the same folder as this Python script.

Formula:
    MSE = (1 / N) * sum((Image1 - Image2) ** 2)

N is the total number of pixels. The two images must have the same dimensions.
"""

import os
import cv2
import numpy as np


IMAGE1_PATH = "img1.jpg"
IMAGE2_PATH = "img2.jpg"


def main():
    # Check that both image files exist.
    if not os.path.exists(IMAGE1_PATH):
        print(f"Error: '{IMAGE1_PATH}' was not found.")
        print("Place img1.jpg in the same folder as this script.")
        return

    if not os.path.exists(IMAGE2_PATH):
        print(f"Error: '{IMAGE2_PATH}' was not found.")
        print("Place img2.jpg in the same folder as this script.")
        return

    # Read both images in grayscale.
    image1 = cv2.imread(IMAGE1_PATH, cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread(IMAGE2_PATH, cv2.IMREAD_GRAYSCALE)

    if image1 is None or image2 is None:
        print("Error: One or both images could not be read.")
        return

    # MSE requires the images to have identical dimensions.
    if image1.shape != image2.shape:
        print("Error: The two grayscale images must have the same dimensions.")
        print(f"img1.jpg dimensions: {image1.shape}")
        print(f"img2.jpg dimensions: {image2.shape}")
        print("Resize or crop the images so their dimensions match, then run again.")
        return

    # Convert to floating-point values before subtraction to avoid overflow.
    difference = image1.astype(np.float64) - image2.astype(np.float64)
    mse = np.mean(difference ** 2)

    print("Mean Squared Error (MSE) calculated successfully.")
    print(f"Image dimensions: {image1.shape[1]} x {image1.shape[0]}")
    print(f"MSE: {mse:.4f}")

    if mse == 0:
        print("The images are identical at the pixel level after grayscale conversion.")
    else:
        print("An MSE of 0 means identical grayscale pixels; larger values indicate greater pixel differences.")


if __name__ == "__main__":
    main()
