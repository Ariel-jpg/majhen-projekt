from .Concrete_creator import Create_Cactus, Create_Mouse, Create_Notebook
from .Product import Product

class Factory:
    def __init__(self) -> None:
        pass

    def create_product(product_code: str) -> Product:
        product_code = product_code.lower()

        if product_code == "cactus": return Create_Cactus().factory_method()
        if product_code == "notebook": return Create_Notebook().factory_method()
        if product_code == "mouse": return Create_Mouse().factory_method()