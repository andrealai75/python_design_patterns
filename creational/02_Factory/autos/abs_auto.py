import abc


class AbsAuto(abc.ABC):
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractclassmethod
    def stop(self):
        pass
