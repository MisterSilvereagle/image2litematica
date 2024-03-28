from litemapy import Schematic, Region, BlockState

b = {0: 'warped_hyphae', 1: 'sculk_catalyst', 2: 'respawn_anchor', 3: 'obsidian', 4: 'sculk', 5: 'blue_terracotta', 6: 'lapis_block', 7: 'black_concrete', 8: 'gray_concrete', 9: 'smithing_table', 10: 'deepslate_lapis_ore', 11: 'blue_glazed_terracotta', 12: 'crying_obsidian', 13: 'polished_blackstone', 14: 'warped_planks', 15: 'gray_concrete_powder', 16: 'tinted_glass', 17: 'cyan_stained_glass', 18: 'blue_concrete_powder', 19: 'cyan_glazed_terracotta', 20: 'blue_ice', 21: 'diamond_block', 22: 'cyan_wool', 23: 'cyan_concrete', 24: 'warped_wart_block', 25: 'light_blue_concrete', 26: 'blue_stained_glass', 27: 'light_blue_stained_glass', 28: 'tube_coral_block', 29: 'light_blue_concrete_powder', 30: 'light_blue_wool', 31: 'light_blue_glazed_terracotta', 32: 'glass', 33: 'packed_ice', 34: 'smooth_quartz', 35: 'ice', 36: 'prismarine_bricks', 37: 'white_stained_glass', 38: 'white_concrete_powder', 39: 'white_wool', 40: 'snow_block', 41: 'dark_prismarine', 42: 'warped_stem', 43: 'gray_glazed_terracotta', 44: 'black_concrete_powder', 45: 'coal_block', 46: 'polished_blackstone_bricks', 47: 'stripped_warped_hyphae', 48: 'verdant_froglight', 49: 'prismarine', 50: 'light_gray_glazed_terracotta', 51: 'pearlescent_froglight', 52: 'amethyst_block', 53: 'cyan_concrete_powder', 54: 'black_wool', 55: 'spruce_leaves', 56: 'lapis_ore', 57: 'blackstone', 58: 'diamond_ore', 59: 'cracked_polished_blackstone_bricks', 60: 'oxidized_cut_copper', 61: 'warped_nylium', 62: 'blue_concrete', 63: 'clay', 64: 'white_glazed_terracotta', 65: 'emerald_ore', 66: 'polished_diorite', 67: 'white_concrete', 68: 'lodestone', 69: 'stripped_warped_stem', 70: 'black_stained_glass', 71: 'light_blue_terracotta', 72: 'black_terracotta', 73: 'diorite', 74: 'iron_block', 75: 'ochre_froglight', 76: 'blue_wool', 77: 'magenta_stained_glass', 78: 'purpur_block', 79: 'purpur_pillar', 80: 'purple_stained_glass', 81: 'deepslate_diamond_ore', 82: 'cherry_leaves', 83: 'magenta_glazed_terracotta', 84: 'deepslate_emerald_ore', 85: 'cracked_deepslate_tiles', 86: 'cherry_log', 87: 'spruce_wood', 88: 'purple_glazed_terracotta', 89: 'smooth_basalt', 90: 'chiseled_deepslate', 91: 'nether_bricks', 92: 'gray_wool', 93: 'smooth_stone', 94: 'crimson_planks', 95: 'dried_kelp_block', 96: 'cracked_nether_bricks', 97: 'chiseled_nether_bricks', 98: 'cherry_wood', 99: 'calcite', 100: 'chiseled_polished_blackstone', 101: 'cracked_stone_bricks', 102: 'andesite', 103: 'dark_oak_wood', 104: 'oxidized_copper', 105: 'end_stone_bricks', 106: 'emerald_block', 107: 'light_gray_concrete_powder', 108: 'pink_concrete_powder', 109: 'birch_wood', 110: 'birch_log', 111: 'red_nether_bricks', 112: 'polished_deepslate', 113: 'gilded_blackstone', 114: 'polished_basalt', 115: 'furnace', 116: 'deepslate_tiles', 117: 'cobbled_deepslate', 118: 'bone_block', 119: 'chiseled_stone_bricks', 120: 'basalt', 121: 'purple_concrete', 122: 'mycelium', 123: 'light_gray_stained_glass', 124: 'mushroom_stem', 125: 'mud', 126: 'chiseled_quartz_block', 127: 'pink_glazed_terracotta', 128: 'light_gray_wool', 129: 'slime_block', 130: 'polished_andesite', 131: 'magenta_terracotta', 132: 'coal_ore', 133: 'stone', 134: 'weathered_copper', 135: 'cobblestone', 136: 'white_terracotta', 137: 'gravel', 138: 'quartz_bricks', 139: 'soul_soil', 140: 'purple_terracotta', 141: 'purple_wool', 142: 'stone_bricks', 143: 'netherite_block', 144: 'gold_ore', 145: 'light_gray_concrete', 146: 'deepslate', 147: 'gray_stained_glass', 148: 'birch_leaves'}


reg = Region(-640, -64, -1000, 1280, 1, 720)
schem = reg.as_schematic(name="BastiGHG_rPlace24", author="MisterSilvereagle", description="Made with litemapy")

for x, y, z in reg.allblockpos():
	blockid = a[z][x]
	blockname = b[blockid]
	block = BlockState(f"minecraft:{blockname}")
	reg.setblock(x, y, z, block)

schem.save(f"schematics/basti2.litematic")