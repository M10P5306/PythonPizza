from Model import MenuItem
from Global import Toppings


class Pizza(MenuItem.MenuItem):
    def __init__(self, name: str, toppings: []):
        super().__init__(name, 60)
        self.tops = [Toppings.Toppings.tomato_sauce, Toppings.Toppings.cheese]
        for topping in toppings:
            self.tops.append(topping)
            self.cost += topping._value_

    def __str__(self) -> str:
        toppoes = ""
        for topping in self.tops:
            toppoes += topping._name_ + ", "
        return self.name + ": " + str(toppoes) + " " + str(self.cost) + "kr"
