class Normal_Event:
    def __init__(self, type_event) -> None:
        self.type_event = type_event

class Event_with_friend:
    def __init__(self, type_event, associate_friend, sender) -> None:
        self.type_event = type_event
        self.associate_friend = associate_friend
        self.sender = sender

        self.notify_friend_invitation()
        
    def notify_friend_invitation(self):
        self.associate_friend.recieve_friend_invitation(self)