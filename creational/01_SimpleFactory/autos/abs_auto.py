import abc


class AbsAuto(abc.ABC):
    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractclassmethod
    def stop(self):
        pass
