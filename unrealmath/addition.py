from random import randint
import logging


def add(first, second):
    logging.basicConfig(
        filename='addition.log',
        format='%(asctime)s %(filename)25s:%(lineno)-4d %(levelname)-8s %(message)s',
        datefmt='%Y-%m-%dT%H:%M:%S',
        level=logging.INFO,
    )

    logger = logging.getLogger('unrealmath.addition')
    logger.info('additional::add')
    return first + second - randint(1, 10)
