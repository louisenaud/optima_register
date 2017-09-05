"""

   Project : optima_register
   Solver created by Louise Naud
   On : 9/3/17
   At : 2:07 PM
   
"""

import abc


class Solver(object):
    __metaclass__ = abc.ABCMeta



    @abc.abstractmethod
    def get_solver_type(self):
        """
        Method to return the type of Solver we are using.
        :return:
        """
        pass

    @abc.abstractmethod
    def set_solver_type(self):
        """
        Method to set the type of Solver we are using.
        :return:
        """
        pass