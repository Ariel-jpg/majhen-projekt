from .Event import Event_with_friend, Normal_Event
from .Sensor import Sensor
from .State.Admins import Admins
        
class Citizen:
    def __init__(self, name, last_name, phone_number, cuil) -> None:
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.cuil = cuil

        self.friend_list = dict()
        self.rejections_list = dict()
        self.block_list = list()
    
    def __str__(self) -> str:
        return f"- name: {self.name} \n- last_name: {self.last_name} \n- phone_number: {self.phone_number} \n- cuil: {self.cuil}\n"

    def get_cuil(self) -> str:
        return self.cuil

    def get_formatted_data(self) -> dict:
        formatted_data = dict({
            "name": self.name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "cuil": self.cuil,
        })

        return formatted_data

    # Friend_list = Citizen Object
    # Rejections_list = Citizen_cuil: { Citizen_cuil, rejections_counter }

    # c1 = sender
    # c2 = reciever 

    def send_friend_request(self, friend) -> None: # "Dispatcher" - c1 Method
        admin_in_charge = Admins.get_admin()
        admin_in_charge.filter_friend_request(self, friend)

    def recieve_friend_request(self, sender, friend_request) -> None: # "Listener" - c2 Method
        print(f"{self.name} {self.last_name} te llegó una solicitud de {sender.name} {sender.last_name}")

        response = input("Querés aceptar la solicitud y/n: ").lower()

        if response == "y":
            self.friend_list.update({ sender.get_cuil() : sender.get_formatted_data() })

            friend_request.accept_friend_request()
        else: 
            friend_request.reject_friend_request()
    
    def recieve_answer_friend_request(self, friend_request) -> None: # "Listener" - c1 Method
        accepted = friend_request.get_response()
        citizen = friend_request.reciever

        if accepted:
            friend = citizen

            self.friend_list.update({ friend.get_cuil() : friend.get_formatted_data() })
        else: 
            citizen_id = citizen.get_cuil()

            if bool(self.rejections_list.get(citizen_id)):
                rejections_counter = self.rejections_list.get(citizen_id)["rejections_counter"]
                rejections_counter += 1

                if rejections_counter == 5:
                    friend_request.admin_in_charge.block_citizen(citizen, self.cuil)

                    print(f"Usted fue bloqueado para el usuario {citizen.name} {citizen.last_name}. Motivo: 5 o más solicitudes de amistad rechazadas")
            else: 
                rejections_counter = 1

            self.rejections_list.update({ citizen_id: { "cuil": citizen_id, "rejections_counter": rejections_counter } })
    
    def exists_citizen_blocked(self, citizen_cuil) -> bool:
        return citizen_cuil in self.block_list
        
    def notify_event(self, type_event): # type_event : Type_event
        normal_event = Normal_Event(type_event)
        Sensor(normal_event)
    
    def notify_event_with_friend(self, type_event, friend):
        if self.friend_list.get(friend.cuil):
            event = Event_with_friend(type_event, friend, self)            
        else:
            print(f"El contacto {friend.name} {friend.last_name} no forma parte de su lista de amigos. Solo se creará el evento") # Check

            event = Normal_Event(type_event)
        
        Sensor(event)

    def recieve_friend_invitation(self, event):
        sender = event.sender
        print(f"{self.name} {self.last_name} te llego una invitacion a un evento {sender.name} {sender.last_name}")
        
        response = input("¿Vas a asistir? (y/n)").lower()
        
        if response == "y":
            Sensor(event)
            