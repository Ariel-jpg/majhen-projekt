class Admins:
    admins_list = dict()

    @staticmethod
    def add_admin(new_admin) -> None: # new_admin = Admin( -> None)
        Admins.admins_list.update({ new_admin.get_id(): new_admin})

    @staticmethod
    def validate_admin(admin_id) -> bool:
        try:
            # Access to the Admins.admins_list[admin_id] list always fails if the record does not exist. This is the reason why the try - except option was chosen
            return bool(Admins.admins_list[admin_id]) and Admins.admins_list[admin_id].blocked == False
        except:
            return False

    @staticmethod
    def block_admin(admin_id) -> None:
        Admins.admins_list[admin_id].blocked = True

    @staticmethod
    def unblock_admin(admin_id) -> None:
        Admins.admins_list[admin_id].blocked = False
        
    @staticmethod
    def delete_admin(admin_id) -> None:
        Admins.admins_list.pop(admin_id)

    @staticmethod
    def get_admin(): # Return Admin, annotation causes import conflicts
        for _, admin in Admins.admins_list.items():
            if not admin.blocked:
                return admin
        # not all administrators can be locked out

    @staticmethod
    def get_all_admins_dev() -> str:
        string = ""

        for admin_id, admin in Admins.admins_list.items():
            string += f"{admin_id}: - name: {admin.name} - blocked: {admin.blocked} \n"

        return string