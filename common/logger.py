import logging, os

curren_path = os.path.dirname(__file__)
log_path = 'D:\\PycharmProjects\\Gittest20201030\\log\\zengzhu.log'


class LoggerInfo:
    def __init__(self, logpath=log_path):
        self.logpath = logpath
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level=logging.INFO)
        self.file_log = logging.FileHandler(self.logpath,encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        self.file_log.setFormatter(formatter)
        self.logger.addHandler(self.file_log)

    def log_info(self, message):
        self.logger.info(message)

    def err_info(self, message):
        self.logger.error(message)


logger = LoggerInfo()
if __name__ == '__main__':
    # logger1 = LoggerInfo()
    logger.log_info('sss')
