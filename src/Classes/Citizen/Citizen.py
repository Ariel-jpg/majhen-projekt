from Anses import Anses


# Anses.search_citizen(cuil) -> dict { name, last_name, cuil, phone }
# Ariel["last_name"]
# Anses.validate_citizen(cuil) -> bool



class Citizen:
    friend_list = dict()
    rejections_list = dict()

    def __init__(self, name, last_name, phone_number, cuil):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.cuil = cuil

    def GetRejections(self, citizen) -> dict:
        if self.rejections_list[citizen.cuil]:
            return self.rejections_list[citizen.cuil]["rejections"]
        else: 
            return None
        
    def sendGreeting(self, reciever):
        reciever.RecieveFriendRequest(self)
        
    def RecieveFriendRequest(self, sender):
        #sender = self.nombre
        print(f"{self.name}!, you have recieved a friend request from {sender.name}")
        answer = input("Do you accept? Y/N: ")
        sender.GetAnswer(self, answer.lower())

    def GetAnswer(self, reciever, answer, sender):
        if answer == "y":
            print("yes")
            self.friend_list.update({ reciever.cuil : reciever })
            self.friend_list.update({ sender.cuil : sender })

        elif answer == "n":
            print("no")
            
            rejections_counter = None
        
            if self.rejections_list.get(reciever.cuil):
                rejections_counter = self.rejections_list[reciever.cuil]["rejections"] + 1

            else:
                 rejections_counter = 1
                 self.rejections_list.update({ reciever.cuil : { "reciever": reciever.cuil, "rejections": rejections_counter } })

        else:
            print("The user has dennied your friend request :(")
   
class Registration:
    registered_users = dict()

    def Registration(self):
        name = input("Name: ")
        last_name = input("last_name: ")
        cuil = input("cuil: ")
        phone = input("phone: ")
        if Anses.validate_citizen(name, last_name, cuil, phone):
            new_citizen = Citizen(name, last_name, cuil, phone)
            self.registered_users.update({ new_citizen.cuil : new_citizen })
            print(":) yayyy")

        else:
            print("Te quedaste afuera. F")


cami = Registration()
cami.Registration()