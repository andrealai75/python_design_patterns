from autofactory import AutoFactory


factory = AutoFactory()

for cname in ('ChevyVolt', 'FordFusion', 'JeepSahara', 'Tesla', 'Fiat'):
    car = factory.create_instance(cname)
    car.start()
    car.stop()
