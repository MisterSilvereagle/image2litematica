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
