from .Creator import Creator
from .Concrete_product import Cactus, Mouse, Notebook

class Create_Cactus (Creator):
    def __init__(self) -> None:
        super().__init__()

        self.name = "Cactus Created"

    def factory_method(self):
        print(self.AnOperation())
        return Cactus()

class Create_Mouse (Creator):
    def factory_method(self):
        print(self.AnOperation())
        return Mouse()

class Create_Notebook (Creator):
    def factory_method(self):
        print(self.AnOperation())
        return Notebook()