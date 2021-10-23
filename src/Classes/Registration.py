from Modules.Anses.Anses import Anses
from .Citizen_module.Citizen import Citizen

# static class
class Registration:
    registered_citizens = dict()

    @staticmethod
    def __str__():
        string = ""
        
        for _, citizen_data in Registration.registered_citizens.items():
            string = string + str(citizen_data)

        return string

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
        Registration.registered_citizens.update({ new_citizen.cuil : new_citizen })

    @staticmethod   
    def login() -> Citizen:
        print("INICIAR SESIÓN")        
        
        citizen_cuil = input("Cuil: ")
        citizen_phone = input("Número de celular: ")
        
        while not Registration.register_exists(citizen_cuil, citizen_phone):
            print("Los datos ingresados no corresponden con un usuario registrado. Por favor, verifique los datos e intente de nuevo")
            
            citizen_cuil = input("Cuil: ")
            citizen_phone = input("Número de celular: ")
        
        citizen = Registration.registered_citizens[citizen_cuil]

        return citizen

    @staticmethod
    def register_exists(citizen_cuil, citizen_phone) -> bool: 
        return bool( Registration.registered_citizens.get(citizen_cuil) ) and ( Registration.registered_citizens[citizen_cuil].phone_number == citizen_phone )

    # DEV METHODS -------------

    @staticmethod   
    def login_dev(citizen_cuil, citizen_phone) -> Citizen:
        print("INICIAR SESIÓN")        
        
        citizen_cuil = citizen_cuil
        citizen_phone = citizen_phone
        
        while not Registration.register_exists(citizen_cuil, citizen_phone):
            print("Los datos ingresados no corresponden con un usuario registrado. Por favor, verifique los datos e intente de nuevo")
            
            citizen_cuil = input("Cuil: ")
            citizen_phone = input("Número de celular: ")
        
        citizen = Registration.registered_citizens[citizen_cuil]

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
        Registration.registered_citizens.update({ new_citizen.cuil : new_citizen })