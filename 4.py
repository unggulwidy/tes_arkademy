import random

nonprimes = set(j for i in range(2, 8) for j in range(i*2, 31, i))
primes = [x for x in range(2, 31) if x not in nonprimes]

def randomize(a):
    randomlist = random.sample(primes, a)
    sumlist = sum(randomlist)
    print('array:', randomlist)
    print('sum:', sumlist)

randomize(6)
