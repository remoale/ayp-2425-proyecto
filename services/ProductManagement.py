from models.Product import Product
from services.Data import products


class ProductManagement:
    """
    Clase para la gestión de productos en la tienda.

    Atributos:
    products (list): Lista de productos disponibles.

    Métodos:
    __init__(): Inicializa los atributos de la clase.
    __str__(): Devuelve una representación en cadena de la tienda.
    add(): Agrega un nuevo producto a la lista.
    search(): Busca productos en la lista según diferentes criterios.
    modify(): Modifica la información de un producto existente.
    remove(): Elimina un producto de la lista.
    menu(): Muestra el menú de opciones para la gestión de productos.
    """

    def __init__(self):
        self.products = products

    
    def __str__(self):
        return (f'Store(products={self.products})')
    

    def add(self):
        name = input('Introduzca el nombre del producto: ').strip()
        price = None
        while price is None:
            try:
                price = float(input('Introduzca el precio del producto: '))
            except ValueError:
                print('Entrada no válida, por favor introduzca un número válido para el precio.')
        description = input('Introduzca la descripción del producto: ').strip()
        category = input('Introduzca la categoría del producto: ').strip()
        inventory = None
        while inventory is None:
            try:
                inventory = int(input('Introduzca la disponibilidad en inventario del producto: '))
            except ValueError:
                print('Entrada no válida, por favor introduzca un número válido para la disponibilidad en inventario.')
        optional = input('Opcional: modelo de vehículos para los cual aplica (y/n): ').strip().lower()
        compatible_vehicles = []
        if optional == 'y':
            compatible_vehicles = input('Introduzca los modelos de vehículos separados por coma: ').strip().split(',')
        id = len(self.products) + 1
        product = Product(id, name, price, description, category, inventory, compatible_vehicles)
        self.products.append(product)
        print()
        print('Producto agregado:', product.name)
        print()
    
    
    def search(self):
        # 1. Filtrar por categoría
        filtered_products = []
        print('Seleccione un filtro para buscar un producto:')
        print()
        option = None
        while option not in [1, 2, 3, 4]:
            print('1. Categoría\n2. Precio\n3. Nombre\n4. Disponibilidad en inventario\n')
            try:
                option = int(input('Seleccione una opción: '))
                if option not in [1, 2, 3, 4]:
                    print('Opción no válida, por favor seleccione una opción válida.')
            except ValueError:
                print('Entrada no válida, por favor introduzca un número.')
        if option == 1:
            category = input('Introduzca la categoría: ').strip()
            filtered_products = [product for product in self.products if product.category == category]
        elif option == 2:
            while True:
                try:
                    price = float(input('Introduzca el precio: '))
                    break
                except ValueError:
                    print('Entrada no válida, por favor introduzca un número válido para el precio.')
            filtered_products = [product for product in self.products if product.price == price]
        elif option == 3:
            name = input('Introduzca el nombre: ').strip().lower()
            filtered_products = [product for product in self.products if name in product.name.lower()]
        elif option == 4:
            while True:
                try:
                    inventory = int(input('Introduzca la disponibilidad en inventario: '))
                    break
                except ValueError:
                    print('Entrada no válida, por favor introduzca un número válido para la disponibilidad en inventario.')
            filtered_products = [product for product in self.products if product.inventory == inventory]
        print()

        # 2. Mostrar resultados
        if len(filtered_products) == 0:
            raise ValueError('No se encontraron productos con los criterios dados')
        elif len(filtered_products) == 1:
            print('\nProducto encontrado:', product.name, '\n')
            product = filtered_products[0]
            return product
        else:
            print('Se encontraron múltiples productos:')
            for product in filtered_products:
                print(f'{product.id}. {product.name}')      
            while True:
                try:
                    choice = int(input('\nSeleccione el ID del producto: '))
                    if choice in [product.id for product in self.products]:
                        for product in filtered_products:
                            if product.id == choice:
                                print('\nProducto seleccionado:', product.name, '\n')
                                return product
                    else:
                        print('Opción no válida, por favor seleccione un número válido.')
                except ValueError:
                    print('Entrada no válida, por favor introduzca un número.')
    

    def modify(self):
        # 1. Buscar el producto
        name = input('Introduzca el nombre del producto a modificar: ').strip()
        product_to_modify = self.search_product(name)

        # 2. Introducir la información a modificar
        print('Seleccione la información que desea modificar:')
        option = None
        while option not in [1, 2, 3, 4]:
            option = int(input('1. Categoría\n2. Precio\n3. Nombre\n4. Disponibilidad en inventario\n'))
            if option not in [1, 2, 3, 4]:
                print('Opción no válida, por favor seleccione una opción válida.')
        if option == '1':
            product_to_modify.category = input('Introduzca la nueva categoría: ').strip()
        elif option == '2':
            try:
                product_to_modify.price = float(input('Introduzca el nuevo precio: '))
            except ValueError:
                print('Entrada no válida, por favor introduzca un número válido para el precio.')
                return
        elif option == '3':
            product_to_modify.name = input('Introduzca el nuevo nombre: ').strip()
        elif option == '4':
            try:
                product_to_modify.inventory = int(input('Introduzca la nueva disponibilidad en inventario: '))
            except ValueError:
                print('Entrada no válida, por favor introduzca un número válido para la disponibilidad en inventario.')
                return
            
        # 3. Modificar el producto en la lista
        for i, product in enumerate(self.products):
            if product.id == product_to_modify.id:
                self.products[i] = product_to_modify
                return
        raise ValueError('Producto no encontrado')
    

    def remove(self):
        # 1. Buscar el producto
        product_to_remove = self.search_product()

        # 2. Eliminar el producto de la lista
        self.products.remove(product_to_remove)
        return


    def menu(self):
        option = None
        while option not in [1, 2, 3, 4, 5]:
            print('1. Agregar producto', '2. Modificar producto',
                  '3. Buscar producto', '4. Eliminar producto', '5. Volver', '', sep='\n')
            option = int(input('Seleccione una opción: '))
            print()
            if option not in [1, 2, 3, 4, 5]:
                print('Opción no válida, por favor seleccione una opción válida.')
        if option == 1:
            self.add()
        elif option == 2:
            self.modify()
        elif option == 3:
            self.search()
        elif option == 4:
            self.remove()
        return
