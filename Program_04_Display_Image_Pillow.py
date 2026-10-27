"""
Program 4: Open and Display an Image Using Pillow
Objective:
Open sunset.png with Pillow and display the image.

Required file:
    sunset.png (place it in the same folder as this Python script)
"""

import os
from PIL import Image
import matplotlib.pyplot as plt

IMAGE_PATH = "sunset.png"


def main():
    if not os.path.exists(IMAGE_PATH):
        print(f"Error: '{IMAGE_PATH}' was not found.")
        print("Place sunset.png in the same folder as this script.")
        return

    try:
        with Image.open(IMAGE_PATH) as image:
            image.load()
            print("Image loaded successfully.")
            print(f"Image name: {IMAGE_PATH}")
            print(f"Image size (width, height): {image.size}")
            print(f"Image mode: {image.mode}")

            plt.figure(figsize=(8, 6))
            plt.imshow(image)
            plt.title("Sunset Image (Pillow)")
            plt.axis("off")
            plt.tight_layout()
            plt.show()

    except OSError as error:
        print(f"Error: Could not open the image: {error}")


if __name__ == "__main__":
    main()
