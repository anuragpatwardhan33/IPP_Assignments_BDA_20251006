"""
Program 3: Convert a Color Image to Grayscale
Objective:
Load a color image using OpenCV, convert it to grayscale, and save the
result as output_gray.jpg.

Required input:
    scene.jpg (place it in the same folder as this Python script)
"""

import os
import cv2

INPUT_PATH = "scene.jpg"
OUTPUT_PATH = "output_gray.jpg"


def main():
    if not os.path.exists(INPUT_PATH):
        print(f"Error: '{INPUT_PATH}' was not found.")
        print("Place scene.jpg in the same folder as this script.")
        return

    image = cv2.imread(INPUT_PATH, cv2.IMREAD_COLOR)

    if image is None:
        print(f"Error: OpenCV could not read '{INPUT_PATH}'.")
        print("Check that the file is a valid image.")
        return

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    saved = cv2.imwrite(OUTPUT_PATH, gray_image)
    if not saved:
        print(f"Error: Could not save '{OUTPUT_PATH}'.")
        return

    print("Image converted to grayscale successfully.")
    print(f"Input image: {INPUT_PATH}")
    print(f"Output image: {OUTPUT_PATH}")
    print(f"Original image dimensions: {image.shape}")
    print(f"Grayscale image dimensions: {gray_image.shape}")


if __name__ == "__main__":
    main()
