from datetime import datetime

# Static class
class Friends_Requests:
    friends_requests_pending = dict()
    friends_requests_solved = dict()

    @staticmethod
    def resolved_friend_request(friend_request):
        Friends_Requests.friends_requests_solved.update({
            friend_request.id_: {
                "sender_cuil": friend_request.transmitter.get_cuil(),
                "reciever_cuil": friend_request.reciever.get_cuil(),
                "friends": friend_request.state["accepted"]
        }})

        Friends_Requests.friends_requests_pending.pop(friend_request.id_)

    @staticmethod
    def add_new_friend_request(friend_Request):
        Friends_Requests.friends_requests_pending.update(
            { friend_Request.id_: friend_Request })