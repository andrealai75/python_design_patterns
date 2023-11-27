from .abc_builder import AbcBuilder


class BudgetBuilder(AbcBuilder):
    def case(self):
        self._computer.case = 'Corsair'

    def build_mainboard(self):
        self._computer.mainboard = 'ASUS'
        self._computer.cpu = 'AMD'
        self._computer.memory = '2 X 4GB'

    def install_hard_drive(self):
        self._computer.hard_drive = 'Seagate'

    def install_video_card(self):
        self._computer.video_card = 'On board'
