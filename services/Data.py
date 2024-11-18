from requests import get
from models.Product import Product

# Petición GET al archivo JSON con los productos
url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/products.json'
data = get(url).json()

# Crear una lista de objetos Product a partir de los datos obtenidos
products = [Product(**item) for item in data]

# Listas para almacenar los datos de nuevas ventas y clientes
sales = []
customers = []
