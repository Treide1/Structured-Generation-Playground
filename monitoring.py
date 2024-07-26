import time
import logging


def print_runtime(func):
    """
    Measure execution time of a function.
    Use as decorator.
    """
    def wrapper_function(*args, **kwargs): 
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f"Runtime: {end_time - start_time}")
    return wrapper_function

def log_runtime(func):
    """
    Log execution time of a function.
    Use as decorator.
    """
    def wrapper_function(*args, **kwargs): 
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        logging.debug(f"Runtime ({func.__name__}): {end_time - start_time}")
    return wrapper_function


def setup_logger(filename: str):
    logger_name = filename.split(".")[0]
    
    logger = logging.getLogger(logger_name)
    logger.setLevel(level=logging.DEBUG)
    fh = logging.FileHandler(filename=filename, mode="w")
    fh_formatter = logging.Formatter(fmt="%(asctime)s - [%(levelname)s] | %(message)s")
    fh.setFormatter(fh_formatter)
    logger.addHandler(fh)
    
    logger.setLevel(logging.DEBUG)

    # Silence other loggers
    for log_name, log_obj in logging.Logger.manager.loggerDict.items():
        if log_name != logger_name:
            log_obj.disabled = True
    
    logging.root = logger
