from .abs_factory import AbsFactory
from autos.fordfusion import FordFusion

class FordFactory(AbsFactory):
    def create_auto(self):
        ford = FordFusion()
        ford.name = 'Ford Fusion'
        return ford
