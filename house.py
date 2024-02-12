from dataclasses import dataclass

from PIL import Image

from landscape_element import LandscapeElement
from plotting import insert_image


@dataclass
class Address:
    country: str
    zip_code: str
    town: str
    street: str
    house_number: int


class House(LandscapeElement):
    img = "img/house.jpg"

    def __init__(self, number_of_levels: int, address: Address) -> None:
        self._number_of_levels = number_of_levels
        self._address = address
        self._snow_on_roof = False

    def __repr__(self) -> str:
        maybe_snow = " with a snowy roof" if self._snow_on_roof else ""
        return f"{self._number_of_levels} level house at {self._address}{maybe_snow}"

    def draw(self, background: Image, position: tuple[int, int]) -> None:
        insert_image(background,self.img, position, self.img_size)

    def cover_roof_with_snow(self) -> None:
        self._snow_on_roof = True
