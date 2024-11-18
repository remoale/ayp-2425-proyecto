from services.Data import sales
from models.Shipping import Shipping
from random import randint

class ShippingManagement:
    """
    Clase para la gestión de envíos en la tienda.

    Atributos:
    sales (list): Lista de ventas realizadas.

    Métodos:
    __init__(sales): Inicializa los atributos de la clase.
    __str__(): Devuelve una representación de texto de las ventas.
    register(): Registra un nuevo envío solicitando los datos necesarios.
    search(): Busca un envío registrado.
    menu(): Muestra el menú de opciones para la gestión de envíos.
    """

    def __init__(self):
        self.sales = sales

    
    def __str__(self):
        return (f'Store(sales={self.sales})')
    

    def register(self):
        # 1. Solicitar orden de compra
        order = None
        while order not in [sale.invoice for sale in sales]:
            order = input('Introduzca la orden de compra: ').strip()
            if order not in [sale.invoice for sale in sales]:
                print('Orden de compra no encontrada, por favor introduzca una orden válida.')

        # 2. Seleccionar servicio de envío
        print('\n1. Zoom\n2. Delivery\n')
        service = int(input('Seleccione el servicio de envío: '))
        if service == 1:
            service = 'Zoom'
        else:
            service = 'Delivery'
        order = input('Introduzca la orden de compra: ')

        # 3. Costo del servicio
        shipping_cost = randint(10, 50)
        shipping = Shipping(order, service, shipping_cost)

        # 4. En caso de que sea delivery agregar los datos del motorizado
        if service == 'Delivery':
            shipping.moto_name = input('Introduzca el nombre del motorizado: ').strip()
            shipping.moto_id = input('Introduzca la cédula del motorizado: ').strip()
            shipping.moto_phone = input('Introduzca el número de teléfono del motorizado: ').strip()

        return shipping

    
    def search(self):
        # 1. Filtrar
        filtered_shippings = []
        print('Seleccione un filtro para buscar un envío:')
        print()
        option = None
        while option not in [1, 2]:
            print('1. Cliente\n2. Fecha\n')
            try:
                option = int(input('Seleccione una opción: '))
                if option not in [1, 2]:
                    print('Opción no válida, por favor seleccione una opción válida.')
            except ValueError:
                print('Entrada no válida, por favor introduzca un número.')
        if option == 1:
            id = input('Introduzca la cédula o RIF del cliente: ').strip()
            filtered_shippings = [sale.shipping for sale in sales if sale.customer.id == id]
        elif option == 2:
            while True:
                try:
                    date = input('Introduzca la fecha: ')
                    break
                except ValueError:
                    print('Entrada no válida, por favor introduzca un número válido para el precio.')
            filtered_shippings = [sale for sale in sales if sale.date == date]
        print()

        # 2. Mostrar resultados
        if len(filtered_shippings) == 0:
            raise ValueError('No se encontraron pagos con los criterios dados')
        elif len(filtered_shippings) == 1:
            print('\nEnvío encontrado:', payment.date, '\n')
            payment = filtered_shippings[0]
            return payment
        else:
            print('Se encontraron múltiples pagos:')
            for payment in filtered_shippings:
                print(f'{payment.date}. {payment.customer.name}')      
            while True:
                try:
                    choice = int(input('\nSeleccione un pago: '))
                    if 1 <= choice <= len(filtered_shippings):
                        payment = filtered_shippings[choice - 1]
                        print('\nPago seleccionado:', payment.date, payment.customer.name, '\n')
                        return payment
                    else:
                        print('Opción no válida, por favor seleccione un número válido.')
                except ValueError:
                    print('Entrada no válida, por favor introduzca un número.')


    def menu(self):
        print('1. Registrar envío')
        print('2. Consultar envío')
        print('3. Volver')
        option = int(input('Ingrese el número de la opción deseada: '))
        if option == 1:
            self.register()
        elif option == 2:
            self.search()
        elif option == 3:
            return
        else:
            print('Opción no válida, por favor intente de nuevo.')
