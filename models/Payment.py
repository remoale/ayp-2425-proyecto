from models.Customer import Customer

class Payment:
    def __init__(self, customer: Customer, amount: float, currency: str,
                 type: str, date: str):
        self.customer = customer
        self.amount = amount
        self.currency = currency
        self.type = type
        self.date = date
    

    def __str__(self):
        return (f'Payment(customer={self.customer}, amount={self.amount}, currency={self.currency}, '
                f'type={self.type}, date={self.date})')
