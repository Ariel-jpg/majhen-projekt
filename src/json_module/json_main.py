from Import_index import General_state
import json

class Json:
    def __init__(self) -> None:
        pass

    def save_json(self):
        sensores = General_state.get_sensors_formatted_data()

        with open('./src/json_module/data.json', 'w', encoding='utf-8') as f:
            json.dump(sensores, f, ensure_ascii=False, indent=4)
    
    def load_json_from_file(self):
        with open('./src/json_module/data.json') as json_file:
            data = json.load(json_file)

            print(data)
            return data

