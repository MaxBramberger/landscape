from typing import Generic, TypeVar

import numpy as np
from PIL import Image

from house import House
from landscape_element import LandscapeElement
from plotting import area_in_picture
from tree import Tree

T = TypeVar("T")


class Collection(Generic[T]):

    def __init__(self, items: list[T]) -> None:
        self.items = items

    def __repr__(self) -> str:
        out = "\n".join([str(item) for item in self.items])
        return f"{self.__class__.__name__} consisting of: \n{out}"


class Forrest(Collection[Tree], LandscapeElement):
    def draw(self, background: Image, position: tuple[int, int]) -> None:
        draw_items(self.items, background, position)


class Village(Collection[House], LandscapeElement):
    def draw(self, background: Image, position: tuple[int, int]) -> None:
        draw_items(self.items, background, position)


class Landscape(Collection[LandscapeElement]):

    def __init__(self, items: list[LandscapeElement]) -> None:
        tmp = []
        for item in items:
            if isinstance(item, Collection):
                tmp.extend(item.items)
            else:
                tmp.append(item)

        super().__init__(tmp)

    def make_winter(self) -> None:
        for element in self.items:
            if isinstance(element, Tree):
                element.loose_leaves()
            elif isinstance(element, House):
                element.cover_roof_with_snow()

    def draw(self, background: Image, position: tuple[int, int]) -> None:
        draw_items(self.items, background, position)


def draw_items(landscape_items: list[LandscapeElement], background, position):
    offset_x = 0
    offset_y = 0
    for item in landscape_items:
        new_position = (position[0] + offset_x, position[1] + offset_y)
        item.draw(background, new_position)

        if area_in_picture((position[0] + offset_x + item.img_size[0], position[1]), item.img_size):
            offset_x += item.img_size[0]
        else:
            offset_x = 0
            offset_y += item.img_size[1]
