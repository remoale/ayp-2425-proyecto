from services.Data import sales
from models.Sale import Sale
from services.SalesManagement import SalesManagement

class ShippingManagement:
    def __init__(self, sales):
        self.sales = sales

    
    def __str__(self):
        return (f'Store(sales={self.sales})')
    

    def register(self):
        # 1. Solicitar orden de compra
        order = input('Introduzca la orden de compra: ').strip()

        # 2. Seleccionar servicio de envío
        print('Seleccione el método de envío:')
        shipping = int(input('1.Zoom\n2.Delivery por moto'))
        if shipping == 1:
            shipping = 'Zoom'
        else:
            shipping = 'Delivery por moto'

        # 3. En caso de que sea delivery agregar los datos del motorizado
        if shipping == 'Delivery por moto':
            moto_name = input('Introduzca el nombre del motorizado: ').strip()
            moto_id = input('Introduzca la cédula del motorizado: ').strip()
            moto_phone = input('Introduzca el número de teléfono del motorizado: ').strip()

        # 4. Costo del servicio
        #for sale in sales:
        cost = SalesManagement.search()
        shipping_cost = cost * 0.10
        print(f'El costo del envío es: {shipping_cost}')

    
    
    def search(self):
        pass


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
