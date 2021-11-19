from Import_index import generate_id, generate_password
from .Event import Birthday_event,Party_event, Concert_event
from . import General_state

class Admin:
    def __init__(self, name) -> None:
        self.id_ = generate_id()
        self.name = name
        self.blocked = False

        self.password = generate_password()

    def get_id(self):
        return self.id_

    def create_admin(self):
        name_new_admin = input("Ingrese el nombre del nuevo administrador: ")

        General_state.get_admins_state().add_admin_to_list(name_new_admin)
    
    def block_admin(self, admin_id):
        
        print(f"El administrador {self.name} ha bloqueado a {General_state.admins_state.get_admin(admin_id).name}")

        General_state.get_admins_state().block_admin(admin_id)

    def load_sensor(self, sensor):
        General_state_ = General_state.General_state
        sensor_exists = False

        for _, sensor_ in General_state_.sensors.items():
            same_birthday_instances = (isinstance(sensor_.event, Birthday_event) and isinstance(sensor.event, Birthday_event))
            same_concert_instances = (isinstance(sensor_.event, Concert_event) and isinstance(sensor.event, Concert_event))
            same_party_instances = (isinstance(sensor_.event, Party_event) and isinstance(sensor.event, Party_event))

            if same_birthday_instances or same_concert_instances or same_party_instances:
                if sensor.get_event_description() == sensor_.get_event_description():
                    sensor_exists = True
        
        if sensor_exists:
            sensor_.update_concurrency(sensor.get_actual_concurrency())
        else:
            General_state_.load_sensor(sensor)
 
class Admin_dev (Admin):
    def __init__(self, id_, password, name) -> None:
        self.id_ = id_
        self.name = name
        self.blocked = False

        self.password = password