import sys
from random import randint

T = int(sys.argv[1])

print T

for case_ in xrange(T):
    n = randint(1, 1000)
    m = randint(1, 10 ** 9)

    print n, m

