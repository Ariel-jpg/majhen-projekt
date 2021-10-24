from abc import ABC, abstractmethod

class Creator (ABC):
    @abstractmethod
    def factory_method(self):
        pass
        
    def AnOperation(self) -> str:
        return f"Su producto ha sido creado con éxito. Ha creado un {self.name}" # Self is an Creator_concrete instace
    