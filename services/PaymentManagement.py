from services.Data import sales, customers
from services.CustomerManagement import CustomerManagement

class PaymentManagement:
    def __init__(self, sales, customers):
        self.sales = sales
        self.customers = customers

    
    def __str__(self):
        return (f'Store(sales={self.sales})')
    

    def register(self):
        # 1. Solicitar los datos del cliente
        if len(customers) > 0:
            choice = int(input(('Cliente registrado? (y/n) ')).strip().lower() == 'y')
            if choice:
                CustomerManagement.search()
            else:
                CustomerManagement.register()
        name = input('Introduzca el nombre del cliente: ').strip()
        id = input('Introduzca la cédula o RIF del cliente: ').strip()
        email = input('Introduzca el correo electrónico del cliente: ').strip()
        address = input('Introduzca la dirección del cliente: ').strip()

    
    
    def search(self):
        pass


    def menu(self):
        while True:
            print("1. Registrar pago")
            print("2. Buscar pago")
            print("3. Volver")
            choice = int(input("Seleccione una opción: "))
            if choice == 1:
                self.register()
            elif choice == 2:
                self.search()
            elif choice == 3:
                break
            else:
                print("Opción no válida, por favor intente de nuevo.")
