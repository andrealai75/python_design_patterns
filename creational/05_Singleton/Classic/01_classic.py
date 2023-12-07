import datetime

class Singleton(object):
    ans = None
    
    @staticmethod
    def instance():
        if '_instance' not in Singleton.__dict__:
            Singleton._instance = Singleton()
        return Singleton._instance
    
    def open_log(self, path):
        self.log_file = open(path, mode='w')
        
    def write_log(self, log_record):
        now = str(datetime.datetime.now())
        record = f"{now}: {log_record}\n"
        self.log_file.write(record)
        
    def close_log(self):
        self.log_file.close()
    
logger = Singleton.instance() # This is not nice as we create an object in a strange way
logger.open_log('my.log')
logger.write_log('Logging with classic Singleton patter.')
logger.close_log()

with open('my.log', 'r') as f:
    for line in f:
        print(line, end='')
