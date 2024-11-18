from services.ProductManagement import ProductManagement
from services.SalesManagement import SalesManagement
from services.CustomerManagement import CustomerManagement
from services.PaymentManagement import PaymentManagement
from services.ShippingManagement import ShippingManagement
from services.Stats import Stats


def main():

    ProductManagement = ProductManagement()
    SalesManagement = SalesManagement()
    CustomerManagement = CustomerManagement()
    PaymentManagement = PaymentManagement()
    ShippingManagement = ShippingManagement()
    Stats = Stats()

    while True:
        print("Tienda en línea de productos para vehículos 🚗")
        print("Seleccione una opción:")
        print("1. Gestión de Productos")
        print("2. Gestión de Ventas")
        print("3. Gestión de Clientes")
        print("4. Gestión de Pagos")
        print("5. Gestión de Envíos")
        print("6. Estadísticas")
        print("7. Salir")

        option = int(input("Ingrese el número de la opción deseada: "))

        if option == 1:
            ProductManagement.menu()
        elif option == 2:
            SalesManagement.menu()
        elif option == 3:
            CustomerManagement.menu()
        elif option == 4:
            PaymentManagement.menu()
        elif option == 5:
            ShippingManagement.menu()
        elif option == 6:
            Stats.menu()
        elif option == 7:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")


if __name__ == '__main__':
    main()