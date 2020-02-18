import functools
import inspect
import logging.config
import re

logger = logging.getLogger("mainLogger")
filename_regexp = re.compile(r'.*/(.*\.py)')


def prep_logging_decorator(func):
    """Wraps TestCase's prep() method with logger's calls

    Args:
      func: function to be decorated
    """
    filename = filename_regexp.match(inspect.getmodule(inspect.stack()[1][0]).__file__).group(1)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info('{}: Start preparation'.format(filename))
        func(*args, **kwargs)
        logger.info('{}: Finished preparation'.format(filename))
    return wrapper


def run_logging_decorator(func):
    """Wraps TestCase's run() method with logger's calls

    Args:
      func: function to be decorated
    """
    filename = filename_regexp.match(inspect.getmodule(inspect.stack()[1][0]).__file__).group(1)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info('{}: Start running'.format(filename))
        func(*args, **kwargs)
        logger.info('{}: Finished running'.format(filename))
    return wrapper


def clean_up_logging_decorator(func):
    """Wraps TestCase's clean_up() method with logger's calls

    Args:
      func: function to be decorated
    """
    filename = filename_regexp.match(inspect.getmodule(inspect.stack()[1][0]).__file__).group(1)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info('{}: Start cleaning up'.format(filename))
        func(*args, **kwargs)
        logger.info('{}: Finished cleaning up'.format(filename))
    return wrapper


def execute_logging_decorator(func):
    """Wraps TestCase's execute() method with logger's calls

    Args:
      func: function to be decorated
    """
    filename = filename_regexp.match(inspect.getmodule(inspect.stack()[1][0]).__file__).group(1)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info('*** {}: START EXECUTING ***'.format(filename))
        result = func(*args, **kwargs)
        logger.info('{}: Finished executing'.format(filename))
        return result
    return wrapper
