class Admins:
    admins_list = dict()

    @staticmethod
    def add_admin(new_admin) -> None: # new_admin = Admin()
        Admins.admins_list.update({ new_admin.get_id(): new_admin})

    @staticmethod
    def validate_admin(admin_id) -> bool:
        try:
            # Access to the Admins.admins_list[admin_id] list always fails if the record does not exist. This is the reason why the try - except option was chosen
            return bool(Admins.admins_list[admin_id]) and Admins.admins_list[admin_id].blocked == False
        except:
            return False

    @staticmethod
    def block_admin(admin_id):
        Admins.admins_list[admin_id].blocked = True

    @staticmethod
    def unblock_admin(admin_id):
        Admins.admins_list[admin_id].blocked = False
        
    @staticmethod
    def delete_admin(admin_id):
        Admins.admins_list.pop(admin_id)



class Admin:
    def __init__(self, name, _id, password) -> None:
        # self.id_ = generate_id() utils method
        self.id_ = _id
        self.name = name
        self.blocked = False

        # self.password = generate_password() 
        self.password = password

    def get_id(self):
        return self.id_

    def block_admin(self, admin_id):
        if Admins.validate_admin(self.id_):
            Admins.block_admin(admin_id)
        else:
            return # Check

    def unblock_admin(self, admin_id):
        if Admins.validate_admin(self.id_):
            Admins.unblock_admin(admin_id)
        else:
            print("No fue posible desbloquear al administrador. Corrobore sus permisos y si el administrador existe e intentelo de nuevo")

            return # Check

    def create_admin(self, name, _id, password):
        if Admins.validate_admin(self.id_):
            new_admin = Admin(name, _id, password) 
            Admins.add_admin(new_admin) # Por entorno de ejecuión la solución es correcta

            return new_admin 
        else: 
            print("No fue posible crear al administrador. Corrobore sus permisos e intentelo de nuevo")
            
            return # Check

    def delete_admin(self, admin_id):
        if Admins.validate_admin(self.id_):
            Admins.delete_admin(admin_id)
        else:
            print("No fue posible eliminar al administrador. Corrobore sus permisos y si el administrador existe e intentelo de nuevo")
            
            return # Check

    def modify_admin(self, admin, name, password): # Check method
        if Admins.validate_admin(self.id_):
            if name != "" and password != "":
                new_admin = Admin(name, admin.get_id(), password)
            elif name != "":
                new_admin = Admin(name, admin.get_id(), admin.password)
            else: 
                new_admin = Admin(admin.name, admin.get_id(), password)
    
            return new_admin
        else:
            print(f"No fue posible modificar al administrador solicitado. Corrobore sus permisos y si el administrador existe e intentelo de nuevo")

            return # Check




Ariel = Admin("Ariel", "1", "123")
Admins.add_admin(Ariel)

Lola = Ariel.create_admin("Lola", "2", "1234")
Masi = Ariel.create_admin("Masi", "3", "12345")
Camila = Ariel.create_admin("Camila", "4", "123456")

Lola.block_admin("1")
Ariel.delete_admin("2")

Lola.unblock_admin("1")
Ariel.delete_admin("2")

# The administrator that was removed does not exist in the "Administrators" class, but does exist in the runtime. However, you will not be able to perform any operations
Lola.create_admin("Lola 2", "5", "123")

print()