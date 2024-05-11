from collections import defaultdict
from import_class import Import #cursed

class Module:
    def __init__(self, name:str):
        self.name = name
        self.imports = defaultdict(Import)

    #returns string of import and all its data
    def str(self):
        import_str=""

        for key, value in self.imports.items():
            import_str += value.name + "\n"
            import_str += f"Total calls: {value.total_calls}\n"
            import_str += "Attributes:\n"
            for key, value in value.attributes.items():
                import_str += f"{key}: {value}\n"
            import_str += "\n"
        return (f"Module: {self.name}\n"
                f"Imports:{import_str}\n")



