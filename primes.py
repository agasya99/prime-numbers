#!/bin/env python
import math
import time

def run(max):
    primes = []
    if max <= 1:
        return primes
    for i in xrange(2, max + 1):
        if i % 2 == 0:
            if i == 2:
                primes.append(i)
        else:
            composite = False
            z = int(math.sqrt(i))
            for j in xrange(3, z + 1):
                if i % j == 0:
                    composite = True
                    break
            if not composite:
                primes.append(i)
    return primes

max = 1000000
start_time = time.time()
primes = run(max)
total_time = time.time() - start_time

for num in primes:
    print num

print 'Total time: %s seconds' % (total_time)
