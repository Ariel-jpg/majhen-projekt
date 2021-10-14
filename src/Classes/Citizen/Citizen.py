from os import stat
from Modules.Anses.Anses import Anses

# Anses.get_citizen_data(cuil) -> dict { name, last_name, cuil, phone }
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

    def __str__(self) -> str:
        return f"- name: {self.name} \n- last_name: {self.last_name} \n- phone_number: {self.phone_number} \n- cuil: {self.cuil}\n"

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

# static class
class Registration:
    registered_citizens = dict()

    @staticmethod
    def __str__():
        string = ""
        
        for _, citizen_data in Registration.registered_citizens.items():
            string = string + str(citizen_data)

        return f"{string}"

    @staticmethod
    # def sign_up() -> None:
    def sign_up(cuil) -> None:
        # citizen_cuil = input('Cuil: ')
        citizen_cuil = cuil

        while(not Anses.validate_citizen(citizen_cuil)):
            print("El cuil ingresado no corresponde a un ciudadano real. Por favor verifique los datos e intente de nuevo")
            citizen_cuil = input('Cuil')

        citizen_data = Anses.get_citizen_data(citizen_cuil)
        
        name = citizen_data["name"]
        last_name = citizen_data["last_name"]
        phone = citizen_data["phone"]
       
        new_citizen = Citizen(name, last_name, phone, citizen_cuil)
        Registration.registered_citizens.update({ new_citizen.cuil : new_citizen })

    @staticmethod   
    def login() -> Citizen:
        print("INICIAR SESIÓN")        
        
        citizen_cuil = input("Cuil: ")
        citizen_phone = input("Número de celular: ")
        
        while (not Registration.exists_register(citizen_cuil, citizen_phone)):
            print("Los datos ingresados no corresponden con un usuario registrado. Por favor, verifique los datos e intente de nuevo")
            
            citizen_cuil = input("Cuil: ")
            citizen_phone = input("Número de celular: ")
        
        citizen = Registration.registered_citizens[citizen_cuil]

        return citizen

    @staticmethod
    def exists_register(citizen_cuil, citizen_phone) -> bool: 
        return bool( Registration.registered_citizens.get(citizen_cuil) ) and ( Registration.registered_citizens[citizen_cuil].phone_number == citizen_phone )