from . import General_state

class Table:
    pass

class Sensor_table (Table):
    def __init__(self, sensors) -> None:
        super().__init__()
        self.sensors = sensors

    def order_sensors(self, reverse = False) -> dict:
        sensors_dictionary = self.sensors

        sensors_list_dict1 = list() # Inmutable
        sensors_list_dict2 = list()
        sensors_list = list()

        for key, value in sensors_dictionary.items():
            # values = (sensors_dictionary.get(key).get_actual_concurrency())
            sensors_list_dict1.append({'id_': key, 'concurrency': value["concurrency"] })
            sensors_list_dict2.append({'id_': key, 'concurrency': value["concurrency"]})

            sensors_list.append(value["concurrency"])

        sensors_list = sorted(sensors_list, reverse= reverse)

        for i in range(len(sensors_list)):
                for sensor_key in sensors_list_dict1:
                    if sensor_key['concurrency'] == sensors_list[i]:
                        sensors_list_dict2[i] = sensor_key

        return sensors_list_dict2 

class General_table (Table):
    pass