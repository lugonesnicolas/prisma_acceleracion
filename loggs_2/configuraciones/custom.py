import logging
import logging.config

logging.config.fileConfig(fname='custom.conf', disable_existing_loggers=False)

logger=logging.getLogger(__name__)

logger.debug('Este es un mensaje de debug')