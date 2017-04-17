#!/usr/bin/python
import random
from datetime import datetime

def getRandomNumber():
    return random.randrange(1, 101)

def getRandomSubset():
    return [xrange(1,101) for i in sorted(random.sample(xrange(len(xrange(1,101))), 4))]

if __name__ == '__main__':
    random.seed(datetime.now())
    print(getRandomNumber())
    print(getRandomSubset())
