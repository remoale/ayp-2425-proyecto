class Shipping:
    def __init__(self, order: str, service: str, cost: float):
        self.order = order
        self.service = service
        self.cost = cost


    def __str__(self):
        return (f'Shipping(order={self.order}, service={self.service}, cost={self.cost})')
