"""Main module of the fourth task."""
import os
import re
import logging.config
import base_test_case


class TestRunner:
    """The program's main class that runs all tests in the specified directory

    Attributes:
        testsOverall (number): counter for tests to be run
        testsSuccessful (number): counter for successful tests
        logger (Logger): logger configured in logging.conf.
        log_file_name (string): logging configuration file's name

    Methods:
        __create_class_instance: Creates an instance of a specified class class_name and counts all tests to be run.
        run_test_cases_in_directory: Detects and runs all test cases in the specified directory dir_full_path
    """

    testsOverall = 0
    testsSuccessful = 0
    logger = logging.getLogger(__name__)
    log_file_name = 'logging.conf'
    if os.path.isfile(os.path.join(os.path.dirname(os.path.realpath(__file__)), log_file_name)):
        logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=True)
    else:
        print('Error: No logging configuration file.')
        exit(-1)

    def __create_class_instance(self, class_name):
        """Creates an instance of a specified class class_name and counts all tests to be run.

        Args:
          class_name: class to create an instance of

        Returns:
          specified class instance
        """
        module = __import__(class_name)
        if hasattr(module, 'TestCase') and issubclass(module.TestCase, base_test_case.TestCase):
            self.testsOverall += 1
            test_case_name = 'Test' + str(self.testsOverall)
            return module.TestCase(test_case_name)

    def run_test_cases_in_directory(self, dir_full_path):
        """Detects and runs all test cases in the specified directory dir_full_path

        Args:
          dir_full_path: path of the directory with test cases
        """
        for file_name in os.listdir(dir_full_path):
            current_match = re.match(r'^(test_case\d+)\.py$', file_name)
            if current_match is not None:
                class_instance = self.__create_class_instance(current_match.group(0)[:-3])
                result = class_instance.execute()
                if result:
                    self.testsSuccessful += 1
        print('Ran {} tests. Successful: {}, failed: {}. The log file is log.txt.'
              .format(self.testsOverall, self.testsSuccessful, self.testsOverall - self.testsSuccessful))


if __name__ == '__main__':
    runner = TestRunner()
    runner.run_test_cases_in_directory('.')
