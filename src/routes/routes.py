from src.fetchParameter.fetchparameter import Fetchparameters
from src.products.product import Product

class Routes:
    @staticmethod
    def addproduct(request):
        fetch_params = Fetchparameters()
        category = fetch_params.fetch_parameter(request, 'category', type=str)
        quantity = fetch_params.fetch_parameter(request, 'quantity', type=int)
        productName = fetch_params.fetch_parameter(request, 'productName', type=int)
        costPrice = fetch_params.fetch_parameter(request, 'costPrice', type=int)
        sellingPrice = fetch_params.fetch_parameter(request, 'sellingPrice', type=int)
        manufacturingDate = fetch_params.fetch_parameter(request, 'manufacturingDate', type=str)  # Change type as needed
        expiryDate = fetch_params.fetch_parameter(request, 'expiryDate', type=str)  # Change type as needed
        result = Product().save_product(category, quantity, productName, costPrice, sellingPrice, manufacturingDate, expiryDate)
        return result


    @staticmethod
    def update_product(request):
        fetch_params = Fetchparameters()
        id = fetch_params.fetch_parameter(request, 'id', type=int)
        name = fetch_params.fetch_parameter(request, 'name', type=str)
        qty = fetch_params.fetch_parameter(request, 'qty', type=int)
        amount = fetch_params.fetch_parameter(request, 'amount', type=int)
        result = Product().update_product(id, name, qty,amount)
        return result

    @staticmethod
    def get_products():
        return Product.get_products()



