MOD = (10 ** 9) + 7

T = int(raw_input())

for case_ in xrange(T):
    n, m = map(int, raw_input().split())

    a = m / n
    b = m % n
    mini = ((n - b) * pow(a, 2, MOD) + b * pow(a + 1, 2, MOD)) % MOD
    maxi = pow(m, 2, MOD)

    print maxi % MOD, mini % MOD

'''
^^^TEST^^^
1
11 2021
-------
4084441 371315
$$$TEST$$$
'''
