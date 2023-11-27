from computer import Computer
import abc


class AbcBuilder(abc.ABC):
    def new(self):
        self._computer = Computer()

    def get(self):
        return self._computer

    def build(self):
        self.computer = Computer()

    @abc.abstractmethod
    def case(self):
        pass

    @abc.abstractmethod
    def build_mainboard(self):
        pass

    @abc.abstractmethod
    def install_hard_drive(self):
        pass

    @abc.abstractmethod
    def install_video_card(self):
        pass
