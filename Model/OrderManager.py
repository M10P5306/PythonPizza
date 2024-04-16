class OrderManager:

    def __init__(self):
        self.order_history = []

    def add_to_history(self, order: []):
        self.order_history.append(order)