"""
Program 7: Rotate an Image 90 Degrees Clockwise
Objective:
Load an image using OpenCV, rotate it 90 degrees clockwise, and display
the rotated image.

Required file:
    scene.jpg (place it in the same folder as this Python script)
"""

import os
import cv2
import matplotlib.pyplot as plt

IMAGE_PATH = "scene.jpg"


def main():
    if not os.path.exists(IMAGE_PATH):
        print(f"Error: '{IMAGE_PATH}' was not found.")
        print("Place scene.jpg in the same folder as this script.")
        return

    image = cv2.imread(IMAGE_PATH, cv2.IMREAD_COLOR)

    if image is None:
        print(f"Error: OpenCV could not read '{IMAGE_PATH}'.")
        return

    rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    print("Image rotated successfully.")
    print(f"Original dimensions (width x height): {image.shape[1]} x {image.shape[0]}")
    print(f"Rotated dimensions (width x height): {rotated_image.shape[1]} x {rotated_image.shape[0]}")

    # Convert BGR to RGB for correct colors in Matplotlib.
    original_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    rotated_rgb = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(original_rgb)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(rotated_rgb)
    plt.title("Rotated 90° Clockwise")
    plt.axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
