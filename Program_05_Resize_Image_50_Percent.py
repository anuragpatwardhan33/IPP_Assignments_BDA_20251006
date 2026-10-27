"""
Program 5: Resize an Image to 50% of Its Original Dimensions
Objective:
Read an image using OpenCV, resize it to 50% of its original width and
height, and display the original and resized images.

Required file:
    scene.jpg (place it in the same folder as this Python script)
"""

import os
import cv2
import matplotlib.pyplot as plt

IMAGE_PATH = "scene.jpg"
SCALE_FACTOR = 0.5


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

    original_height, original_width = image.shape[:2]
    new_width = int(original_width * SCALE_FACTOR)
    new_height = int(original_height * SCALE_FACTOR)

    resized_image = cv2.resize(
        image,
        (new_width, new_height),
        interpolation=cv2.INTER_AREA
    )

    print("Image resized successfully.")
    print(f"Original dimensions (width x height): {original_width} x {original_height}")
    print(f"Resized dimensions (width x height): {new_width} x {new_height}")

    # Convert BGR to RGB for correct colors in Matplotlib.
    original_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    resized_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(original_rgb)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(resized_rgb)
    plt.title("Resized Image (50%)")
    plt.axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
