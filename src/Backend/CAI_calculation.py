import math

def geomean(xs):
    return math.exp(math.fsum(math.log(x) for x in xs) / len(xs))
