import abc

class AbcMaker(abc.ABC):
    def start(self):
        print(f"Starting {self.friendly_name()}!!")

    def stop(self):
        print(f"Stopping {self.friendly_name()}!!!")
        
    def friendly_name(self):
        name = ""
        for char in self.__class__.__name__:
            if char == char.upper():
                name += " " + char
            else:
                name += char
        return name.strip()
