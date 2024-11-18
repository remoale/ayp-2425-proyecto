from models.Product import Product
from models.Customer import Customer
from services.ProductManagement import ProductManagement
from services.Data import products, sales, customers

class SalesManagement:
    def __init__(self, sales, customers):
        self.sales = sales
        self.customers = customers

    
    def __str__(self):
        return (f'Store(sales={self.sales})')
    

    def register(self):
        # 1. Solicitar los datos del cliente
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

        # 2. Solicitar los productos vendidos
        products = []
        while choice != 'n':
            product = ProductManagement.search_product()
            quantity = int(input('Introduzca la cantidad del producto comprado: '))
            for i in range(quantity):
                products.append((product, quantity))
            choice = input('¿Desea agregar otro producto? (y/n) ').strip().lower()

        # 3. Solicitar el método de pago
        print('Seleccione el método de pago:',
            '1. Punto de venta\n2. Pago móvil\n3. Transferencia\n4. Zelle\n5. PayPal\n6. Efectivo:')
        payment = None
        while payment not in [1, 2, 3, 4, 5, 6]:
            payment = int(input(''))
            if payment == 1:
                payment = 'Punto de venta'
            elif payment == 2:
                payment = 'Pago móvil'
            elif payment == 3:
                payment = 'Transferencia'
            elif payment == 4:
                payment = 'Zelle'
            elif payment == 5:
                payment = 'PayPal'
            else:    
                payment = 'Efectivo'

        # 4. Solicitar el método de envío
        print('Seleccione el método de envío:')
        shipping = int(input('1.Zoom\n2.Delivery'))
        if shipping == 1:
            shipping = 'Zoom'
        else:
            shipping = 'Delivery'

        # 5. Resumen de la venta
        print('Total de compra:')
        subtotal = sum([product.price for product, quantity in products])
        print('Subtotal: ', subtotal)

        # Descuento
        discount = 0
        if customer.legal: # and payment_amount == subtotal
            discount = subtotal * 0.05
            print('Descuento: ', discount)
            subtotal -= discount
        
        # IVA (16%)
        tax = subtotal * 0.16
        print('IVA: ', tax)

        # IGTF (3%)
        igtf = subtotal * 0.03
        print('IGTF: ', igtf)

        # Total
        total = subtotal + tax + igtf - discount
    

    def invoice(self):
        # Si el cliente es una persona jurídica, se podrá realizar compras a crédito (pago en 15 o 30 días)
        # Si el cliente es una persona natural, se deberá realizar el pago al momento de la compra 
        pass


    def search(self):
        filtered_products = []
        print('Seleccione la opción por la que desea filtrar:')
        option = None
        while option not in [1, 2]:
            option = int(input('1. Cliente\n2. Fecha de la venta\n'))
            if option not in [1, 2]:
                print('Opción no válida, por favor seleccione una opción válida.')
        if option == 1:
            id = input('Introduzca el ID del cliente: ').strip()
            filtered_products = [customer for customer in self.customers if customer.id == id]
        elif option == 2:
            date = float(input('Introduzca la fecha de la venta ("YYYY-MM-DD"): '))
            filtered_products = [sale for sale in self.sales if sale.date == date]
 
        if len(filtered_products) == 0:
            raise ValueError('No se encontraron productos con los criterios dados')
        elif len(filtered_products) == 1:
            product = filtered_products[0]
        else:
            print('Se encontraron múltiples productos:')
            for product in filtered_products:
                print(f'{product.id}. {product.name}')      
            while True:
                try:
                    choice = int(input('Seleccione el ID del producto: '))
                    if choice in [product.id for product in self.products]:
                        for product in filtered_products:
                            if product.id == choice:
                                return product
                    else:
                        print('Opción no válida, por favor seleccione un número válido.')
                except ValueError:
                    print('Entrada no válida, por favor introduzca un número.')


    def menu(self):
        while True:
            print('Seleccione una opción:')
            print('1. Registrar venta')
            print('2. Consultar venta')
            print('3. Generar factura')
            print('4. Volver')
            option = int(input('Ingrese el número de la opción deseada: '))
            if option == 1:
                self.register()
            elif option == 2:
                self.search()
            elif option == 3:
                self.invoice()
            elif option == 4:
                break
            else:
                print('Opción no válida, por favor intente de nuevo.')
