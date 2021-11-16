# Main

# test 17/10

from Classes.State.Registration_state import Registration_State as Registration
from Classes.State.Friends_requests import Friends_Requests
from Classes.Admin import Admin
from Classes.State.Admins import Admins
from Classes.State.Reports_requests import Reports_requests

# Create Admins -

Ariel_Admin = Admin("Ariel_Admin", "1", "123")
Admins.add_admin(Ariel_Admin)

Lola_Admin = Ariel_Admin.create_admin("Lola_Admin", "2", "1234")
Masi_Admin = Ariel_Admin.create_admin("Masi_Admin", "3", "12345")
Camila_Admin = Ariel_Admin.create_admin("Camila_Admin", "4", "123456")

Lola_Admin.block_admin("1")
Ariel_Admin.delete_admin("2")

Lola_Admin.unblock_admin("1")
Ariel_Admin.delete_admin("2")

# The administrator that was removed does not exist in the "Administrators" class, but does exist in the runtime. However, you will not be able to perform any operations
Lola_Admin.create_admin("Lola_Admin 2", "5", "123")

# -----------------

# Create Users -

data = [
    "03567492743",
    "20445738571",
    "21406826487",
    "13458484274"
]

for cuil in data:
    Registration.sign_up_dev(cuil)

# instances = []
# instances.append(Registration.login())

Ariel = Registration.login_dev("03567492743", "0118568921")
Lola = Registration.login_dev("20445738571", "2994763810")
Maximo = Registration.login_dev("21406826487", "2218348361")
Camila = Registration.login_dev("13458484274", "2207357381")

# -----------------

# Some requests from friends for routine
Ariel.send_friend_request(Camila)
Camila.send_friend_request(Maximo)
Lola.send_friend_request(Maximo)

# Blocking at 5 rejections and verification that it works
# Ariel.send_friend_request(Lola)
# Ariel.send_friend_request(Lola)
# Ariel.send_friend_request(Lola)
# Ariel.send_friend_request(Lola)
# Ariel.send_friend_request(Lola)

# Ariel.send_friend_request(Lola)

# Administrators block and unblock a user for another user
Ariel_Admin.block_citizen(Lola, Ariel.get_cuil())
Ariel.send_friend_request(Lola) # he can't

Ariel_Admin.unblock_citizen(Lola, Ariel.get_cuil())
Ariel.send_friend_request(Lola) # he can

Ariel.notify_event("seguridad")
Lola.notify_event("seguridad")
Maximo.notify_event("seguridad")
Camila.notify_event("seguridad")
Ariel.notify_event("espectaculos")
Lola.notify_event("seguridad")
Maximo.notify_event("seguridad")
Ariel.notify_event("espectaculos")
Lola.notify_event("seguridad")
Maximo.notify_event("espectaculos")

Ariel.notify_event("salud")
Ariel.notify_event_with_friend("salud", Lola)

Friends_Requests # debug
Registration # debug
Reports_requests # debug
print("Registro de administradores: \n", Admins.get_all_admins_dev())
print("Registro de reportes de eventos: \n", Reports_requests.get_all_report_requests_dev())
print("Registro de solicitudes de amistad: \n", Friends_Requests.get_all_friends_requests_dev())

print(Registration.__str__())