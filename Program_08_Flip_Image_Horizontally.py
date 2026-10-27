"""
Program 8: Flip an Image Horizontally (Left to Right)
Objective:
Load car.jpg using OpenCV, flip it from left to right, and display
the original and flipped images.

Required file:
    car.jpg (place it in the same folder as this Python script)

Output:
    Displays the original image and its horizontally flipped version.
"""

import os
import cv2
import matplotlib.pyplot as plt

IMAGE_PATH = "car.jpg"


def main():
    # Check whether the image file exists.
    if not os.path.exists(IMAGE_PATH):
        print(f"Error: '{IMAGE_PATH}' was not found.")
        print("Place car.jpg in the same folder as this script.")
        return

    # Read the image in color.
    image = cv2.imread(IMAGE_PATH, cv2.IMREAD_COLOR)

    if image is None:
        print(f"Error: OpenCV could not read '{IMAGE_PATH}'.")
        return

    # Flip horizontally: flipCode=1 means left-to-right.
    flipped_image = cv2.flip(image, 1)

    print("Image flipped horizontally successfully.")
    print(f"Original dimensions (width x height): {image.shape[1]} x {image.shape[0]}")
    print(f"Flipped dimensions (width x height): {flipped_image.shape[1]} x {flipped_image.shape[0]}")

    # Convert BGR to RGB so Matplotlib displays colors correctly.
    original_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    flipped_rgb = cv2.cvtColor(flipped_image, cv2.COLOR_BGR2RGB)

    # Display original and flipped images side by side.
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(original_rgb)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(flipped_rgb)
    plt.title("Horizontally Flipped Image")
    plt.axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
