class Order:
    def __init__(self):
        self.items = []
        self.cost = 0

    def add_item(self, item):
        self.items.append(item)
        self.cost += item.cost
