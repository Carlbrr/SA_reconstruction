class Import:
    def __init__(self, name:str):
        self.name = name
        self.attributes = dict()
        self.total_calls = 0

    def str(self):
        return (f"Import: module {self.name}\n"+
                f"Total calls: {self.total_calls}\n"+
                f"Attributes: {self.attributes}\n")