# Main

# test 13/10

from Classes.Citizen.Citizen import Citizen, Registration

data = [
    "03567492743",
    "20445738571",
    "21406826487",
    "13458484274"
]

instances = []

for cuil in data:
    Registration.sign_up(cuil)

instances.append(Registration.login())

print(Registration.__str__())