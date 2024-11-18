class Customer:
    def __init__(self, name: str, id: str, email: str,
                 address: str, phone: str, legal: bool):
        self.name = name
        self.id = id
        self.email = email
        self.address = address
        self.phone = phone
        self.legal = legal


    def __str__(self):
        return (f'Customer(name={self.name}, id={self.id}, email={self.email}, '
                f'address={self.address}, phone={self.phone}, legal={self.legal})')
