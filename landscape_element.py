from abc import ABC

from PIL import Image


class LandscapeElement(ABC):
    img_size = (200, 150)

    def __repr__(self) -> str:
        raise NotImplementedError

    def draw(self, background: Image, position: tuple[int, int]) -> None:
        raise NotImplementedError
