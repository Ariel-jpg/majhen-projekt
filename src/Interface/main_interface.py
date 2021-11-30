
from Import_index import Sensor_table, General_state, Citizen, Admin, Sensor
from .Presenters import Presenters
#import from general_state General state, and then load sensor???
class Interface:
    def __init__(self) -> None:
        self.role = None
        
        self.inicialize()

    def control_data_entry(self, options_quantity) -> str:
        'Solo puede retornar una opcion valida para el sistema'

        entry = input().strip()

        try:
            for char in entry:
                cast_test = int(char)
        except:
            entry = 1000

        while not (int(entry) > 0 and int(entry) <= options_quantity):
                print(f"Por favor introduzca una opción válida para ingresar al sistema (del 1 al {options_quantity}): ", end='')
                entry = input()    

        return entry

    def inicialize(self):
        print("Bienvenido a Lamac ¿Cómo desea entrar?")
        print("1 - Como ciudadano")
        print("2 - Como administrador")
        print("3 - Como sensor")
        print("4 - Ver mapa")

        user_entry = self.control_data_entry(4)

        presenter = Presenters()

        if user_entry == "1":
            citizen = presenter.citizen_registration()
            
            # rand_citizen = General_state.citizens_state.get_random_citizen

            # citizen.send_friend_request(rand_citizen())
            # citizen.send_friend_request(rand_citizen())
            # citizen.send_friend_request(rand_citizen())
            # citizen.send_friend_request(rand_citizen())
            # citizen.send_friend_request(rand_citizen())

            # citizen.send_event_report()
            # citizen.send_event_report()
            # citizen.send_event_report()
            
            # Call the citizen interface
            self.citizen_interface(citizen)

        elif user_entry == "2":

            admin = presenter.admin_registration()

            # Call the admin interface
            self.admin_interface(admin)
        elif user_entry == "3":
            self.sensor_interface()

        else:
            self.map_interface()


    def citizen_interface(self, citizen: Citizen):

        def initiate_citizen():
            print('Menu Ciudadano.\n¿Que accion desea realizar?')
            print('1. Crear/reportar un evento')
            print('2. Mandar una solicitud de amistad')
            print('3. Volver al menu principal')
            
            citizen_entry = self.control_data_entry(3)

            if citizen_entry == '1':
                print('-- Crear/reportar un evento fue seleccionado -- ')
                citizen.send_event_report()
                self.citizen_interface(citizen)
                #vuelve al menu citizen
            
            elif citizen_entry == '2':
                print('-- Mandar una solicitud de amistad fue seleccionado --')
                print('Ingresa el cuil de la persona: ', end='')
                cuil_FR = input()       # get a cuil, add to friend list.
                citizen_state = General_state.get_citizens_state()
                recipient = citizen_state.get_citizen(cuil_FR)

                citizen.send_friend_request(recipient)
                self.citizen_interface(citizen)
                # vuelve al menu de citizen.
            
            elif citizen_entry == '3':  #go back to main menu
                self.inicialize() 

        initiate_citizen()

    def admin_interface(self, admin_logged: Admin):
        
        def initiate_Admin():
            print('Menu Administrador. \n¿Que accion desea realizar?')
            print('1. Ver tabla de estadisticas')
            print('2. Ver sensores')
            print('3. Opciones de Administrador')
            print('4. Bloquear Ciudadano')
            print('5. Volver al menu principal.')

            admin_entry = self.control_data_entry(5)

            presenter = Presenters()

            if admin_entry == '1':      # show staticts table
                print('-- Ver tabla de estadisticas fue seleccionado --')
                print('Ver tabla de estadisticas de la zona:')
                print('1. Zona 1')
                print('2. Zona 2')
                print('3. Zona 3')
                print('4. Zona 4')
                print('5. Volver a menu Administrador.')

                states_table_entry = self.control_data_entry(5)

                presenter = Presenters()

                if states_table_entry == '1':
                    print('-- Mostrando tabla de zona 1 --')

                
                elif states_table_entry == '2':
                    print('-- Mostrando tabla de zona 2 --')


                elif states_table_entry == '3':
                    print('-- Mostrando tabla de zona 3 --')

                
                elif states_table_entry == '4':
                    print('-- Mostrando tabla de zona 4 --')

                elif states_table_entry == '5':
                    self.admin_interface(admin_logged)



            elif admin_entry == '2':        # show sensors
                print('-- Ver sensores fue seleccionado -- ')           #maybe not show this

            elif admin_entry == '3':        # create/ block/ delete admin
                print('-- Opciones de Administrador fue seleccionado -- ')
                print('Que accion quiere realizar?')
                print('1. Crear un administrador')
                print('2. Bloquear un administrador')
                print('3. Eliminar un administrador')
                print('4. Volver a menu Administrador')
                
                options_admin_entry = self.control_data_entry(4)

                presenter = Presenters()

                if options_admin_entry == '1':      # create admin
                    print('-- Crear un administrador fue seleccionado --')
                    new_admin = admin_logged.create_admin()

                    print('Un nuevo administrador fue creado')
                    print(f'ID:{new_admin.Admin.get_id()}')
                    print(f'Password: ', new_admin.get_password())
                    
                elif options_admin_entry == '2':        #block admin
                    print('Bloquear un administrador fue seleccionado --')
                    id_admin = input('ID del administrador al que se desea bloquear: ')     
                    print(f'{id_admin}')
                    Admin.block_admin(id_admin)
                    print(f'Administrador {id_admin} fue bloquado.')
                
                elif options_admin_entry == '3':        #delete admin
                    print('-- Eliminar un administrador fue seleccionado --')
                    id_admin = input('ID del administrador al que se desea eliminar: ')
                    print(f'{id_admin}')
                    
                    admins_state = General_state.get_admins_state()
                    
                    admins_state.delete_admin(id_admin)

                    print('Administador fue eliminado.')


                elif options_admin_entry == '4':        #go back to admin menu
                    self.admin_interface(admin_logged)

            elif admin_entry == '4':        #  block citizen, show random citizen getting blocked
                print('-- Opciones ciudadano seleccionado -- ')
                print('¿Que accion desea realizar?')
                print('1. Bloquear un ciudadano')
                print('2. Volver a menu Administrador')

                citizen_options = self.control_data_entry(2)

                presenter = Presenters()

                if citizen_options == '1':      #block citizen from admin POV
                    print('-- bloquear ciudadano fue seleccionado -- ')
                    get_cuil_cit = input('Cuil del ciudadano que se desea bloquear: ')
                    #where is it???

                elif citizen_options == '2':    #exit to admin menu
                    self.admin_interface(admin_logged)

            elif admin_entry == '5':        # go back to main menu
                self.inicialize()

        initiate_Admin()
    
    def sensor_interface(self):
        def initiate_sensor_interface():
            
            print('Menu Sensores.')
            print('1. Sensores activos.')
            print('2. Volver al menu principal.')

            sensor_entry = self.control_data_entry(2)

            if sensor_entry == '1':     #show all active sensors, according to seba in slack
                print('-- Sensores activos fue seleccionado --')
                print('¿Que accion desea realizar?')
                print('1. Mostrar todos los sensores activos')
                print('2. Volver a menu Sensores')

                sensor_type_entry = self.control_data_entry(2)

                if sensor_type_entry == '1':
                    print('--Monstrando sensores activos--')
                    sensors = General_state.get_sensors()

                    for sensor_id, sensor in sensors.items():
                        print(sensor_id + ': \n - Concurrencia:' + sensor.get_actual_concurrency() + '\n - Tipo de evento: ' + sensor.event.get_type_events_str + '- Descripcion del evento: ' + sensor.get_event_description() )

                    self.sensor_interface()

                elif sensor_type_entry == '2':
                    self.sensor_interface()
            
            elif sensor_entry == '2':
                self.inicialize()
        
        initiate_sensor_interface()

    def map_interface(self):
        def initiate_map_interface():
            print('-- Ver mapa fue seleccionado --')
            print('Ver mapa de la zona:')
            print('1. Zona 1')
            print('2. Zona 2')
            print('3. Zona 3')
            print('4. Zona 4')
            print('5. Volver a menu principal')
            
            map_entry = self.control_data_entry(5)

            if map_entry == '5':
                self.inicialize()

            print(f"-- Mostrando mapa de la zona {map_entry} --")

            initiate_map_interface()
            # TODO

        initiate_map_interface()
