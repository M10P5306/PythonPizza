import Model.Pizza
from View import View
from Model import MenuManager, OrderManager, AlcoholicDrink, Order


class Controller:

    def __init__(self):
        self.menu_manager = MenuManager.MenuManager()
        self.view = View.View(self)
        self.order_manager = OrderManager.OrderManager()
        self.selected = None
        self.curr_order = Order.Order()
        self.view.start()

    def button_clicked(self, button_type: str):
        match button_type:
            case "DRINKS":
                if self.selected == "HISTORY":
                    self.view.clear_right()
                    self.view.clear_cost()
                self.selected = "DRINKS"
                drinks = []
                for drink in self.menu_manager.drinks:
                    drinks.append(drink.__str__())
                self.view.populate_left(drinks)
            case "FOOD":
                if self.selected == "HISTORY":
                    self.view.clear_right()
                    self.view.clear_cost()
                self.selected = "FOOD"
                self.display_pizzas()
            case "ADD":
                if self.view.left_text_field.curselection():
                    if self.selected == "FOOD" or "DRINKS":
                        index = self.view.left_text_field.curselection()[0]
                        self.add_to_order(self.selected, index)
            case "ORDER":
                if not self.curr_order:
                    self.view.display_message("Ordern är tom")
                    return
                has_pizza = False
                for item in self.curr_order.items:
                    if type(item) == Model.Pizza.Pizza:
                        has_pizza = True
                if has_pizza:
                    self.order_manager.add_to_history(self.curr_order)
                    self.curr_order = Order.Order()
                    self.view.clear_cost()
                    self.view.clear_right()
                else:
                    self.view.display_message("Måste finnas pizza i en beställning.")
            case "HISTORY":
                if not self.curr_order.items:
                    self.selected = "HISTORY"
                    self.display_orders()
                else:
                    self.view.display_message("Färdigställ din order först.")
            case "VIEW":
                if self.selected == "HISTORY":
                    self.view.clear_right()
                    self.view.clear_cost()
                    index = self.view.left_text_field.curselection()[0]
                    self.show_order(self.order_manager.order_history[index])

    def show_order(self, order):
        for item in order.items:
            name = item.__str__()
            price = item.cost
            self.view.add_to_right(name, price)

    def add_to_order(self, info: str, index: int):
            if info == "DRINKS":

                if type(self.menu_manager.drinks[index]) == Model.AlcoholicDrink.AlcoholicDrink:
                    if self.view.age_check() == "no":
                        return

                item = self.menu_manager.drinks[index].__str__()
                cost = self.menu_manager.drinks[index].cost
                self.curr_order.add_item(self.menu_manager.drinks[index])
                self.view.add_to_right(item, cost)

            if info == "FOOD":
                item = self.menu_manager.food[index].__str__()
                cost = self.menu_manager.food[index].cost
                self.curr_order.add_item(self.menu_manager.food[index])
                self.view.add_to_right(item, cost)

    def add_new_pizza(self, name: str, toppings: []):
        new_pizza = Model.Pizza.Pizza(name,toppings)
        self.menu_manager.add_pizza(new_pizza)
        item = new_pizza.__str__()
        cost = new_pizza.cost
        self.curr_order.add_item(new_pizza)
        self.view.add_to_right(item, cost)
        self.display_pizzas()

    def display_pizzas(self):
        self.selected = "FOOD"
        pizzas = []
        for pizza in self.menu_manager.food:
            pizzas.append(pizza.__str__())
        self.view.populate_left(pizzas)

    def display_orders(self):
        orders = []
        counter = 1
        for order in self.order_manager.order_history:
            orders.append("Order " + str(counter) + " " + str(order.cost) + "kr")
            counter += 1
        self.view.populate_left(orders)
