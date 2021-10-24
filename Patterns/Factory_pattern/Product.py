from abc import ABC, abstractmethod

class Product (ABC):  
    @abstractmethod
    def operation(self) -> str:
        pass

    @abstractmethod
    def return_price_with_iva():
        pass
