from PIL import Image

# Naming scheme: compass_map_mp_dontetsk_yy_xx.png
# 16x16 tiles, each tile 512x512 pixels
# SIZE = (16, 16)  # The dimensions of the stitched image in tiles
SIZE = (3, 3)
TILE_SIZE = (512, 512)  # The dimensions of each tile in pixels


def get_tile(x, y):
    return Image.open(f'tiles/compass_map_mp_dontetsk_{y:02d}_{x:02d}.png')


def main():
    try:
        with get_tile(1, 1) as first_tile:
            stitched_map = Image.new(first_tile.mode, [SIZE[i]*TILE_SIZE[i] for i in range(2)])
    except FileNotFoundError:
        print("No tiles found.")
        exit(1)

    for y in range(SIZE[1]):
        for x in range(SIZE[0]):
            try:
                with get_tile(x+1, y+1) as tile:
                    if tile.size == TILE_SIZE:
                        stitched_map.paste(tile, (TILE_SIZE[0]*x, TILE_SIZE[1]*y))
                    else:
                        print(f"Invalid tile size at ({x}, {y}). Skipped.")
            except FileNotFoundError:
                print(f"Missing tile at ({x}, {y}). Skipped.")

    print("Success.")
    stitched_map.save('stitched_map.png')
    stitched_map.show()


if __name__ == '__main__':
    main()
