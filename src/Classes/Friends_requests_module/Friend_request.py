from Modules.Base_converter import decimal_to_hexadecimal
Friends_requests import Friends_Requests
from datetime import datetime

# sender is an instance of citizen
class Friend_Request:
    def __init__(self, sender, reciever, admin_in_charge) -> None:
        self.id_ = self.generate_friend_request_id(sender.get_cuil())
        self.sender = sender
        self.reciever = reciever
        self.admin_in_charge = admin_in_charge
        self.state = dict({
            "state": "pending",
            "accepted": None
        })

        Friends_Requests.add_new_friend_request(self)  # Check
        
        self.notify_reciever_friend_request()

    def generate_friend_request_id(self, id_sender) -> str:  
        date = datetime.now()
        date = f"{date.minute}{date.microsecond}"

        date = decimal_to_hexadecimal(int(date))
        cuil = decimal_to_hexadecimal(int(id_sender))
        
        date = date + cuil

        return date

    def get_response(self) -> bool:
        return self.state["accepted"]

    def update_state(self) -> None:
        Friends_Requests.resolved_friend_request(self)

    def accept_friend_request(self) -> None:
        self.state = dict({
            "state": "resolved",
            "accepted": True
        })

        self.notify_sender_friend_request()
        self.update_state()

    def reject_friend_request(self) -> None:
        self.state = dict({
            "state": "resolved",
            "accepted": False
        })

        self.notify_sender_friend_request()
        self.update_state()

    def notify_reciever_friend_request(self) -> None:
        self.reciever.recieve_friend_request(self.sender, self)
        
    def notify_sender_friend_request(self) -> None:
        self.sender.recieve_answer_friend_request(self)
