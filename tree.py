from enum import Enum

from PIL import Image

from landscape_element import LandscapeElement
from plotting import insert_image


class FruitType(Enum):
    Apple = "Apple"
    Pear = "Pear"


class Tree(LandscapeElement):
    img = "img/tree.jpg"

    def __init__(self, n_fruit: int) -> None:
        self._has_leaves = True
        self._n_fruit = n_fruit

    def __repr__(self) -> str:
        leaves = "with leaves" if self._has_leaves else "without leaves"
        return f"Tree {leaves} and {self._n_fruit} fruits."

    def loose_leaves(self) -> None:
        self._has_leaves = False

    def draw(self, background: Image, position: tuple[int, int]) -> None:
        insert_image(background,self.img, position, self.img_size)


class AppleTree(Tree):

    def __init__(self, n_fruit: int) -> None:
        super().__init__(n_fruit)

    def __repr__(self) -> str:
        leaves = "with leaves" if self._has_leaves else "without leaves"
        return f"Apple tree {leaves} and {self._n_fruit} apples."

    def loose_leaves(self) -> None:
        self._n_fruit = 0
        super().loose_leaves()


class PearTree(Tree):

    def __init__(self, n_fruit: int) -> None:
        super().__init__(n_fruit)

    def __repr__(self) -> str:
        leaves = "with leaves" if self._has_leaves else "without leaves"
        return f"Apple tree {leaves} and {self._n_fruit} apples."

    def loose_leaves(self) -> None:
        self._n_fruit = 0
        super().loose_leaves()

def get_leaf_string(has_leaves: bool) -> str:
    return "with leaves" if has_leaves else "without leaves"
