from autos.ford.fiesta import FordFiesta
from autos.ford.lincoln import LincolnMKS
from autos.ford.mustang import FordMustang 
from .abc_factory import AbcFactory

class FordFactory(AbcFactory):
    def create_economy():
        return FordFiesta()

    def create_sport():
        return FordMustang()
    
    def create_luxury():
        return LincolnMKS()
