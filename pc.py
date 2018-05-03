import random
from results import *
from roll import *

def pc():
    d0 = roll()
    d1 = roll()
    d2 = roll()
    d3 = roll()
    d4 = roll()
    value = results(d0,d1,d2,d3,d4)
    return value
