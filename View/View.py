import tkinter.messagebox
from tkinter import *
from View import MakePizzaWindow


class View:

    def __init__(self, controller):
        self.controller = controller
        self.window = Tk()
        self.window.title("Pizza time!")
        self.window.geometry("950x390")
        self.instruction_label = Label(text="Make selection by clicking list and/or buttons")
        self.instruction_label.place(x=10, y=0)
        self.instruction_label_two = Label(text="Current order:")
        self.instruction_label_two.place(x=470, y=0)
        self.cost = 0
        self.cost_label = StringVar()
        self.cost_label.set("Total cost: " + str(self.cost) + "kr")
        self.instruction_label = Label(textvariable=self.cost_label)
        self.instruction_label.place(x=800, y=0)
        self.left_text_field = Listbox(height=20, width=75)
        self.right_text_field = Listbox(height=20, width=75)
        self.left_text_field.place(x=10, y=15)
        self.right_text_field.place(x=470, y=15)
        self.button_food = Button(text="FOOD", command=lambda: self.event_to_controller("FOOD"))
        self.button_food.place(x=10, y=350)
        self.button_drinks = Button(text="DRINKS", command=lambda: self.event_to_controller("DRINKS"))
        self.button_drinks.place(x=60, y=350)
        self.button_add = Button(text="ADD", command=lambda: self.event_to_controller("ADD"))
        self.button_add.place(x=118, y=350)
        self.button_create = Button(text="CREATE PIZZA", command=self.pizza_window)
        self.button_create.place(x=160, y=350)
        self.button_history = Button(text="ORDER HISTORY", command=lambda: self.event_to_controller("HISTORY"))
        self.button_history.place(x=255, y=350)
        self.button_order = Button(text="ORDER", command=lambda: self.event_to_controller("ORDER"))
        self.button_order.place(x=480, y=350)
        self.button_view = Button(text="VIEW ORDER", command=lambda: self.event_to_controller("VIEW"))
        self.button_view.place(x=540, y=350)

    def start(self):
        self.window.mainloop()

    def event_to_controller(self, button_text: str):
        self.controller.button_clicked(button_text)

    def pizza_window(self):
        MakePizzaWindow.MakePizzaWindow(self.controller)

    def populate_left(self, arr: []):
        self.clear_left()
        for item in arr:
            self.left_text_field.insert(END, item)

    def clear_left(self):
        self.left_text_field.delete(0, END)

    def clear_right(self):
        self.right_text_field.delete(0, END)

    def clear_cost(self):
        self.cost = 0
        self.cost_label.set("Total cost:" + str(self.cost) + "kr")

    def add_to_right(self, item: str, cost: int):
        self.update_cost(cost)
        self.right_text_field.insert(END, item)

    def update_cost(self, new_cost: int):
        self.cost += new_cost
        self.cost_label.set("Total cost: " + str(self.cost) + "kr")

    def display_message(self, message: str):
        tkinter.messagebox.showinfo("INFO", message=message)

    def age_check(self) -> str:
        result = tkinter.messagebox.askquestion("Ålderskontroll", message="Är du över 18 år?")
        return result
