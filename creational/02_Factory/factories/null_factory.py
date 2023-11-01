from .abs_factory import AbsFactory
from autos.nullcar import NullCar

class NullFactory(AbsFactory):
    def create_auto(self):
        null = NullCar("Unknown")
        null.name = 'Null'
        return null
