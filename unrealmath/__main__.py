import logging
import sys

from unrealmath.addition import add
from unrealmath.subtraction import reduce

logger = logging.getLogger('unrealmath')
logger.setLevel(logging.INFO)

console = logging.StreamHandler(sys.stdout)
console.setLevel(logging.INFO)
console.setFormatter(
    logging.Formatter(fmt='%(asctime)s %(filename)25s:%(lineno)-4d %(levelname)-8s %(message)s',
                      datefmt='%H:%M:%S'))

logger.addHandler(console)

if __name__ == '__main__':
    reduce(5, 1)
    add(2, 5)
