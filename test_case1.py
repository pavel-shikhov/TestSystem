import os
import time
import logging.config

import base_test_case
import decorators
import exceptions


class TestCase(base_test_case.TestCase):
    """Test case that prints all files in the current directory if current time value (in ms) is even.

    Attributes:
        logger (Logger): logger configured in logging.conf.

    Methods:
        prep: Prepares the test execution by checking if current time value (in ms) is even
        run: Lists all files in the current directory
        execute: Executes the test by invoking prep(), run()
    """
    logger = logging.getLogger("mainLogger")

    @decorators.prep_logging_decorator
    def prep(self):
        """Prepares the test execution by checking if current time value (in ms) is even

        Raises:
          PreparationException: if current time value (in ms) is odd.
        """
        self.logger.info('Check if current time value (in ms) is even')
        if int(time.time()) % 2 != 0:
            raise exceptions.PreparationException('Exiting because the test case should be launched at an even system '
                                                  'time (in ms).')
            # exit("Exiting because current system time (in ms) is odd.")

    @decorators.run_logging_decorator
    def run(self):
        """Lists all files in the current directory"""
        self.logger.info('Get files from current directory')
        # Will get a NameError if running from inside an interpreter
        files = [f for f in os.listdir(os.path.dirname(os.path.realpath(__file__))) if os.path.isfile(f)]
        self.logger.info('Files from the current directory: {}'.format(files))
        self.logger.info('Print files from the current directory.')
        print(files)

    @decorators.clean_up_logging_decorator
    def clean_up(self):
        pass

    @decorators.execute_logging_decorator
    def execute(self):
        """Executes the test by invoking prep(), run()

        Returns:
          True if test passed.
          False if test failed
        """
        self.logger.info('Test: name: {}, tc_id: {}'.format(self.get_name(), self.get_tc_id()))
        try:
            self.prep()
            self.run()
            return True
        except exceptions.PreparationException:
            self.logger.exception('Preparation failed: Current time value (in ms) must be even.')
            return False


