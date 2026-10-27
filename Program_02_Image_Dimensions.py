"""
Program 2: Display Image Dimensions and Data Type
Objective:
Load scene.jpg using OpenCV and print its height, width, number of
channels, and data type.

Required file:
    scene.jpg (place it in the same folder as this Python script)
"""

import os
import cv2

IMAGE_PATH = "scene.jpg"


def main():
    if not os.path.exists(IMAGE_PATH):
        print(f"Error: '{IMAGE_PATH}' was not found.")
        print("Place scene.jpg in the same folder as this script.")
        return

    image = cv2.imread(IMAGE_PATH, cv2.IMREAD_COLOR)

    if image is None:
        print(f"Error: OpenCV could not read '{IMAGE_PATH}'.")
        print("Check that the file is a valid image.")
        return

    height, width, channels = image.shape

    print("Image loaded successfully.")
    print(f"Image name: {IMAGE_PATH}")
    print(f"Height: {height} pixels")
    print(f"Width: {width} pixels")
    print(f"Number of channels: {channels}")
    print(f"Data type: {image.dtype}")


if __name__ == "__main__":
    main()
