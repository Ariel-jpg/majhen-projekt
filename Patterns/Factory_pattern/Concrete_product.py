from .Product import Product

class Cactus (Product):
    def __init__(self) -> None:
        self.name = "Cactus"
        self.price = 300

    def operation(self) -> str:
        return self.name

    def return_price_with_iva(self):
        return self.price + 40

class Notebook (Product):
    def __init__(self) -> None:
        self.name = "Notebook"
        self.price = 1000

    def operation(self) -> str:
        return self.name

    def return_price_with_iva(self):
        return self.price + 40

class Mouse (Product):
    def __init__(self) -> None:
        self.name = "Mouse"
        self.price = 100

    def operation(self) -> str:
        return self.name

    def return_price_with_iva(self):
        return self.price + 40