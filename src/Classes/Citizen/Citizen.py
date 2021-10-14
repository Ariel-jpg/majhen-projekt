from Classes.Friends_requests.Friend_request import Friend_Request
        
class Citizen:
    def __init__(self, name, last_name, phone_number, cuil) -> None:
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.cuil = cuil

        self.friend_list = dict()
        self.rejections_list = dict()
    
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

    def send_friend_request(self, friend) -> None: # Dispatcher - c1 Method
        Friend_Request(self, friend)
    
    def recieve_friend_request(self, sender, friend_request) -> None: # Listener - c2 Method
        print(f"{self.name} {self.last_name} te llegó una solicitud de {sender.name} {sender.last_name}")

        response = input("Querés aceptar la solicitud y/n: ").lower()

        if response == "y":
            self.friend_list.update({ sender.get_cuil() : sender.get_formatted_data() })

            friend_request.accept_friend_request()
        else: 
            friend_request.reject_friend_request()
    
    def recieve_answer_friend_request(self, friend_request) -> None: # Listener - c1 Method
        accepted = friend_request.get_response()
        friend = friend_request.reciever

        if accepted:
            self.friend_list.update({ friend.get_cuil() : friend.get_formatted_data() })
        else: 
            friend_id = friend.get_cuil()

            if bool(self.rejections_list.get(friend_id)):
                rejections_counter = self.rejections_list.get(friend_id)["rejections_counter"] + 1
            else: 
                rejections_counter = 1

            self.rejections_list.update({ friend_id: { "cuil": friend_id, "rejections_counter": rejections_counter } })