from models.Customer import Customer
from models.Product import Product
from models.Payment import Payment

class Sale:
    def __init__(self, customer: Customer, products: list[Product], quantity: int,
                 payment: Payment, shipping: str, summary: dict):
        self.customer = customer
        self.products = products
        self.quantity = quantity
        self.payment = Payment
        self.shipping = shipping
        self.summary = summary


    def __str__(self):
        return (f'Sale(customer={self.customer}, products={self.products}, quantity={self.quantity}, '
                f'payment={self.payment}, shipping={self.shipping}, summary={self.summary})')
