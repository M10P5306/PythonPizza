from abc import ABC, abstractmethod


class MenuItem(ABC):

    @abstractmethod
    def __init__(self, name: str, cost: int):
        self.name = name
        self.cost = cost