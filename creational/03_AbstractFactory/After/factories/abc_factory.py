import abc  

class AbcFactory(abc.ABC):
    @abc.abstractmethod
    def create_economy():
        pass

    @abc.abstractmethod
    def create_sport():
        pass
    
    @abc.abstractmethod
    def create_luxury():
        pass
