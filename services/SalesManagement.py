from models.Shipping import Shipping
from models.Sale import Sale
from services.ProductManagement import ProductManagement
from services.CustomerManagement import CustomerManagement
from services.ShippingManagement import ShippingManagement
from services.Data import products, sales, customers
from datetime import datetime
from random import randint


class SalesManagement:
    """
    Clase para la gestión de ventas en la tienda.

    Atributos:
    sales (list): Lista de ventas realizadas.
    customers (list): Lista de clientes registrados.

    Métodos:
    __init__(sales, customers): Inicializa los atributos sales y customers.
    __str__(): Devuelve una representación de texto de las ventas.
    register(): Registra una nueva venta solicitando los datos necesarios.
    search(): Busca una venta registrada.
    invoice(): Genera una factura para una venta registrada.
    menu(): Muestra el menú de opciones para la gestión de ventas.
    """

    def __init__(self):
        self.products = products
        self.sales = sales
        self.customers = customers

    
    def __str__(self):
        return (f'Store(sales={self.sales})')
    

    def register(self):
        date = datetime.now()

        # 1. Solicitar los datos del cliente
        print('Datos del cliente:')
        while True:
            choice = input('Es cliente registrado? (y/n) ').strip().lower() == 'y'
            customer = None
            if choice:
                id = int(input('Introduzca cédula o RIF: '))
                try:
                    customer = [customer for customer in self.customers if customer.id == id][0]
                    break
                except IndexError:
                    print('El cliente no se encuentra registrado')
            if not choice or customer is None:
                customer = CustomerManagement().register()
                break

        # 2. Solicitar los productos vendidos
        sold_products = {}
        choice = 'y'
        while choice == 'y':
            product = ProductManagement().search()
            quantity = int(input('Introduzca la cantidad del producto comprado: '))
            sold_products[f'{product.name}'] = quantity
            choice = input('¿Desea agregar otro producto? (y/n) ').strip().lower()
        

        # 3. Solicitar el método de pago
        print('\n1. Punto de venta', '2. Pago móvil', '3. Transferencia',
              '4. Zelle', '5. PayPal', '6. Efectivo:\n', sep='\n')
        choice = None
        while choice not in [1, 2, 3, 4, 5, 6]:
            choice = int(input('Seleccione el método de pago: '))
            if choice == 1:
                payment = 'Punto de venta'
            elif choice == 2:
                payment = 'Pago móvil'
            elif choice == 3:
                payment = 'Transferencia'
            elif choice == 4:
                payment = 'Zelle'
            elif choice == 5:
                payment = 'PayPal'
            else:    
                choice = 'Efectivo'

        # 4. Definir el envío
        shipping = ShippingManagement().register()

        # 5. Resumen de la venta
        print('Total de compra:')
        subtotal = 0
        for key, value in sold_products.items():
            for product in self.products:
                if product.name == key:
                    subtotal += product.price * value
        print('Subtotal: ', subtotal)

        # 6. Solicitar monto de pago
        payment_amount = float(input('Introduzca el monto a pagar: '))

        # 5% de descuento si el cliente es jurídico y paga de contado
        discount = 0
        if customer.legal and payment_amount == subtotal:
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

        # Summary
        summary = {'subtotal': subtotal, 'descuentos': discount, 'tax': tax, 'igtf': igtf, 'total': total}

        sale = Sale(customer, products, payment, shipping,
                    {'subtotal': subtotal, 'descuentos': discount, 'tax': tax, 'igtf': igtf, 'total': total},
                    summary=summary)
        self.sales.append(sale)
        print('Venta registrada con éxito!\n')
        self.invoice(sale)
        

    def invoice(self, sale):
        invoice = randint(100000, 1000000)
        sale.invoice = invoice
        print(f'\nFactura: {invoice}')

        # Fecha de emisión
        date = datetime.now()
        print(f'Fecha de emisión: {date}')

        # Monto a pagar
        print(f'Subtotal: {sale.summary["subtotal"]}')
        print(f'Descuentos: {sale.summary["descuentos"]}')
        print(f'IVA: {sale.summary["tax"]}')
        print(f'IGTF: {sale.summary["igtf"]}')
        print(f'Total: {sale.summary["total"]}')

        # Si el cliente es una persona jurídica, se podrá realizar compras a crédito (pago en 15 o 30 días)
        # Si el cliente es natural su factura se realizará para compras en el momento
        if sale.customer.legal:
            # Términos de pago
            term = randint(0, 1)
            if term == 0:
                term = 15
            else:
                term = 30
            print(f'Términos de pago: Tiene un plazo de {term} días desde la emisión de la factura para realizar el pago.')
        
        print('Gracias por su compra!')


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
            print('1. Registrar venta')
            print('2. Consultar venta')
            print('3. Generar factura')
            print('4. Volver')
            print()
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
