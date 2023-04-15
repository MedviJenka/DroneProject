import logging
from datetime import datetime
from core.infrastructure.constants.data import LOG


def log(text='', level=logging.INFO) -> callable:

    """"
    logger method
    :params: level ........... logging level, debug, info, etc...
             text ............ text displayed in logger
    """

    _time = datetime.now()
    time_format = f'{_time: %A | %d/%m/%Y | %X}'
    logging.basicConfig(filename=LOG,
                        datefmt=time_format,
                        format=f'%(levelname)s:{time_format} .......... %(message)s',
                        level=level)
    match level:
        case logging.INFO:
            logging.info(text)
        case logging.DEBUG:
            logging.debug(text)
        case logging.ERROR:
            logging.error(text)
        case logging.CRITICAL:
            logging.critical(text)
        case logging.FATAL:
            logging.fatal(text)
        case _:
            raise Exception('no such logging level')
