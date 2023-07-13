from typing import Tuple

import numpy as np  # type: ignore

# Testing variables
w_r = 0
w_g = 175
w_b = 255
light_floor = (w_r, w_g, w_b)

# Tile graphics structured type compatible with Console.tiles_rgb.
graphic_dt = np.dtype(
    [
        # Originally the unicode codepoint was ("ch", np.int32)
        ("ch", "2B"),  # Unicode codepoint.
        ("fg", "3B"),  # 3 unsigned bytes, for RGB colors.
        ("bg", "3B"),
    ]
)

# Tile struct used for statically defined tile data.
tile_dt = np.dtype(
    [
        ("walkable", bool),  # True if this tile can be walked over.
        ("transparent", bool),  # True if this tile doesn't block FOV.
        ("dark", graphic_dt),  # Graphics for when this tile is not in FOV.
        ("light", graphic_dt),  # Graphics for when the tile is in FOV.
    ]
)


def new_tile(
    *,  # Enforce the use of keywords, so that parameter order doesn't matter.
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
    light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """Helper function for defining individual tile types """
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)


# SHROUD represents unexplored, unseen tiles
SHROUD = np.array((ord(" "), (255, 255, 255), (3, 3, 3)), dtype=graphic_dt)

floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord("."), (7, 11, 12), (0, 0, 0)),
    light=(ord("."), (light_floor), (1, 1, 1)),
)
wall = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord("#"), (14, 22, 23), (5, 5, 5)),
    light=(ord(""), (255, 255, 255), (0, 0, 0)),
    # (21, 33, 35)
)
water = new_tile(
    walkable=False,
    transparent=True,
    dark=(ord("="), (2, 28, 79), (0, 0, 0)),
    light=(ord("="), (255, 255, 255), (0, 0, 0)),
    # (23, 79, 191)
)
down_stairs = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(">"), (0, 0, 100), (255, 255, 255)),
    light=(ord(">"), (255, 255, 255), (20, 18, 5)),
)