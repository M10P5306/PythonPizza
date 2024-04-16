import tkinter.ttk
from tkinter import *
from tkinter import messagebox
from Global import Toppings


class MakePizzaWindow:
    def onselect(self, evt):
        index = evt.widget.curselection()
        evt.widget.delete(index)

    def onclick(self, evt):
        for i in range(self.listbox.size()):
            if self.listbox.get(i) == evt.widget.get():
                return
        self.listbox.insert(END, evt.widget.get())

    def get_pizza_info(self):
        pizza_name = self.name_field.get("1.0", END)[:-1]
        pizza_toppings = []

        if len(pizza_name) > 1:
            for i in range(self.listbox.size()):
                index = self.toppings_list_names.index(self.listbox.get(i))
                pizza_toppings.append(self.toppings_list[index])

            self.controller.add_new_pizza(pizza_name, pizza_toppings)
            self.new_window.destroy()
        else:
            tkinter.messagebox.showinfo("No pizza name",message="Please enter pizza name.", parent=self.new_window)

    def __init__(self, controller):
        self.toppings_list = [Toppings.Toppings.kebab, Toppings.Toppings.shrimps, Toppings.Toppings.pineapple,
                              Toppings.Toppings.garlic_sauce, Toppings.Toppings.basil, Toppings.Toppings.ham,
                              Toppings.Toppings.mushrooms, Toppings.Toppings.onions]

        self.toppings_list_names = []
        for topping in self.toppings_list:
            self.toppings_list_names.append(topping._name_)

        self.controller = controller
        self.new_window = Tk()
        self.new_window.title("Make some pizza!")
        self.new_window.geometry("350x350")
        self.label = tkinter.Label(self.new_window, text="Pizza name")
        self.label.place(x=10, y=10)
        self.name_field = tkinter.Text(self.new_window, height=1, width=37)
        self.name_field.place(x=10, y=30)
        self.label_two = tkinter.Label(self.new_window, text="Toppings (click topping to delete)")
        self.label_two.place(x=10, y= 55)
        self.listbox = tkinter.Listbox(self.new_window, name="listbox", height=10, width=50)
        self.listbox.bind("<<ListboxSelect>>", self.onselect)
        self.listbox.place(x=10, y=80)
        self.topping_box = tkinter.ttk.Combobox(self.new_window, state="readonly", width=30, values=self.toppings_list_names)
        self.topping_box.bind("<<ComboboxSelected>>", self.onclick)
        self.topping_box.place(x=10, y=250)
        self.button = tkinter.Button(self.new_window, text="Add to Menu", command=self.get_pizza_info)
        self.button.place(x=232, y=250)
        self.new_window.mainloop()
