#!/usr/bin/env python

import math

fi = (1.0+math.sqrt(5.0))/2.0

def fib(n):
    return math.floor((fi**n)/math.sqrt(5.0)+0.5)




if __name__ == "__main__":
    print sum([fib(x) for x in range(3,40,3) if fib(x) < 4000000])
