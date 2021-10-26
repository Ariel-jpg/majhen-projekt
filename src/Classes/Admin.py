from .State.Reports_requests import Reports_requests
from .Friend_request import Friend_Request
from .State.Admins import Admins
from .Registration import Registration

class Admin:
    def __init__(self, name, _id, password) -> None:
        # self.id_ = generate_id() utils method
        self.id_ = _id
        self.name = name
        self.blocked = False

        # self.password = generate_password()
        self.password = password

    def get_id(self):
        return self.id_

    def block_admin(self, admin_id) -> None:
        if Admins.validate_admin(self.id_):
            Admins.block_admin(admin_id)
        else:
            return  # Check

    def unblock_admin(self, admin_id) -> None:
        if Admins.validate_admin(self.id_):
            Admins.unblock_admin(admin_id)
        else:
            print("No fue posible desbloquear al administrador. Corrobore sus permisos y si el administrador existe e intentelo de nuevo")

            return  # Check

    def create_admin(self, name, _id, password) -> None:
        if Admins.validate_admin(self.id_):
            new_admin = Admin(name, _id, password)
            # Por entorno de ejecuión la solución es correcta
            Admins.add_admin(new_admin)

            return new_admin
        else:
            print("No fue posible crear al administrador. Corrobore sus permisos e intentelo de nuevo")

            return  # Check

    def delete_admin(self, admin_id) -> None:
        if Admins.validate_admin(self.id_):
            Admins.delete_admin(admin_id)
        else:
            print("No fue posible eliminar al administrador. Corrobore sus permisos y si el administrador existe e intentelo de nuevo")

            return  # Check

    def modify_admin(self, admin, name, password) -> None:  # Check method
        if Admins.validate_admin(self.id_):
            if name != "" and password != "":
                new_admin = Admin(name, admin.get_id(), password)
            elif name != "":
                new_admin = Admin(name, admin.get_id(), admin.password)
            else:
                new_admin = Admin(admin.name, admin.get_id(), password)

            return new_admin
        else:
            print(f"No fue posible modificar al administrador solicitado. Corrobore sus permisos y si el administrador existe e intentelo de nuevo")

            return  # Check

    def block_citizen(self, citizen, citizen_to_block_cuil):
        # This can be done in two ways:
        # 1: only admins can block citizens. (Chosen)
        # 2: only admins can access citizen methods to block.
        citizen.block_list.append(citizen_to_block_cuil)

    def unblock_citizen(self, citizen, citizen_to_unblock_cuil):
        # This can be done in two ways:
        # 1: only admins can unblock citizens. (Chosen)
        # 2: only admins can access citizen methods to unblock.
        citizen_unblock = Registration.registered_citizens[citizen_to_unblock_cuil]
        
        print(f"El usuario {citizen_unblock.name} {citizen_unblock.last_name} fue desbloqueado para el usuario {citizen.name} {citizen.last_name}. \nAcción ejecutada por el administrador: {self.name} \n")
        citizen.block_list.remove(citizen_to_unblock_cuil)

    def filter_friend_request(self, sender, reciever):
        if not reciever.exists_citizen_blocked(sender.get_cuil()):
            Friend_Request(sender, reciever, self)
        else:
            print(f"Usted se encuentra bloqueado para el usuario {reciever.name} {reciever.last_name} por lo que no es posible enviarle solicitudes de amistad.")
    
    # Sensor { type_event, ... }
    def receive_report_request(self, sensor):
        report_key = sensor.type_event
        
        Reports_requests.update_report_request(report_key)
        reports_number = Reports_requests.get_report_request(report_key)

        if reports_number > 20: pass 
            # Create and suscribe event