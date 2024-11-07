import logging.config
import os

config_path = os.path.join(os.path.dirname(__file__), 'logging.ini')
logging.config.fileConfig(config_path)
logger = logging.getLogger('appLogger')
