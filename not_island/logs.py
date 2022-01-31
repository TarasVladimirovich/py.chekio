import logging
import sys

logging.basicConfig(format='%(asctime)s %(filename)25s:%(lineno)-4d %(levelname)-8s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO,
                    handlers=[logging.StreamHandler(sys.stdout)],
                    )