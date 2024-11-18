from models.Product import Product
from services.Data import products

class ProductManagement:
    def __init__(self):
        self.products = products

    
    def __str__(self):
        return (f'Store(products={self.products})')
    

    def add_product(self):
        category = input('Introduzca la categoría del producto: ').strip()
        try:
            price = float(input('Introduzca el precio del producto: '))
        except ValueError:
            print('Entrada no válida, por favor introduzca un número válido para el precio.')
            return
        name = input('Introduzca el nombre del producto: ').strip()
        try:
            inventory = int(input('Introduzca la disponibilidad en inventario del producto: '))
        except ValueError:
            print('Entrada no válida, por favor introduzca un número válido para la disponibilidad en inventario.')
            return
        optional = input('Opcional: modelo de vehículos para los cual aplica (y/n): ').strip().lower()
        compatible_vehicles = []
        if optional == 'y':
            compatible_vehicles = input('Introduzca los modelos de vehículos separados por coma: ').strip().split(',')
        product = Product(category=category, price=price, name=name, inventory=inventory, compatible_vehicles=compatible_vehicles)
        self.products.append(product)
        return
            
    
    def search_product(self):
        filtered_products = []
        print('Seleccione la opción por la que desea filtrar:')
        option = None
        while option not in [1, 2, 3, 4]:
            option = int(input('1. Categoría\n2. Precio\n3. Nombre\n4. Disponibilidad en inventario\n'))
            if option not in [1, 2, 3, 4]:
                print('Opción no válida, por favor seleccione una opción válida.')
        if option == 1:
            category = input('Introduzca la categoría: ').strip()
            filtered_products = [product for product in self.products if product.category == category]
        elif option == 2:
            price = float(input('Introduzca el precio: '))
            filtered_products = [product for product in self.products if product.price == price]
        elif option == 3:
            name = input('Introduzca el nombre: ').strip()
            filtered_products = [product for product in self.products if product.name == name]
        elif option == 4:
            inventory = int(input('Introduzca la disponibilidad en inventario: '))
            filtered_products = [product for product in self.products if product.inventory == inventory]
        
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
    

    def modify_product(self):
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
    

    def remove_product(self):
        # 1. Buscar el producto
        name = input('Introduzca el nombre del producto a modificar: ').strip()
        product_to_remove = self.search_product(name)

        # 2. Eliminar el producto de la lista
        self.products.remove(product_to_remove)
        return


    def menu(self):
        option = None
        while option not in [1, 2, 3, 4, 5]:
            option = int(input('1. Agregar producto\n2. Modificar producto\n3. Buscar producto\n4. Eliminar producto\n5. Volver'))
            if option not in [1, 2, 3, 4, 5]:
                print('Opción no válida, por favor seleccione una opción válida.')
        if option == 1:
            self.add_product()
        elif option == 2:
            self.modify_product()
        elif option == 3:
            self.search_product()
        elif option == 4:
            self.remove_product()
        return
