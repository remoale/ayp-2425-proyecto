from models.Customer import Customer
from models.Payment import Payment
from models.Shipping import Shipping

class Sale:
    def __init__(self, customer: Customer, products: list[dict], quantity: int,
                 payment: Payment, shipping: Shipping, summary: dict):
        self.customer = customer
        self.products = products
        self.payment = Payment
        self.shipping = shipping
        self.summary = summary


    def __str__(self):
        return (f'Sale(customer={self.customer}, products={self.products}, quantity={self.quantity}, '
                f'payment={self.payment}, shipping={self.shipping}, summary={self.summary})')
