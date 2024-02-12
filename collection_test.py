from PIL import Image
from matplotlib import pyplot as plt

from collection import Forrest, Village, Landscape
from house import House, Address
from plotting import PICTURE_WIDTH, PICTURE_HEIGHT
from tree import AppleTree, PearTree

TEST_ADDRESS_1 = Address("Fantasialand", "1337", "Hogwarts", "Sesamstraße", 30)
TEST_ADDRESS_2 = Address("Fantasialand", "1337", "Hogwarts", "Sesamstraße", 32)


def test_print_forrest() -> None:
    forrest = Forrest([AppleTree(5), AppleTree(3)])

    print("\n" + str(forrest))


def test_print_village() -> None:
    village = Village([House(4, TEST_ADDRESS_1), House(3, TEST_ADDRESS_2)])

    print("\n" + str(village))


def test_print_landscape() -> None:
    village = Village([House(4, TEST_ADDRESS_1), House(3, TEST_ADDRESS_2)])
    landscape = Landscape([village, AppleTree(5)])

    print(landscape)


def test_make_winter_landscape() -> None:
    village = Village([House(4, TEST_ADDRESS_1), House(3, TEST_ADDRESS_2)])
    landscape = Landscape([village, AppleTree(5)])
    landscape.make_winter()
    print(landscape)


def test_draw_landscape() -> None:
    forrest = Forrest([PearTree(2), PearTree(3), PearTree(2), PearTree(3)])
    village = Village([House(1, TEST_ADDRESS_1),  House(2, TEST_ADDRESS_2)])
    landscape = Landscape([forrest,House(3, TEST_ADDRESS_1), AppleTree(5), House(3, TEST_ADDRESS_1), village])

    width, height = PICTURE_WIDTH, PICTURE_HEIGHT  # Total size of the composite picture
    composite_img = Image.new('RGB', (width, height), color='white')
    landscape.draw(composite_img, position=(0, 0))
    # Displaying the composite image
    plt.imshow(composite_img)
    plt.axis('off')  # Turn off axis
    plt.show()
