# Main

# test 14/10

from Classes.Citizen.Citizen import Citizen
from Classes.Friends_requests.Friends_requests import Friends_Requests
from Classes.Registration import Registration

data = [
    "03567492743",
    "20445738571",
    "21406826487",
    "13458484274"
]

instances = []

for cuil in data:
    Registration.sign_up(cuil)

# instances.append(Registration.login())

Ariel = Registration.login_dev("03567492743", "0118568921")
Lola = Registration.login_dev("20445738571", "2994763810")
Maximo = Registration.login_dev("21406826487", "2218348361")
Camila = Registration.login_dev("13458484274", "2207357381")

Ariel.send_friend_request(Camila)

Ariel.send_friend_request(Lola)
Ariel.send_friend_request(Lola)
Ariel.send_friend_request(Lola)
Ariel.send_friend_request(Lola)
Ariel.send_friend_request(Lola)

Camila.send_friend_request(Maximo)
Lola.send_friend_request(Maximo)

Friends_Requests # Debug

print(Registration.__str__())