"""
Program 9: Convert a Color Image to HSV and Display H, S, and V Channels

Objective:
Load a color image using OpenCV, convert it from BGR to HSV,
and display the Hue, Saturation, and Value channels separately.

Required file:
    scene.jpg (place it in the same folder as this Python script)
"""

import os
import cv2
import matplotlib.pyplot as plt

IMAGE_PATH = "scene.jpg"


def main():
    # Check whether the image file exists.
    if not os.path.exists(IMAGE_PATH):
        print(f"Error: '{IMAGE_PATH}' was not found.")
        print("Place scene.jpg in the same folder as this script.")
        return

    # Read the image in color.
    image = cv2.imread(IMAGE_PATH, cv2.IMREAD_COLOR)

    if image is None:
        print(f"Error: OpenCV could not read '{IMAGE_PATH}'.")
        return

    # OpenCV reads images in BGR format; convert to HSV.
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Split the HSV image into its three channels.
    hue, saturation, value = cv2.split(hsv_image)

    print("Image converted to HSV successfully.")
    print(f"Image dimensions (height, width): {image.shape[0]}, {image.shape[1]}")
    print("HSV channels extracted: Hue, Saturation, Value")

    # Display the original image and each HSV channel.
    original_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(original_rgb)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(2, 2, 2)
    plt.imshow(hue, cmap="gray")
    plt.title("Hue (H) Channel")
    plt.axis("off")

    plt.subplot(2, 2, 3)
    plt.imshow(saturation, cmap="gray")
    plt.title("Saturation (S) Channel")
    plt.axis("off")

    plt.subplot(2, 2, 4)
    plt.imshow(value, cmap="gray")
    plt.title("Value (V) Channel")
    plt.axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
