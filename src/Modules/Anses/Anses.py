import dataset

class Anses:
    
    def __init__(self, dataset) -> None:
        self.dataset = dataset


lo = dict(
    {
        "id" : "rodrigo"
    }
)

a = Anses(dataset)

print(a)