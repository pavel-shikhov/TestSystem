### Test Case System
This is a test system that runs all test cases named `test_case\d+.py` and situated in the current folder.

All test cases must extend an abstract class `base_test_case.py` and implement its 3 helper abstract methods:
* `prep()` to perform test case preparation
* `run()` to perform test case main actions
* `clean_up()` to do the cleanup work once the test's running is through

Each test case must also implement the `execute()` abstract method which serves as an orchestrator for all the helper methods.

The prerequisite for test case system's usage is the `logging.conf` file that sets all log records to be written into a specified file.

Full documentation is available in the source code.

To run all tests, the `TestRunner.py` should be launched without arguments.
