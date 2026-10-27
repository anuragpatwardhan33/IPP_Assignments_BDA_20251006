"""
Program 1: Read and Display an Image Using OpenCV
Objective: Read flower.jpg and display it with the title "Original Image".
"""
import os
import cv2
import matplotlib.pyplot as plt

IMAGE_PATH = "flower.jpg"

def main():
    if not os.path.exists(IMAGE_PATH):
        print(f"Error: '{IMAGE_PATH}' was not found.")
        print("Place flower.jpg in the same folder as this script.")
        return

    image = cv2.imread(IMAGE_PATH)
    if image is None:
        print(f"Error: OpenCV could not read '{IMAGE_PATH}'.")
        print("Check that the file is a valid image.")
        return

    print("Image loaded successfully.")
    print("Image shape (height, width, channels):", image.shape)
    print("Data type:", image.dtype)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(8, 6))
    plt.imshow(image_rgb)
    plt.title("Original Image")
    plt.axis("off")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
