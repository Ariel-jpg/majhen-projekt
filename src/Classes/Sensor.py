from .State.Admins import Admins

class Sensor:
    def __init__(self, event) -> None:
        self.type_event = event.type_event
        self.event = event

        self.notify_event()

    def notify_event(self):
        admin_in_charge = Admins.get_admin()
        admin_in_charge.receive_report_request(self)