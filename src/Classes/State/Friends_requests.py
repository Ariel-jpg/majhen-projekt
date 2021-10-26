# Static class
class Friends_Requests:
    friends_requests_pending = dict() # Multi thread
    friends_requests_solved = dict()

    @staticmethod
    def resolved_friend_request(friend_request) -> None:
        Friends_Requests.friends_requests_solved.update({
            friend_request.id_: {
                "sender_cuil": friend_request.sender.get_cuil(),
                "reciever_cuil": friend_request.reciever.get_cuil(),
                "friends": friend_request.state["accepted"]
        }})

        Friends_Requests.friends_requests_pending.pop(friend_request.id_)

    @staticmethod
    def add_new_friend_request(friend_Request) -> None:
        Friends_Requests.friends_requests_pending.update({ friend_Request.id_: friend_Request })

    @staticmethod
    def get_all_friends_requests_dev() -> str:
        string = ""

        for friend_Request_id, state in Friends_Requests.friends_requests_solved.items():
            sender_cuil = state["sender_cuil"]
            reciever_cuil = state["reciever_cuil"]
            friends = state["friends"]

            string += f"{friend_Request_id}: - sender_cuil: {sender_cuil} - reciever_cuil: {reciever_cuil} - friends: {friends} \n"

        return string