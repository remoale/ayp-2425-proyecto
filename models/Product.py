class Product:
    def __init__(self, id: int, name: str, price: float, description: str,
                 category: str, inventory: int, compatible_vehicles: list[str]):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.category = category
        self.inventory = inventory
        self.compatible_vehicles = compatible_vehicles
    

    def __str__(self):
        return (f'Product(id={self.id}, name={self.name}, price={self.price}, '
            f'description={self.description}, category={self.category}, '
            f'inventory={self.inventory}, compatible_vehicles={self.compatible_vehicles})')