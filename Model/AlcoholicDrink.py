from Model import Drink


class AlcoholicDrink(Drink.Drink):
    def __init__(self, name: str, cost: int, volume: int, alcohol_volume: float):
        super().__init__(name, cost, volume)
        self.alcohol_volume = alcohol_volume

    def __str__(self):
        return self.name + " " + str(self.alcohol_volume) + "%, " + str(self.volume) + "cl ," + str(self.cost) + "kr"
