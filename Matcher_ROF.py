"""

   Project : optima_register
   Matcher_ROF created by Louise Naud
   On : 9/3/17
   At : 2:05 PM
   
"""

from Matcher import Matcher
from Solver import Solver

class Matcher_ROF(Matcher):
    """

    """
    def __init__(self, solver, params, inputs):
        self._type = "ROF"
        self._solver = solver
        self._params = params
        self._inputs = inputs

    def solve(self):
        return
