"""

   Project : optima_register
   Matcher_TVL1.py created by Louise Naud
   On : 9/3/17
   At : 2:05 PM
   
"""

from Matcher import Matcher
from Solver import Solver

class Matcher_TVL1(Matcher):
    """

    """
    def __init__(self, solver, params):
        self._solver = solver
        self._params = params
        self._type = "TVL1"

    def solve(self):
        return

