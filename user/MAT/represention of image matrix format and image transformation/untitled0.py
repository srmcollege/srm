from PIL import Image, ImageFilter
import numpy as np
import matplotlib.pyplot as plt
import os

image_path = r"C:\OS 2024\MAT\representation of image matrix format\Screenshot 2024-10-20 201621.png"

if not os.path.exists(image_path):
    print("File not found. Please check the path and file name.")
else:
    def load_image(image_path):
        return Image.open(image_path)

    def image_to_matrix(image):
        return np.array(image)

    def display_image(image, title):
        plt.imshow(image, cmap='gray')
        plt.title(title)
        plt.axis('off')
        plt.show()

    def blur_image(image, radius):
        return image.filter(ImageFilter.GaussianBlur(radius))

    image = load_image(image_path)

    print("Original Image:")
    display_image(image, "Original Image")

    gray_image = image.convert('L')
    matrix_representation = image_to_matrix(gray_image)
    print("Matrix Representation:")
    print(matrix_representation)
    print("Matrix Shape:", matrix_representation.shape)

    radius = float(input("Enter blur radius: "))
    blurred_image = blur_image(image, radius)
    print("Blurred Image:")
    display_image(blurred_image, "Blurred Image")
