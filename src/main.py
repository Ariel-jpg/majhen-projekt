from Import_index import General_state
from Interface.main_interface import Interface

if __name__ == "__main__":
    General_state.load_instances()  
    # sensors = General_state.get_sensors()
    # 
    # json_ = Json()
    # json_.save_json()
    # sensors_dict = json_.load_json_from_file()

    Interface()