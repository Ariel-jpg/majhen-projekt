
from ..Citizen import Citizen
from ..Modules.Anses.Anses import Anses

class Registration_State:
    registered_citizens = dict()

    def __init__(self) -> None:
        pass

    def update_registered_citizens(self, new_registered_citezens):
        self.registered_citizens = new_registered_citezens
    
    @staticmethod
    def sign_up() -> None:
        citizen_cuil = input('Cuil: ')

        while(not Anses.validate_citizen(citizen_cuil)):
            print("El cuil ingresado no corresponde a un ciudadano real. Por favor verifique los datos e intente de nuevo")
            citizen_cuil = input('Cuil')

        citizen_data = Anses.get_citizen_data(citizen_cuil)
        
        name = citizen_data["name"]
        last_name = citizen_data["last_name"]
        phone = citizen_data["phone"]
       
        new_citizen = Citizen(name, last_name, phone, citizen_cuil)
        Registration_State.registered_citizens.update({ new_citizen.cuil : new_citizen })
    
    @staticmethod   
    def login() -> Citizen:
        print("INICIAR SESIÓN")        
        
        citizen_cuil = input("Cuil: ")
        citizen_phone = input("Número de celular: ")
        
        while not Registration_State.register_exists(citizen_cuil, citizen_phone):
            print("Los datos ingresados no corresponden con un usuario registrado. Por favor, verifique los datos e intente de nuevo")
            
            citizen_cuil = input("Cuil: ")
            citizen_phone = input("Número de celular: ")
        
        citizen = Registration_State.registered_citizens[citizen_cuil]

        return citizen
    
    # login and sing up dev

    @staticmethod   
    def login_dev(citizen_cuil, citizen_phone) -> Citizen:
        print("INICIAR SESIÓN")        
        
        citizen_cuil = citizen_cuil
        citizen_phone = citizen_phone
        
        while not Registration_State.register_exists(citizen_cuil, citizen_phone):
            print("Los datos ingresados no corresponden con un usuario registrado. Por favor, verifique los datos e intente de nuevo")
            
            citizen_cuil = input("Cuil: ")
            citizen_phone = input("Número de celular: ")
        
        citizen = Registration_State.registered_citizens[citizen_cuil]

        return citizen
    

    def sign_up_dev(cuil) -> None:
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
        Registration_State.registered_citizens.update({ new_citizen.cuil : new_citizen })
    
    @staticmethod
    def register_exists(citizen_cuil, citizen_phone) -> bool: 
        return bool( Registration_State.registered_citizens.get(citizen_cuil) ) and ( Registration_State.registered_citizens[citizen_cuil].phone_number == citizen_phone )

    @staticmethod
    def __str__():
        string = ""
        
        for _, citizen_data in Registration_State.registered_citizens.items():
            string = string + str(citizen_data)

        return string