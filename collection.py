from typing import Generic, TypeVar

from house import House
from landscape_element import LandscapeElement
from tree import Tree

T = TypeVar("T")


class Collection(Generic[T]):

    def __init__(self, items: list[T]) -> None:
        self.items = items

    def __repr__(self) -> str:
        out = "\n".join([str(item) for item in self.items])
        return f"{self.__class__.__name__} consisting of: \n{out}"


class Forrest(Collection[Tree], LandscapeElement):
    pass


class Village(Collection[House], LandscapeElement):
    pass


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
