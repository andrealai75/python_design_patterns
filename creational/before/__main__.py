from chevyvolt import ChevyVolt
from fordfusion import FordFusion
from jeepsahara import JeepSahara
from nullcar import NullCar


def getcar(carname):
    if carname == 'Chevy':
        return ChevyVolt()
    if carname == 'Ford':
        return FordFusion()
    if carname == 'Jeep':
        return JeepSahara()
    else:
        return NullCar(carname)


for cname in ('Chevy', 'Ford', 'Jeep', 'Tesla'):
    car = getcar(cname)
    car.start()
    car.stop()
