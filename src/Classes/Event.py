from abc import ABC, abstractclassmethod

from Import_index import generate_id

class Coordinates:
    def __init__(self, latitude: str, longitude: str) -> None:
        self.latitude = latitude 
        self.longitude = longitude 

    def get_coordinates(self):
        coordinates = [self.latitude, self.longitude]

        return coordinates

class Events (ABC, Coordinates):
    def __init__(self, latitude: str, longitude: str, descripcion: str) -> None:
        super().__init__(latitude, longitude)
        self.descripcion = descripcion
        self.friend = False
        self.concurrency = 1
        self._id = generate_id()
        
    @abstractclassmethod
    def get_type_event_str(self) -> str:
        pass

    def add_friend(self, friend):
        self.friend = friend
        self.concurrency = 2

    def get_concurrency(self):
        return self.concurrency

    def get_description(self) -> str:
        return self.descripcion

# Type Events

class Birthday_event (Events):
    def __init__(self, latitude, longitude, descripcion) -> None:
        super().__init__(latitude, longitude, descripcion)

    def get_type_event_str(self):
        return "Birthday"

class Concert_event (Events):
    def __init__(self, latitude, longitude, descripcion) -> None:
        super().__init__(latitude, longitude, descripcion)

    def get_type_event_str(self):
        return "Concert"

class Party_event (Events):
    def __init__(self, latitude, longitude, descripcion) -> None:
        super().__init__(latitude, longitude, descripcion)

    def get_type_event_str(self):
        return "Party"