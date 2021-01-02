import logging
from functools import wraps


def create_logger():
    # create a logger object
    logger = logging.getLogger('exc_logger')
    logger.setLevel(logging.INFO)

    # create a file to store all the
    # logged exceptions
    logfile = logging.FileHandler('exc_logger.log')

    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)

    logfile.setFormatter(formatter)
    logger.addHandler(logfile)

    return logger


logger = create_logger()

# you will find a log file
# created in a given path
print(logger)


def exception(logger):
    # logger is the logging object
    # exception is the decorator objects
    # that logs every exception into log file
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            try:
                return func(*args, **kwargs)

            except:
                issue = "exception in " + func.__name__ + "\n"
                issue = issue + "-------------------------\
                ------------------------------------------------\n"
                logger.exception(issue)
            raise

        return wrapper

    return decorator


@exception(logger)
def divideStrByInt():
    return "krishna" / 7


# Driver Code
if __name__ == '__main__':
    divideStrByInt()
