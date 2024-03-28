import os
from PIL import Image
import numpy as np

def check_same_pixel_content(image1, image2):
    # Convert images into numpy arrays
    image1 = image1.convert("RGBA")
    image2 = image2.convert("RGBA")
    image1_array = np.array(image1)
    image2_array = np.array(image2)

    # Check if the shapes of the two images are the same
    if image1_array.shape != image2_array.shape:
        return False

    # Check if the pixel contents of the two images are the same
    return np.array_equal(image1_array, image2_array)
    # return np.all(np.abs(image1_array - image2_array) <= 5)

def find_matching_images(dir1, dir2):
    for file1 in os.listdir(dir1):
        if file1.endswith(".png") or file1.endswith(".jpg"):
            img1 = Image.open(os.path.join(dir1, file1))
            for file2 in os.listdir(dir2):
                if file2.endswith(".png") or file2.endswith(".jpg"):
                    img2 = Image.open(os.path.join(dir2, file2))
                    if check_same_pixel_content(img1, img2):
                        print(f"Matching images found: {file1} in {dir1}, {file2} in {dir2}")

# compare the individual blocks from the image with the minecraft assets
find_matching_images(r"D:\Downloads\subImages", r"D:\Downloads\subImages\block")

