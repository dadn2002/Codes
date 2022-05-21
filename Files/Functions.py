import math
import sys
import numpy as np
import pickle
import os
import base64
from google_auth_oauthlib.flow import InstalledAppFlow
import googleapiclient.discovery
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

# run pip install google-auth-oauthlib in your python3 terminal to get googleauth lib
# MAX DIVISION METHODS IS n = 2147483647
sys.setrecursionlimit(2147483647)  # Just to be safe, linalg in facdifsquare need really deep recursion


def gmail(text):
    """ SETTING UP THE GMAIL FEEDBACK SPAM SYSTEM """
    SCOPES = ['https://www.googleapis.com/auth/gmail.send',
              'https://www.googleapis.com/auth/gmail.modify']
    home_dir = os.path.expanduser('~')
    # RUN THIS SEQUENCE OF COMMANDS AT LEAST ONE TIME BEFORE USAGE
    # json_path = os.path.join(home_dir, 'Downloads', 'credentials.json')
    # flow = InstalledAppFlow.from_client_secrets_file(json_path, SCOPES)
    # creds = flow.run_local_server(port=0)
    # pickle_path = os.path.join(home_dir, 'gmail.pickle')
    # with open(pickle_path, 'wb') as token:
    #     pickle.dump(creds, token)
    # Get the path to the pickle file
    pickle_path = os.path.join(home_dir, 'gmail.pickle')
    creds = pickle.load(open(pickle_path, 'rb'))
    service = googleapiclient.discovery.build('gmail', 'v1', credentials=creds)
    my_email = 'nmdavialves@gmail.com'
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'python ' + str(datetime.datetime.now())
    msg['From'] = f'{my_email}'
    msg['To'] = f'{my_email}'
    msgPlain = str(text)
    # msgHtml = '<b>This is my first email!</b>' # Turn characters 'thick'
    msg.attach(MIMEText(msgPlain, 'plain'))
    # msg.attach(MIMEText(msgHtml, 'html'))
    raw = base64.urlsafe_b64encode(msg.as_bytes())
    raw = raw.decode()
    body = {'raw': raw}

    message1 = body
    message = (
        service.users().messages().send(
            userId="me", body=message1).execute())
    print('Message Id: %s' % message['id'])


def search(xlist, platform):
    """ Search if given element platform exists in xlist, return the index where it's found or -1 if not found """
    for i1 in range(len(xlist)):
        if xlist[i1] == platform:
            return i1
    return -1


