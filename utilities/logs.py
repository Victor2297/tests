import logging
from importlib import reload

class GetLogs:
    @staticmethod
    def get_logs():
        reload(logging)
        logging.basicConfig(filename='C:\\Users\\Victor\\PycharmProjects\\testv11111\\Logs\\test.log',
                            filemode='w',
                            level=logging.DEBUG)
        logger = logging.getLogger()
        return logger