from .abs_auto import AbsAuto


class Fiat(AbsAuto):
    def start(self):
        print('Fiat is starting!')

    def stop(self):
        print('Fiat is shutting down.')
