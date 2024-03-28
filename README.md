# image2litematica

## How To:
- Set FILE_PATH to the path to the construction plan image
- Set isChunkInverted to True if the chunk borders of the construction
  plan are inverted.
	Not Yet Implemented: Custom Chunk offset. Currently fixed to
	full chunk in horizontal axis and half chunk offset in vertical
	axis
- Set blocksDir to the directory where the png images corresponding to
	the block tops are. WARNING: This is only possible manually!
	Meaning, you have to remove duplicate files (such as respawn anchor
	bottom and obsidian), rename some files (snow to snow_block or 
	blackstone_top to blackstone), care about transparent (glass) and
	greyscale (leaves) images, furthermore care about animated blocks
	and distinguish between log and wood blocks (e.g. oak log / oak wood)

Because this is tiring work, maybe until there is a possible fix
	stick to the schematic in the releases.

## Future plans for this project: 
Convert any image (both already
 	generated building plan and also normal yet-to-be-converted images)
	into a minecraft schematic that can be placed into your world as
	2d pixelart, e.g. on minecraft r/place contests.



## Info for the individual sub-programs:
- img2array.py : Read a already finished construction plan and split it into all the different distinct blocks used. Save the individual blocks and a list of the corresponding indices to a file
- imageFileSearcher.py : For every splitted block, search in the minecraft assets for its real name. Warning! This step requires a LOT of manual work, as the blocks do not always match and the files are sometimes named differently
- array2schematic.py : convert the array (copy from the text file created earlier) and the corresponding blocks (manually create a dictionary from the output of the previous step) to a litematica schematic.
- main.py : all those steps merged together, but manually is easier in my opinion.
