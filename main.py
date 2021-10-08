# Imports
from PIL import Image

# Functions
def main():
    map: list = []

    with Image.open("map.png") as img:
        pix = img.load()

        # Load through 16 by 16
        for y in range(16):
            map.append([])
            for x in range(16):
                # Get Pixel
                pixl: tuple = pix[x, y]

                # Remove Errors
                pixel = []
                for z in pixl:
                    if z < 5:
                        pixel.append(0)
                    else:
                        pixel.append(z)

                # Sort Colours
                if pixel == [0, 0, 0, 255]:  # Wall
                    map[y].append(1)
                elif pixel == [0, 0, 255, 255]:  # Door
                    map[y].append(2)
                elif pixel == [0, 255, 0, 255]:  # Player
                    map[y].append(3)
                elif pixel == [255, 0, 0, 255]:  # Enemy
                    map[y].append(4)
                else:  # Blank
                    map[y].append(0)

    print(map)


# Run main
if __name__ == "__main__":
    main()
