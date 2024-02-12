from abc import ABC


class LandscapeElement(ABC):

    def __repr__(self) -> str:
        raise NotImplementedError
