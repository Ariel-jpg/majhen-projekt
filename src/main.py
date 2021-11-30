from Import_index import General_state
from Interface.main_interface import Interface
from json_module.json_main import Json
from Map.Zones import Zones

if __name__ == "__main__":
    General_state.load_instances()  
    sensors = General_state.get_sensors()
    
    json_ = Json()
    json_.save_json()
    sensors_dict = json_.load_json_from_file()
   
   
    zones = Zones([1, 2, 3, 4], sensors_dict)
    zones.print_map_zone(3)

    # Interface()
    # sensor_table = Sensor_table()
    # 20445738571
