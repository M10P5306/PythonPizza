from Model import Drink, AlcoholicDrink, Pizza
from Global import Toppings


class MenuManager:
    def __init__(self):
        self.food = []
        self.drinks = []
        self.fill_drinks()
        self.fill_food()

    def fill_drinks(self):
        drink1 = Drink.Drink("Fanta",15, 33)
        drink2 = Drink.Drink("Cola",15, 33)
        drink3 = AlcoholicDrink.AlcoholicDrink("Falcon", 75, 50, 5.5)
        self.drinks.append(drink1)
        self.drinks.append(drink2)
        self.drinks.append(drink3)

    def fill_food(self):
        pizza1 = Pizza.Pizza("Margarita", [Toppings.Toppings.basil])
        pizza2 = Pizza.Pizza("Calzone", [Toppings.Toppings.ham, Toppings.Toppings.mushrooms])
        pizza3 = Pizza.Pizza("Kebab", [Toppings.Toppings.kebab, Toppings.Toppings.garlic_sauce, Toppings.Toppings.onions])
        pizza4 = Pizza.Pizza("Frankenstein", [Toppings.Toppings.ham, Toppings.Toppings.shrimps])
        pizza5 = Pizza.Pizza("Hawaii", [Toppings.Toppings.ham, Toppings.Toppings.pineapple])
        self.food.append(pizza1)
        self.food.append(pizza2)
        self.food.append(pizza3)
        self.food.append(pizza4)
        self.food.append(pizza5)

    def add_pizza(self, pizza):
        self.food.append(pizza)
