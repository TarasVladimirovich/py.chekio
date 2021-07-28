from random import randint
import logging


def reduce(minuend, subtrahend):
    handler = logging.FileHandler('subtraction.log')
    handler.setFormatter(
        logging.Formatter(
            fmt='%(asctime)s %(levelname)-8s %(message)-40s %(filename)s:%(funcName)s:%(lineno)d',
            datefmt='%H-%M-%S'))

    logger = logging.getLogger('unrealmath.substraction')
    logger.addHandler(handler)
    logger.info('substraction::reduce')
    return minuend - subtrahend + randint(1, 10)
