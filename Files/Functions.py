import math
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve
import sys
from scipy import linalg


def search(xlist, platform):
    """ Search if given element platform exists in xlist, return the index where it's found or -1 if not found """
    for i1 in range(len(xlist)):
        if xlist[i1] == platform:
            return i1
    return -1


def facsmall(n, s):
    """ Factorization of n if n is prod of small primes (up to s) """
    listp = primelist(s)
    list1 = []
    for i in range(0, len(listp)):
        while (n / listp[i]).is_integer():
            list1.append(listp[i])
            n = int(n / listp[i])
    if n > 1:
        list1.append(n)
    if not list1:
        list1 = [n]
    list1.sort()
    return list1


def primelist(n):
    """ Gives a list of all primes up to n """
    listp = [2]
    for i in range(2, n):
        p = True
        for j in range(0, len(listp)):
            if (i / listp[j]).is_integer():
                p = False
        if p:
            listp.append(i)
    listp.sort()
    return listp


def composite(n):
    """ Checks if n is a prod of two primes without checking all the divisors """
    if n == 2:
        return False
    for a in range(1, 1000):
        q = n - 1
        k = 0
        if n % 2 == 0 or 1 < math.gcd(n, a) < n:
            # print("First Case")
            return True
        else:
            l = n
            while n - 1 != pow(2, k) * q:
                l = l / 2
                q = n / l
                k = k + 1
            b = pow(a, q) % n
            if b % n == 1:
                q = q
            else:
                for i in range(0, k - 1):
                    if b % n == -1:
                        # print("Third Case")
                        break
                    b = b * b % n
    # print("Composite")
    return False


def congruence(a, b, c, d, e, f):
    """ Solve Modular Equations of the form: a^b = c^d + e mod f """

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


def row_echelon(a):
    """ Return Row Echelon Form of matrix A """
    # if matrix A has no columns or rows,
    # it is already in REF, so we return itself
    r, c = a.shape
    if r == 0 or c == 0:
        return a

    # we search for non-zero element in the first column
    for i in range(len(a)):
        if a[i, 0] != 0:
            break
    else:
        # if all elements in the first column is zero,
        # we perform REF on matrix from second column
        b = row_echelon(a[:, 1:])
        # and then add the first zero-column back
        return np.hstack([a[:, :1], b])

    # if non-zero element happens not in the first row,
    # we switch rows
    if i > 0:
        ith_row = a[i].copy()
        a[i] = a[0]
        a[0] = ith_row

    # we divide first row by first element in it
    a[0] = a[0] / a[0, 0]
    # we subtract all subsequent rows with first row (it has 1 now as first element)
    # multiplied by the corresponding element in the first column
    a[1:] -= a[0] * a[1:, 0:1]

    # we perform REF on matrix from second row, from second column
    b = row_echelon(a[1:, 1:])

    # we add first row and first (zero) column, and return
    # A = np.array([[1, 2, 2],
    #               [1, 4, 4],
    #               [1, 2, 1]], dtype='float')
    #
    # print(Functions.row_echelon(A))
    return np.vstack([a[:1], np.hstack([a[1:, :1], b])])


def axb(a, b, p):
    """ Solve Ax=b mod p when the usual np.linalb.solve or .stdsqr or other methods does not work properly"""
    # The main purpose of this function is facdifsquare in a optimal way
    


def facdifsquare(n, list1: int, s) -> int:
    """ Factorization of n using x^2-y^2=(x+y)(x-y) identity"""
    # Use this function in a smart way, big n with small s and small n with big s... Does not mix or your computer may
    # crash due to overflow (I don't want to prevent that so be aware)
    # list1 is type []
    # actually not optimized for Linear Algebra.
    listp = primelist(s)
    if n > pow(listp[len(listp) - 1], 2):
        # If the number is too big for us to check each case.
        # Basically we need Linear Algebra for that
        mc = math.ceil(math.sqrt(n))
        listk = []
        j = 0
        for i in range(0, 100000):
            listaux = []
            listaux = facsmall(pow(mc+i, 2) % n, s)
            if listaux[len(listaux)-1] <= listp[len(listp)-1]:  # The biggest prime lesser than s
                listk.append(int(pow(mc + i, 2) % n))
                j = j + 1
                # print(mc + i)
                # print(pow(mc + i, 2) % n)
                # print(listaux)
                # print(listaux[len(listaux) - 1])
                # print(listp[len(listp)-1])
                # print(len(listp))
                # print('')
            if j == len(listp) + 5:  # Actually a small increment to be sure that we don't have many Solutions
                break
        print(listk)
        listaux2 = np.zeros((len(listp), len(listp)+5))
        for i in range(0, len(listp)+5):
            l = 0
            for k in range(0, len(listp)):
                listaux3 = facsmall(listk[i], s)
                if listaux3[l] == listp[k]:
                    listaux2[k][i] = int(listaux3.count(listp[k]) % 2)
                    l = l + listaux3.count(listp[k])
                if l > len(listaux3)-1:
                    break
                # print(l)
                # print(i, " ", k)
                # print(listp)
                # print(listaux3)
                # print(int(listaux2[k][i]))
                # print('')
        print("MATRIX DONE")
        # listaux2 = row_echelon(listaux2)
        listaux4 = np.zeros((len(listp), 1))
        listaux5 = np.zeros((1, len(listp)))
        for i in range(0, len(listp)):
            for j in range(0, len(listp) + 5):
                da = float(listaux2[i][j])
                if not da.is_integer():
                    listaux2[i][j] = listaux2[i][j]*2
                if listaux2[i][j] % 2 == 0:
                    listaux2[i][j] = 0
                else:
                    listaux2[i][j] = 1
        print('')
        print(listaux2)
        print(listaux4)
        c = np.linalg.lstsq(listaux2, listaux4)
        for i in range(15):
            print("x", i, ": ", c[0][i])

    else:
        # If the number is small enough for us to check each case until solve the identity
        while n % 2 == 0:
            list1.append(2)
            n = int(n / 2)
        for j in range(0, len(listp)):
            for i in range(1000):
                if math.sqrt(listp[j] * n + pow(i, 2)).is_integer():
                    if j == 0:
                        d1 = int(math.sqrt(listp[j] * n + pow(i, 2))) - i
                        d2 = int(math.sqrt(listp[j] * n + pow(i, 2))) + i
                    else:
                        d1 = math.gcd(int(math.sqrt(listp[j] * n + pow(i, 2))) - i, n)
                        d2 = math.gcd(int(math.sqrt(listp[j] * n + pow(i, 2))) + i, n)
                    list1.append(d1)
                    list1.append(d2)
                    # print("i: ", i, " j: ", j, " d1: ", d1, " d2: ", d2) DEBUG PRINT
                    if composite(d1):
                        while search(list1, d1) != -1:
                            del (list1[search(list1, d1)])
                        list1 = (facdifsquare(d1, list1, s))
                    if composite(d2):
                        while search(list1, d2) != -1:
                            del (list1[search(list1, d2)])
                        list1 = (facdifsquare(d2, list1, s))
                    list1.sort()
                    return list1
        list1.append(n)
        list1.sort()
    return list1


def pollard(n):
    """ Factorization of n if n can be writen as a product pq such that p-1 or q-1 is factored with small primes """
    a = 2
    i = 2
    while i > 1:
        a = pow(a, i) % n
        d = math.gcd(a - 1, n)
        if 1 < d < n:
            return d
        i = i + 1
