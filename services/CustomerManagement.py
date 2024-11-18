from services.Data import customers
from models.Customer import Customer

class CustomerManagement:
    def __init__(self, customers):
        self.customers = customers

    
    def __str__(self):
        return (f'Store(customers={self.customers})')
    

    def register(self):
        name = input('Introduzca el nombre del cliente: ').strip()
        id = input('Introduzca la cédula o RIF del cliente: ').strip()
        email = input('Introduzca el correo electrónico del cliente: ').strip()
        address = input('Introduzca la dirección del cliente: ').strip()
        phone = input('Introduzca el número de teléfono del cliente: ').strip()
        legal = input('¿El cliente es una persona jurídica? (y/n) ').strip().lower() == 'y'
        customer = Customer(name, id, email, address, phone, legal)
        if legal:
            legal_name = input('Nombre de la persona de contacto: ').strip()
            legal_phone = input('Teléfono de la persona de contacto: ').strip()
            legal_email = input('Correo electrónico de la persona de contacto: ').strip()
            customer.legal_name = legal_name
            customer.legal_phone = legal_phone
            customer.legal_email = legal_email
        self.customers.append(customer)
        print('Cliente registrado exitosamente.')
    

    def modify(self, customer):
        id = input('Introduzca la cédula o RIF del cliente a eliminar: ').strip()
        if id in [customer.id for customer in self.customers]:
            print('Seleccione el campo a modificar:', '1. Nombre', '2. Cédula/RIF',
                '3. Correo electrónico', '4. Dirección', '5. Teléfono',
                '6. Persona jurídica', sep='\n')
            choice = None
            while choice not in [1, 2, 3, 4, 5, 6]:
                choice = int(input(''))
            if choice == 1:
                customer.name = input('Introduzca el nuevo nombre: ').strip()
            elif choice == 2:
                customer.id = input('Introduzca la nueva cédula o RIF: ').strip()
            elif choice == 3:
                customer.email = input('Introduzca el nuevo correo electrónico: ').strip()
            elif choice == 4:
                customer.address = input('Introduzca la nueva dirección: ').strip()
            elif choice == 5:
                customer.phone = input('Introduzca el nuevo teléfono: ').strip()
            else:
                customer.legal = input('¿El cliente es una persona jurídica? (y/n) ').strip().lower() == 'y'
                if customer.legal:
                    legal_name = input('Nombre de la persona de contacto: ').strip()
                    legal_phone = input('Teléfono de la persona de contacto: ').strip()
                    legal_email = input('Correo electrónico de la persona de contacto: ').strip()
                    customer.legal_name = legal_name
                    customer.legal_phone = legal_phone
                    customer.legal_email = legal_email
                else:
                    customer.legal_name = None
                    customer.legal_phone = None
                    customer.legal_email = None
            for i in range(len(self.customers)):
                if self.customers[i].id == id:
                    self.customers[i] = customer
            print('Cliente modificado exitosamente.')
            return
        print('Cliente no encontrado.')


    def delete(self):
        id = input('Introduzca la cédula o RIF del cliente a eliminar: ').strip()
        for customer in self.customers:
            if customer.id == id:
                self.customers.remove(customer)
                print('Cliente eliminado exitosamente.')
                return
        print('Cliente no encontrado.')

    
    def search(self):
        id = input('Introduzca la cédula o RIF del cliente a buscar: ').strip()
        for customer in self.customers:
            if customer.id == id:
                print(customer)
                return customer
        print('Cliente no encontrado.')

    
    def menu(self):
        while True:
            print('1. Registrar cliente', '2. Modificar cliente', '3. Eliminar cliente',
                  '4. Buscar cliente', '5. Volver', sep='\n')
            option = None
            while option not in [1, 2, 3, 4]:
                option = int(input(''))
            if option == 1:
                self.register()
            elif option == 2:
                customer = self.search()
                self.modify(customer)
            elif option == 3:
                self.delete()
            elif option == 4:
                self.search()
            else:
                break
            return
