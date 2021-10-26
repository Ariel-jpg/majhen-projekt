# Static class
class Reports_requests:
    report_requests = dict({
        "espectaculos": 0,
        "seguridad": 0,
        "salud": 0,
    })

    def update_report_request(report_key):
        report_value = Reports_requests.report_requests.get(report_key) + 1

        Reports_requests.report_requests.update({ report_key: report_value })

    def get_report_request(report_key):
        return Reports_requests.report_requests.get(report_key)
        
    @staticmethod
    def get_all_report_requests_dev() -> str:
        string = ""

        for type_event, quantity in Reports_requests.report_requests.items():
            string += f"En el evento '{type_event}' hay {quantity} personas \n"

        return string