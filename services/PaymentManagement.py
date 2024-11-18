from services.Data import sales, customers
from services.CustomerManagement import CustomerManagement


class PaymentManagement:
    """
    Clase para la gestión de pagos en la tienda.

    Atributos:
    sales (list): Lista de ventas realizadas.
    customers (list): Lista de clientes registrados.

    Métodos:
    __init__(sales, customers): Inicializa los atributos sales y customers.
    __str__(): Devuelve una representación de texto de las ventas.
    register(): Registra un nuevo pago solicitando los datos del cliente.
    search(): Busca un pago registrado.
    menu(): Muestra el menú de opciones para la gestión de pagos.
    """

    def __init__(self):
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
        # 1. Filtrar
        filtered_payments = []
        print('Seleccione un filtro para buscar un pago:')
        print()
        option = None
        while option not in [1, 2, 3, 4]:
            print('1. Cliente\n2. Fecha\n3. Tipo de pago\n4. Moneda de pago\n')
            try:
                option = int(input('Seleccione una opción: '))
                if option not in [1, 2, 3, 4]:
                    print('Opción no válida, por favor seleccione una opción válida.')
            except ValueError:
                print('Entrada no válida, por favor introduzca un número.')
        if option == 1:
            id = input('Introduzca la cédula o RIF del cliente: ').strip()
            filtered_payments = [sale for sale in sales if sale.customer.id == id]
        elif option == 2:
            while True:
                try:
                    date = input('Introduzca la fecha: ')
                    break
                except ValueError:
                    print('Entrada no válida, por favor introduzca un número válido para el precio.')
            filtered_payments = [sale for sale in sales if sale.date == date]
        elif option == 3:
            payment = input('Introduzca el tipo de pago: ').strip().lower()
            filtered_payments = [sale for sale in sales if sale.payment == payment]
        elif option == 4:
            while True:
                try:
                    currency = int(input('Introduzca la moneda de pago: '))
                    break
                except ValueError:
                    print('Entrada no válida, por favor introduzca un número válido para la disponibilidad en inventario.')
            filtered_payments = [sale for sale in sales if sale.currency == currency]
        print()

        # 2. Mostrar resultados
        if len(filtered_payments) == 0:
            raise ValueError('No se encontraron pagos con los criterios dados')
        elif len(filtered_payments) == 1:
            print('\nVenta encontrada:', payment.date, '\n')
            payment = filtered_payments[0]
            return payment
        else:
            print('Se encontraron múltiples pagos:')
            for payment in filtered_payments:
                print(f'{payment.date}. {payment.customer.name}')      
            while True:
                try:
                    choice = int(input('\nSeleccione un pago: '))
                    if 1 <= choice <= len(filtered_payments):
                        payment = filtered_payments[choice - 1]
                        print('\nPago seleccionado:', payment.date, payment.customer.name, '\n')
                        return payment
                    else:
                        print('Opción no válida, por favor seleccione un número válido.')
                except ValueError:
                    print('Entrada no válida, por favor introduzca un número.')


    def menu(self):
        while True:
            print("1. Registrar pago")
            print("2. Buscar pago")
            print("3. Volver")
            choice = int(input("Seleccione una opción: "))
            if choice == 1:
                self.register()
                break
            elif choice == 2:
                self.search()
                break
            elif choice == 3:
                break
            else:
                print("Opción no válida, por favor intente de nuevo.")
