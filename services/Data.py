from requests import get

url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/products.json'
products = get(url).json()
sales = []
customers = []
