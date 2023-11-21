from autos.gm.cadillac import CadillacCTS
from autos.gm.camaro import ChevyCamaro
from autos.gm.spark import ChevySpark
from .abc_factory import AbcFactory

class GMFactory(AbcFactory):
    def create_economy():
        return ChevySpark()

    def create_sport():
        return ChevyCamaro()
    
    def create_luxury():
        return CadillacCTS()
