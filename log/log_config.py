import logging
from datetime import datetime
from functools import wraps
import inspect

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('app.log')

f_handler.setLevel(logging.DEBUG)
c_handler.setLevel(logging.INFO)

c_handler.setFormatter(logging.Formatter('%(levelname)-10s %(asctime)s : %(message)s'))
f_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)-10s %(module)s : %(message)s'))

logger.addHandler(c_handler)
logger.addHandler(f_handler)



def log_decor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.debug(f'{datetime.now().strftime("%Y.%M.%d %H:%M")}'
                  f' функция {func.__name__} вызвана из функции'
                  f' {inspect.currentframe().f_back.f_code.co_name}')
        return func(*args, **kwargs)

    return wrapper


if __name__ == '__main__':
    logger.info('This is info message')
    logger.error('This is error log')
    logger.warning('this is warn log')
