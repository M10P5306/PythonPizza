from Model import MenuItem


class Drink(MenuItem.MenuItem):
    def __init__(self, name: str, cost: int, volume: int):
        super().__init__(name, cost)
        self.volume = volume

    def __str__(self) -> str:
        return self.name + ", " + str(self.volume) + "cl ," + str(self.cost) + "kr"
