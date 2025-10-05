
from ast import arg


class Calculator():
    def add(self, *args):
        return sum(args)