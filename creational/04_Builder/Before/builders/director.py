class Director(object):
    def __init__(self, builder):
        self._builder = builder

    def build(self):
        self._builder.new()
        self._builder.case()
        self._builder.build_mainboard()
        self._builder.install_hard_drive()
        self._builder.install_video_card()

    def computer(self):
        return self._builder.get()
