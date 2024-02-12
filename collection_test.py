from collection import Forrest, Village, Landscape
from house import House, Address
from tree import AppleTree


def test_print_forrest() -> None:
    forrest = Forrest([AppleTree(5), AppleTree(3)])

    print("\n" + str(forrest))


def test_print_village() -> None:
    address_1 = Address("Fantasialand", "1337", "Hogwarts", "Sesamstraße", 30)
    address_2 = Address("Fantasialand", "1337", "Hogwarts", "Sesamstraße", 32)
    village = Village([House(4, address_1), House(3, address_2)])

    print("\n" + str(village))


def test_print_landscape() -> None:
    address_1 = Address("Fantasialand", "1337", "Hogwarts", "Sesamstraße", 30)
    address_2 = Address("Fantasialand", "1337", "Hogwarts", "Sesamstraße", 32)
    village = Village([House(4, address_1), House(3, address_2)])
    landscape = Landscape([village, AppleTree(5)])

    print(landscape)


def test_make_winter_landscape() -> None:
    address_1 = Address("Fantasialand", "1337", "Hogwarts", "Sesamstraße", 30)
    address_2 = Address("Fantasialand", "1337", "Hogwarts", "Sesamstraße", 32)
    village = Village([House(4, address_1), House(3, address_2)])
    landscape = Landscape([village, AppleTree(5)])
    landscape.make_winter()
    print(landscape)
