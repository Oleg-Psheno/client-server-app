import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('app.log')

f_handler.setLevel(logging.WARNING)
c_handler.setLevel(logging.INFO)

c_handler.setFormatter(logging.Formatter('%(levelname)-10s %(asctime)s : %(message)s'))
f_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)-10s %(module)s : %(message)s'))

logger.addHandler(c_handler)
logger.addHandler(f_handler)

if __name__ == '__main__':

    logger.info('This is info message')
    logger.error('This is error log')
    logger.warning('this is warn log')


