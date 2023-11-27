class Computer(object):
    case: str
    mainboard: str
    cpu: str
    memory: str
    hard_drive: str
    video_card: str

    def display(self) -> None:
        print(f"{self.case} - {self.mainboard} - {self.cpu} - {self.memory} - {self.hard_drive} - {self.video_card}")
