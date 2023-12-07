import datetime

class MonoState(object):
    _state = {}
    
    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        self.__dict__ = cls._state
        return self
    
class Logger(MonoState):
    log_file = None
    
    def __init__(self, path):
        if self.log_file is None:
            self.log_file = open(path, mode='w')
            
    def write_log(self, log_record):
        now = str(datetime.datetime.now())
        record = f'{now}: {log_record}\n'
        self.log_file.write(record)
        
    def close_log(self):
        self.log_file.close()
        self.log_file = None

logger = Logger('records.log')
logger.write_log('Andrea')
logger2 = Logger('second.log')
logger2.write_log('Lai')
logger.close_log()

with open('records.log', 'r') as f:
    for line in f:
        print(line)