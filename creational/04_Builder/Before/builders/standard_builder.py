from .abc_builder import AbcBuilder


class StandardBuilder(AbcBuilder):
    def case(self):
        self._computer.case = 'Coolermaster'

    def build_mainboard(self):
        self._computer.mainboard = 'MSI'
        self._computer.cpu = 'Intel Core 19'
        self._computer.memory = '2 X 160GB'

    def install_hard_drive(self):
        self._computer.hard_drive = 'SSD 2TB'

    def install_video_card(self):
        self._computer.video_card = 'GeForce'
