"""
Program 6: Crop the Central 200 x 200 Region of an Image
Objective:
Load an image, crop a 200 x 200 pixel region from its center, and display
the cropped result using Matplotlib.

Required file:
    scene.jpg (place it in the same folder as this Python script)
"""

import os
import cv2
import matplotlib.pyplot as plt

IMAGE_PATH = "scene.jpg"
CROP_WIDTH = 200
CROP_HEIGHT = 200


def main():
    if not os.path.exists(IMAGE_PATH):
        print(f"Error: '{IMAGE_PATH}' was not found.")
        print("Place scene.jpg in the same folder as this script.")
        return

    image = cv2.imread(IMAGE_PATH, cv2.IMREAD_COLOR)

    if image is None:
        print(f"Error: OpenCV could not read '{IMAGE_PATH}'.")
        return

    height, width = image.shape[:2]

    if width < CROP_WIDTH or height < CROP_HEIGHT:
        print(
            f"Error: Image must be at least {CROP_WIDTH} x {CROP_HEIGHT} pixels. "
            f"Current size is {width} x {height}."
        )
        return

    # Calculate the top-left corner so the crop is centered.
    x_start = (width - CROP_WIDTH) // 2
    y_start = (height - CROP_HEIGHT) // 2

    cropped_image = image[
        y_start:y_start + CROP_HEIGHT,
        x_start:x_start + CROP_WIDTH
    ]

    print("Center crop completed successfully.")
    print(f"Original dimensions (width x height): {width} x {height}")
    print(f"Cropped dimensions (width x height): {cropped_image.shape[1]} x {cropped_image.shape[0]}")

    # OpenCV uses BGR; convert to RGB for correct Matplotlib colors.
    cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(6, 6))
    plt.imshow(cropped_rgb)
    plt.title("Center Crop (200 x 200)")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