def isqrt(x):
    _1_50 = 1 << 50  # 2**50 == 1,125,899,906,842,624
    """Return the integer part of the square root of x, even for very
    large integer values."""
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    if x < _1_50:
        return int(math.sqrt(x))  # use math's sqrt() for small parameters
    n = int(x)
    if n <= 1:
        return n  # handle sqrt(0)==0, sqrt(1)==1
    # Make a high initial estimate of the result (a little lower is slower!!!)
    r = 1 << ((n.bit_length() + 1) >> 1)
    while True:
        newr = (r + n // r) >> 1  # next estimate by Newton-Raphson
        if newr >= r:
            return r
        r = newr


def facsmall(n, s, listp=None):
    """ Factorization of n if n is prod of small primes (up to s) """
    if listp is None:
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
    # print(listp)
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


def row_echelon(a, p=-1):
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
        b = row_echelon(a[:, 1:], p=p)
        # and then add the first zero-column back
        with open("Text/matriz.txt", "a", encoding='utf-8') as f1:
            f1.write(str(b) + "\n")
        return np.hstack([a[:, :1], b])

    # if non-zero element happens not in the first row,
    # we switch rows
    if i > 0:
        ith_row = a[i].copy()
        a[i] = a[0]
        a[0] = ith_row

    # we divide first row by first element in it
    a[0] = (a[0] / a[0, 0]) % 2
    # we subtract all subsequent rows with first row (it has 1 now as first element)
    # multiplied by the corresponding element in the first column
    a[1:] -= a[0] * a[1:, 0:1]
    if p != -1:
        a[1:] = a[1:] % p  # The line where we reduce mod p

    # we perform REF on matrix from second row, from second column
    b = row_echelon(a[1:, 1:], p=p)

    # we add first row and first (zero) column, and return
    # A = np.array([[1, 2, 2],
    #               [1, 4, 4],
    #               [1, 2, 1]], dtype='float')
    #
    # print(Functions.row_echelon(A))
    return np.vstack([a[:1], np.hstack([a[1:, :1], b])])


def gauss(a1, b1, c, d):
    """ Gauss Elimination for Ax=b where x has non-limited variables"""
    # a = matrix, b = vector result, c = limited variables, d = operations mod d
    # print("BEGIN")
    # print(a1)
    # print(b)
    # print(c)
    # print(solution)
    ad = []
    r = np.zeros((len(a1[0]), 1))
    for i in range(len(a1[0])):
        if search(c, i) == -1:
            ad.append(i)
    for x in range(len(ad)):
        # print(x)
        a = a1.copy()  # For some reason python treat matrix usual equalities as some
        b = b1.copy()  # kind of function which affects the original.
        # print("BEFORE")
        # print(a)
        # print(aux)
        solution = np.zeros((len(a[0]), 1))
        for l in range(len(a[0])):
            for k in range(len(a)):
                # print("l: ", l)
                if l == ad[x]:
                    # print(k, l, ad[x], "Put 1")
                    a[k][l] = 1 * a[k][l]
                    solution[l][0] = 1
                elif search(ad, l) != -1:
                    # print(k, l, ad[x], "Put 0")
                    a[k][l] = 0
                    solution[l][0] = 0
        # print("AFTER")
        # print(a)
        # print(aux)
        # a = row_echelon(a, p=2)
        # print("First canonical")
        for i in range(len(a) - 1, -1, -1):  # Actually this -1 made my went insane
            for j in range(0, len(a[0]) - 1):
                if a[i][j] != 0:
                    # print(i, j)
                    # c[search(c, j)] = -1
                    # print("Found: ", i)
                    # print("Found: ", j)
                    # print(b[i])
                    # print(np.transpose(solution))
                    for n in range(j + 1, len(a[0])):
                        # print(b)
                        # print(a)
                        # print('')
                        # print(np.transpose(solution))
                        # print('[' + str(a[i][:]) + ']')
                        # print(solution[n])
                        # print(x, i, j, n, a[i][n], b[i][0])
                        b[i][0] = int((b[i][0] - (a[i][n] * solution[n]) % d) % d)
                        # print(b[i][0])
                    # print('')
                    # print('[' + str(a[i][:]) + ']')
                    solution[j][0] = b[i][0]
                    # print(b[i])
                    b[i][0] = 0
                    # print(np.transpose(solution))
                    # print('[' + str(a[i][:]) + ']')
                    # print(b[i])
                    break
        # print(np.transpose(solution))
        with open("Text/" + 'debug' + ".txt", "a", encoding='utf-8') as f1:
            f1.write(str(x) + "|" + str(len(ad)) + "|" + str(np.transpose(solution)))
            f1.write('\n')
        r = np.concatenate((r, solution), axis=1)
        # print(np.transpose(a.dot(solution)))
        # print("END")
        # print(a)
        # print(c)
        # print(solution)
    return np.transpose(np.delete(r, 0, 1))


def facdifsquare(n, s, list1=None) -> int:
    """ Factorization of n using x^2-y^2=(x+y)(x-y) identity"""
    # Use this function in a smart way, big n with small s and small n with big s... Does not mix or your computer may
    # The parameter s isn't need but im lazy to swap it along the code, be free to give any value to him.
    # list1 is type []
    # OPTIMIZED WITH LINEAR ALGEBRA
    asss = math.log(n, math.e) * math.log(math.log(n, math.e), math.e)
    s = int(math.ceil(pow(math.e, isqrt(asss))))
    iiii = int(math.ceil(pow(math.e, isqrt(2 * asss))))
    if n == 1:
        return list1
    if list1 is None:
        list1 = []
    listp = primelist(s)
    if n > pow(listp[len(listp) - 1], 2):
        # If the number is too big for us to check each case.
        # Basically we need Linear Algebra for that
        mc = math.ceil(isqrt(n))
        listk = []
        listj = []
        j = 0
        for i in range(0, iiii):
            listaux = []
            listaux = facsmall(pow((mc + i) % n, 2) % n, s, listp)
            with open("Text/" + 'debug' + ".txt", "a", encoding='utf-8') as f1:
                straux = str(i) + ":" + str(listaux)
                f1.write(straux)
                f1.write('\n')
            if listaux[len(listaux) - 1] <= listp[len(listp) - 1]:  # The biggest prime lesser than s
                listk.append(int(pow((mc + i) % n, 2) % n))
                listj.append(mc + i)
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
        # print(listk)
        if len(listk) < len(listp):
            return -1  # Actually this error is due to no equations
        listaux2 = np.zeros((len(listp), len(listp) + 5))
        for i in range(0, len(listp) + 5):
            l = 0
            for k in range(0, len(listp)):
                listaux3 = facsmall(listk[i], s, listp)
                if listaux3[l] == listp[k]:
                    listaux2[k][i] = int(listaux3.count(listp[k]) % 2)
                    l = l + listaux3.count(listp[k])
                if l > len(listaux3) - 1:
                    break
                # print(l)
                # print(i, " ", k)
                # print(listp)
                # print(listaux3)
                # print(int(listaux2[k][i]))
                # print('')
        # listaux2 = row_echelon(listaux2)
        listaux4 = np.zeros((len(listp), 1))
        listaux5 = np.zeros((1, len(listp)))
        listaux2 = row_echelon(listaux2, p=2)
        l1 = []
        for i in range(len(listp)):
            for j in range(len(listp) + 5):
                if listaux2[i][j] == 1:
                    l1.append(j)
                    break
        # print(listaux4)
        c = gauss(listaux2, listaux4, l1, 2)
        # print(listk)
        # print(listj)
        for i in range(len(c)):
            test = 1
            test2 = 1
            for j in range(len(c[0])):
                if c[i][j] != 0:
                    # print(listk[j])
                    test = test * listk[j]
                    test2 = test2 * listj[j]
            # print(test)
            test = isqrt(test)
            gcdtest = math.gcd(n, int(test2 - test))
            # print(c)
            # print(listj)
            # print(listk)
            # print(test)
            # print(test2)
            # print(gcdtest)
            # print(gcdtest)
            if gcdtest != 1 and gcdtest != n:
                # print("Non Trivial Factor: ", gcdtest)
                list1.append(gcdtest)
                return facdifsquare(int(n / gcdtest), s, list1)
            else:
                with open("Text/debug.txt", "a", encoding='utf-8') as f1:
                    f1.write(str(i) + str(gcdtest))
        list1.append(n)
        return list1
        # print(c)
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
                        list1 = (facdifsquare(d1, s, list1))
                    if composite(d2):
                        while search(list1, d2) != -1:
                            del (list1[search(list1, d2)])
                        list1 = (facdifsquare(d2, s, list1))
                    # list1 = list(set(list1))
                    list1.sort()
                    return list1
        list1.append(n)
        list1.sort()
    # list1 = list(set(list1))
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
