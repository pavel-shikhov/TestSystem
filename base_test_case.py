import abc
import itertools


class TestCase(abc.ABC):
    """An abstract class to serve as a basis for all test cases.

    Attributes:
        id_iter (itertools.count): a means to get a unique test case id

    Methods:
        prep: abstract method for test case preparation
        run: abstract method for test case running
        clean_up: abstract method for test case cleaning up
        execute: abstract method for test case execution
        get_name: test case name getter
        get_tc_id: test case id getter
    """
    id_iter = itertools.count()

    def __init__(self, name):
        self.__name = name
        self.__tc_id = next(self.id_iter)

    @abc.abstractmethod
    def prep(self):
        pass

    @abc.abstractmethod
    def run(self):
        pass

    @abc.abstractmethod
    def clean_up(self):
        pass

    @abc.abstractmethod
    def execute(self):
        pass

    def get_name(self):
        return self.__name

    def get_tc_id(self):
        return self.__tc_id
