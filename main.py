from PIL import Image
from tqdm import trange
import numpy as np
import os
from litemapy import Schematic, Region, BlockState

FILE_PATH = "./construction_plan.png"
isChunkInverted = True
blocksDir = "./assets/block"

# How To:
# - Set FILE_PATH to the path to the construction plan image
# - Set isChunkInverted to True if the chunk borders of the construction
# 	plan are inverted.
# 	Not Yet Implemented: Custom Chunk offset. Currently fixed to
# 	full chunk in horizontal axis and half chunk offset in vertical
# 	axis
# - Set blocksDir to the directory where the png images corresponding to
# 	the block tops are. WARNING: This is only possible manually!
# 	Meaning, you have to remove duplicate files (such as respawn anchor
# 	bottom and obsidian), rename some files (snow to snow_block or 
# 	blackstone_top to blackstone), care about transparent (glass) and
# 	greyscale (leaves) images, furthermore care about animated blocks
# 	and distinguish between log and wood blocks (e.g. oak log / oak wood)
#
# 	Because this is tiring work, maybe until there is a possible fix
# 	stick to the schematic in the releases.
#
# 	Future plans for this project: Convert any image (both already
# 	generated building plan and also normal yet-to-be-converted images)
# 	into a minecraft schematic that can be placed into your world as
# 	2d pixelart, e.g. on minecraft r/place contests.


##########################################################################
# Better don't touch the code below, but if you want, feel free.

# Helper Method to compare found block images with minecraft assets

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


# Load image

Image.MAX_IMAGE_PIXELS = None
img = Image.open(FILE_PATH)
pixels = img.load()


# If the variable isChunkInverted is set, uninvert the chunk borders

if isChunkInverted:
	width, height = img.size
	for y in trange(height):
		for x in range(width):
			if x % 256 == 255 or y % 256 == 127:
				r, g, b = pixels[x, y]
				pixels[x, y] = (255 - r, 255 - g, 255 - b)


width, height = img.size

# Define the size of the split images
split_width = 16
split_height = 16

# Calculate the number of splits in x and y directions
x_splits = width // split_width
y_splits = height // split_height

# Create a 2D array to hold the split images
arrayOfBlocks = [[None for _ in range(x_splits)] for _ in range(y_splits)]

# Create a dictionary to hold the distinct images
distinct_images = {}
next_index = 0
blockImageDict = {}


# Split the large image into sub-images (blocks) and save them to an array

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
			blockImageDict[next_index] = sub_image
			next_index += 1

		# Replace the sub image in the array with its index
		arrayOfBlocks[i][j] = distinct_images[sub_image_hashable]

blockDict = {}

for index, img1 in blockImageDict.items():
	for file2 in os.listdir(blocksDir):
		if file2.endswith(".png"):
			img2 = Image.open(os.path.join(blocksDir, file2))
			if check_same_pixel_content(img1, img2):
				blockDict[index] = file2.split(".png")[0]

arrayOfBlocks = [row[::-1] for row in arrayOfBlocks[::-1]]

shape = np.array(arrayOfBlocks).shape

reg = Region(0, 0, 0, shape[1], 1, shape[0])
schem = reg.as_schematic(name="name", author="author", description="Made with litemapy")

for x, y, z in reg.allblockpos():
	blockid = a[z][x]
	blockname = b[blockid]
	block = BlockState(f"minecraft:{blockname}")
	reg.setblock(x, y, z, block)

schem.save(f"basti.litematic")
