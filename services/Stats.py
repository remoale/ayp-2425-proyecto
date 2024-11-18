from services.Data import sales
from datetime import datetime

class Stats:
    # Informes de ventas
    # 1. Total de ventas
    def total_sales(self):
        sales_by_day = {}
        sales_by_week = {}
        sales_by_month = {}
        sales_by_year = {}

        for sale in sales:
            date_str = sale.payment.date
            date = datetime.strptime(date_str, '%Y-%m-%d')

            day = date.strftime('%Y-%m-%d')
            week = date.strftime('%Y-%U')
            month = date.strftime('%Y-%m')
            year = date.strftime('%Y')

            if day in sales_by_day:
                sales_by_day[day] += 1
            else:
                sales_by_day[day] = 1

            if week in sales_by_week:
                sales_by_week[week] += 1
            else:
                sales_by_week[week] = 1

            if month in sales_by_month:
                sales_by_month[month] += 1
            else:
                sales_by_month[month] = 1

            if year in sales_by_year:
                sales_by_year[year] += 1
            else:
                sales_by_year[year] = 1

        return {
            'daily': sales_by_day,
            'weekly': sales_by_week,
            'monthly': sales_by_month,
            'yearly': sales_by_year
        }

    
    # 2. Total de ventas por producto
    def total_sales_by_product(self):
        sales_by_product = {}
        for sale in sales:
            for product in sale.products:
                product_id = product.id
                if product_id in sales_by_product:
                    sales_by_product[product_id] += 1
                else:
                    sales_by_product[product_id] = 1

        sorted_sales_by_product = dict(sorted(sales_by_product.items(), key=lambda item: item.value, reverse=True))
        return sorted_sales_by_product


    # 3. Total de ventas por cliente
    def total_sales_by_customer(self):
        sales_by_customer = {}
        for sale in sales:
            customer_id = sale.customer.id
            if customer_id in sales_by_customer:
                sales_by_customer[customer_id] += 1
            else:
                sales_by_customer[customer_id] = 1

        sorted_sales_by_customer = dict(sorted(sales_by_customer.items(), key=lambda item: item[1], reverse=True))
        return sorted_sales_by_customer


    # Informes de pagos
    # 1. Total de pagos
    def total_payments(self):
        payments_by_day = {}
        payments_by_week = {}
        payments_by_month = {}
        payments_by_year = {}

        for sale in sales:
            date_str = sale.payment.date
            date = datetime.strptime(date_str, '%Y-%m-%d')

            day = date.strftime('%Y-%m-%d')
            week = date.strftime('%Y-%U')
            month = date.strftime('%Y-%m')
            year = date.strftime('%Y')

            total = sale['summary']['total']

            if day in payments_by_day:
                payments_by_day[day] += total
            else:
                payments_by_day[day] = total

            if week in payments_by_week:
                payments_by_week[week] += total
            else:
                payments_by_week[week] = total

            if month in payments_by_month:
                payments_by_month[month] += total
            else:
                payments_by_month[month] = total

            if year in payments_by_year:
                payments_by_year[year] += total
            else:
                payments_by_year[year] = total

        return {
            'Día': payments_by_day,
            'Semana': payments_by_week,
            'Mes': payments_by_month,
            'Año': payments_by_year
        }

    # 2. Total de pagos por cliente
    def total_payments_by_customer(self):
        payments_by_customer = {}
        for sale in sales:
            customer_id = sale.customer.id
            total = sale.summary['total']
            if customer_id in payments_by_customer:
                payments_by_customer[customer_id] += total
            else:
                payments_by_customer[customer_id] = total

        sorted_payments_by_customer = dict(sorted(payments_by_customer.items(), key=lambda item: item[1], reverse=True))
        return sorted_payments_by_customer


    # Informes de envíos
    # 1. Total de envíos
    def total_shipments(self):
        shipments_by_day = {}
        shipments_by_week = {}
        shipments_by_month = {}
        shipments_by_year = {}

        for sale in sales:
            date_str = sale.payment.date
            date = datetime.strptime(date_str, '%Y-%m-%d')

            day = date.strftime('%Y-%m-%d')
            week = date.strftime('%Y-%U')
            month = date.strftime('%Y-%m')
            year = date.strftime('%Y')

            if day in shipments_by_day:
                shipments_by_day[day] += 1
            else:
                shipments_by_day[day] = 1

            if week in shipments_by_week:
                shipments_by_week[week] += 1
            else:
                shipments_by_week[week] = 1

            if month in shipments_by_month:
                shipments_by_month[month] += 1
            else:
                shipments_by_month[month] = 1

            if year in shipments_by_year:
                shipments_by_year[year] += 1
            else:
                shipments_by_year[year] = 1

        return {
            'Día': shipments_by_day,
            'Semana': shipments_by_week,
            'Mes': shipments_by_month,
            'Año': shipments_by_year
        }


    # 2. Productos más enviados
    def most_shipped_products(self):
        shipments_by_product = {}
        for sale in sales:
            for product in sale.products:
                product_id = product.id
                if product_id in shipments_by_product:
                    shipments_by_product[product_id] += 1
                else:
                    shipments_by_product[product_id] = 1

        sorted_shipments_by_product = dict(sorted(shipments_by_product.items(), key=lambda item: item[1], reverse=True))
        return sorted_shipments_by_product


    # 3. Clientes con envíos pendientes
    def customers_with_pending_shipments(self):
        pending_shipments_by_customer = {}
        for sale in sales:
            if sale.shipping is None:
                customer_id = sale.customer.id
                if customer_id in pending_shipments_by_customer:
                    pending_shipments_by_customer[customer_id] += 1
                else:
                    pending_shipments_by_customer[customer_id] = 1

        sorted_pending_shipments_by_customer = dict(sorted(pending_shipments_by_customer.items(), key=lambda item: item[1], reverse=True))
        return sorted_pending_shipments_by_customer


    def menu(self):
        while True:
            print("Seleccione una opción:")
            print("1. Total de ventas")
            print("2. Total de ventas por producto")
            print("3. Total de ventas por cliente")
            print("4. Total de pagos")
            print("5. Total de pagos por cliente")
            print("6. Total de envíos")
            print("7. Productos más enviados")
            print("8. Clientes con envíos pendientes")
            print("9. Volver")

            option = input("Ingrese el número de la opción deseada: ")

            if option == '1':
                print(self.total_sales())
            elif option == '2':
                print(self.total_sales_by_product())
                break
            elif option == '3':
                print(self.total_sales_by_customer())
                break
            elif option == '4':
                print(self.total_payments())
                break
            elif option == '5':
                print(self.total_payments_by_customer())
                break
            elif option == '6':
                print(self.total_shipments())
                break
            elif option == '7':
                print(self.most_shipped_products())
                break
            elif option == '8':
                print(self.customers_with_pending_shipments())
                break
            elif option == '9':
                return
            else:
                print("Opción no válida. Intente de nuevo.")
