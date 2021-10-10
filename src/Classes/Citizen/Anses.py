from dataset import dataset

class Anses:
    @staticmethod
    def validate_citizen(citizen_cuil) -> bool:
        return bool(Anses.search_citizen(citizen_cuil))

    @staticmethod
    def search_citizen(citizen_cuil) -> dict:
        return dataset.get(citizen_cuil)