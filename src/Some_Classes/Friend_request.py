from datetime import datetime

# Static class


class Friends_Request:
    friends_requests_pending = dict()

    def resolved_friend_request(friend_request_id):
        Friends_Request.friends_requests_pending.popitem()

    @staticmethod
    def add_new_friend_request(self, friend_Request):
        Friend_Request.friends_requests_pending.update(
            {friend_Request.id: friend_Request})

# transmitter is an instance of citizen


class Friend_Request (Friends_Request):
    def __init__(self, transmitter, id_receiver, friend) -> None:
        self.transmitter = transmitter
        self.id_receiver = id_receiver
        self.state = dict({
            "state": "pending",
            "accepted": None
        })

        self.id = self.generate_friend_request_id(transmitter.get_id())

        Friends_Request.add_new_friend_request(self)  # Check

    def generate_friend_request_id(id_transmitter):
        # Provisional code

        id = datetime.now()
        id.strftime('%m%d%H%M%S')

        return id

    def get_data(self):
        data = dict({
            "transmitter": self.transmitter,
            "id_receiver": self.id_receiver,
            "state": self.state
        })

        return data

    def modify_state(self, friend_request_accepted) -> None:
        self.state = dict({
            "state": "resolved",
            "acceped": friend_request_accepted
        })

        def dispatch_admin_notify():
            pass
