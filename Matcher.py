"""

   Project : optima_register
   Matcher.py created by Louise Naud
   On : 9/3/17
   At : 2:04 PM
   
"""

import abc


class Matcher(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, im1, im2, solver, params, matcher_type="ROF"):
        self._solver = solver
        self._params = params
        self._type = matcher_type
        self._im1 = im1
        self._im2 = im2

    def get_matcher_type(self):
        """
        Method to return the type of Matcher we are using.
        :return:
        """
        return self._type

    def get_solver(self):
        """
        Method to return the type of Matcher we are using.
        :return:
        """
        return self._solver

    def set_solver(self, solver):
        """
        Method to return the type of Matcher we are using.
        :return:
        """
        self._solver = solver

    @abc.abstractmethod
    def solve(self):
        """
        Method to solve the .
        :return:
        """
        pass

