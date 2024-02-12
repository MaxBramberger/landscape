from pathlib import Path
from typing import Union

import matplotlib.pyplot as plt
from PIL import Image

PICTURE_WIDTH = 800
PICTURE_HEIGHT = 600


# Function to insert an image onto another image at specified coordinates
def insert_image(background: Image, image: Union[str, Path], position: tuple[int, int], size: tuple[int, int]):
    img = Image.open(image)
    img = img.resize(size)
    background.paste(img, position)


def area_in_picture(position: tuple[int, int], size: tuple[int, int]) -> bool:
    return position[0] + size[0] < PICTURE_WIDTH and position[1] + size[
        1] < PICTURE_HEIGHT


if __name__ == "__main__":
    # Create a blank composite image
    width, height = PICTURE_WIDTH, PICTURE_HEIGHT  # Total size of the composite picture
    composite_img = Image.new('RGB', (width, height), color='white')

    # Inserting images onto the composite image
    insert_image(composite_img, 'img/tree.jpg', (100, 100), (200, 150))

    # Displaying the composite image
    plt.imshow(composite_img)
    plt.axis('off')  # Turn off axis
    plt.show()
