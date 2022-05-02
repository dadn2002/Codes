import math


def composite(n):
    for a in range(100):
        q = 0
        k = 0
        if n % 2 == 0 or 1 < math.gcd(n, a) < n:
            return True
        l = n
        while l % 2 == 0:
            q = q + 1
            l = l / 2
        while n - 1 != 2 ^ k * q:
            k = k + 1
        b = a ^ q % n
        if b % n == 1:
            b = b
        for i in range(0, k - 1):
            if b % n == -1:
                b = b
                break
            b = b * b % n
    return True


def congruence(a, b, c, d, e, f):
    # a^b = c^d + e mod f
    a1 = False
    b1 = False
    c1 = False
    d1 = False
    e1 = False
    f1 = False
    if type(a) == 'int':
        a1 = True
    if type(b) == 'int':
        b1 = True
    if type(c) == 'int':
        c1 = True
    if type(d) == 'int':
        d1 = True
    if type(e) == 'int':
        e1 = True
    if type(f) == 'int':
        f1 = True
    if b == 1:
        #  a = c^d + e mod f
        if e == 0:
            # a = c*d mod f
            # if not composite(f):
            if not d1:
                while a % c != 0:
                    a = a + f
                return (a / c) % f
