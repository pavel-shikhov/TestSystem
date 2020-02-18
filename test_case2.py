import errno
import logging
import logging.config
import os

import base_test_case
import decorators
import exceptions


class TestCase(base_test_case.TestCase):
    """Test case that prints all files in the current directory if current time value (in ms) is even.

    Attributes:
        logger (Logger): logger configured in logging.conf.

    Methods:
        prep: Prepares the test execution by checking if the computer's RAM volume is more than 1 GB.
        run: Creates tmp/test file of 1024 KB with random content
        clean_up: Removes previously created file tmp/test
        execute: Executes the test by invoking prep(), run(), clean_up()
    """
    logger = logging.getLogger("mainLogger")

    @decorators.prep_logging_decorator
    def prep(self):
        """Prepares the test execution by checking if the computer's RAM volume is more than 1 GB.

        Raises:
          PreparationException: the computer's RAM volume is less than 1 GB.
        """
        self.logger.info('Check if RAM volume is more than 1 GB.')
        ram_volume = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES') / (1024. ** 3)
        if ram_volume < 1:
            raise exceptions.PreparationException("Computer's RAM should be more than 1 GB")
        self.logger.info("RAM volume is more than 1 GB ({} GB)".format(ram_volume))

    @decorators.run_logging_decorator
    def run(self):
        """ Creates tmp/test file of 1024 KB with random content
        """
        self.logger.info('Start creating tmp/test file of 1024 KB with random content')
        self.__create_file('tmp/test', 1024)
        self.logger.info('Successfully created tmp/test file')

    @decorators.clean_up_logging_decorator
    def clean_up(self):
        """Removes previously created file tmp/test

        Raises:
          OSError: if removal failed.
        """
        self.logger.info('Start removing tmp/test file')
        try:
            os.remove('tmp/test')
            self.logger.info('Successfully removed tmp/test file')
        except OSError:
            raise exceptions.CleaningUpException('Error removing tmp/test')

    @decorators.execute_logging_decorator
    def execute(self):
        """Executes the test by invoking prep(), run(), clean_up()

        Returns::
          True if test passed.
          False if test failed
        """
        self.logger.info("TEST: {}, {}".format(self.get_name(), self.get_tc_id()))
        try:
            self.prep()
            self.run()
            self.clean_up()
            return True
        except exceptions.RunningException:
            self.logger.exception('Running failed: Error creating tmp/test.')
            return False
        except exceptions.CleaningUpException:
            self.logger.exception('Cleaning-up failed: Error removing tmp/test.')
            return False

    def __create_file(self, full_path, size_kb):
        """Creates a file of specified size size_kb in the specified location full_path.

        Args:
          full_path: file location.
          size_kb: file size.

        Raises:
          RunningException: If file creation failed.
        """
        if not os.path.exists(os.path.dirname(full_path)):
            try:
                logging.info("Creating {}".format(full_path))
                os.makedirs(os.path.dirname(full_path))
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise exceptions.RunningException('Error creating tmp/test')
                else:
                    self.logger.info('tmp/test already exists.')
        self.logger.info('Generate random content for tmp/test.')
        with open(full_path, 'wb') as output_file:
            output_file.write(os.urandom(size_kb))
        self.logger.info('Generated random content for tmp/test.')


