# Top: Half chunk
# Bottom: Half chunk
# Width: 80 chunks
# Height: 45

# Halb		| 
# 44 Chunks	| x80
# Halb		| 

# x: (256*n)-1
# y: 128+(265*n)-1
# blocks: 1280 x 720


from PIL import Image
from tqdm import trange
import numpy as np
import os

# Image.MAX_IMAGE_PIXELS = None
# img = Image.open(r"D:\Downloads\construction_plan.png")
# pixels = img.load()
# width, height = img.size
# for y in trange(height):
# 	for x in range(width):
# 		if x % 256 == 255 or y % 256 == 127:
# 			r, g, b = pixels[x, y]
# 			pixels[x, y] = (255 - r, 255 - g, 255 - b)
# img.save(r"D:\Downloads\construction_planInverted.png")

Image.MAX_IMAGE_PIXELS = None

def split_image(image_path, output_dir):
	# Open the image file
	img = Image.open(image_path)
	width, height = img.size

	# Define the size of the split images
	split_width = 16
	split_height = 16

	# Calculate the number of splits in x and y directions
	x_splits = width // split_width
	y_splits = height // split_height

	# Create a 2D array to hold the split images
	split_images = [[None for _ in range(x_splits)] for _ in range(y_splits)]

	# Create a dictionary to hold the distinct images
	distinct_images = {}
	next_index = 0

	# Loop over the image and create the split images
	for i in trange(y_splits):
		for j in range(x_splits):
			left = j * split_width
			upper = i * split_height
			right = (j + 1) * split_width
			lower = (i + 1) * split_height
			sub_image = img.crop((left, upper, right, lower))

			# Convert the sub image to a numpy array and make it hashable
			sub_image_arr = np.array(sub_image)
			sub_image_hashable = sub_image_arr.tostring()

			# If the sub image is not in the dictionary, add it
			if sub_image_hashable not in distinct_images:
				distinct_images[sub_image_hashable] = next_index
				# save the individual block image to a directory
				sub_image.save(os.path.join(output_dir, f'{next_index}.png'))
				next_index += 1

			# Replace the sub image in the array with its index
			split_images[i][j] = distinct_images[sub_image_hashable]

	return split_images


# save splitted array to a file
a = split_image(r"D:\Downloads\construction_planInverted.png", r"D:\Downloads\subImages")
with open(r"D:\Downloads\subImages\a.txt", 'w') as f1:
	f1.write(str(a))
