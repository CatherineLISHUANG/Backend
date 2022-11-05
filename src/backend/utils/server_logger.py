import os
import logging


logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger()
logger.setLevel('INFO')

if os.getenv('LOG_LEVEL'):
    logger.setLevel(os.getenv('LOG_LEVEL'))
