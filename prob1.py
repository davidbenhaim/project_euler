#!/usr/bin/env python

if __name__ == "__main__":
    print sum([x*3 for x in range(1,334)]+[x*5 for x in range(1,200) if x%3!=0])

