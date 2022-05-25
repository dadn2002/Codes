import math
import Functions
from io import StringIO
import re
import sys
import numpy as np
import sympy as sym
import scipy.linalg
import pickle
import os


# The collections of classes and functions of group theory, my main objective is to define most of the major groups and
# some computations around Subgroups, Kernells, Isomorphisms, Homomorphisms, Orders relationships, Equivalence Classes,
# Commutator of groups, Group Actions and other problems.
# The list of groups that i'll add in this file is: Ciclic, Symmetric, PGL/PSL, GL, K, Lie Groups,


class Ciclic:
    # The Classic Ciclic Group, defined by G = {e, a, a^2, a^3, ..., a^(|G|-1)}
    # Ciclic(a, b) means element of order a in the ciclic group of order b.
    # General Proprieties:
    # if H<G is a proper subgroup of G, so gcd(|G|,|H|) != 1
    # Fermat Theorem: be G = {0,1,2,3,...,p-1}, so G'={1,2,3,...,p-1} and for all g' in G', we have:
    # g'^|G'|=e_(G'), numerically: g^(p-1)=1 mod p.
    #
    #
    def __init__(self, n, g=1):
        if n == 'null':
            self.element = 'Ciclic'
        else:
            self.element = int(n % g)
        self.grouporder = g

    def value(self):
        # The function that return the parameters of some object
        return [self.element, self.grouporder]

    def group(self):
        # The function list all elements, not all that useful but whatever
        list1 = []
        for i in range(self.grouporder):
            list1.append(i)
        return list1

    def __add__(self, other):
        # G(+)={0,1,2,3,4,5,6,...,p-1}
        if self.grouporder != other.grouporder:
            # Return error if not from same group
            return Ciclic(0, -1)
        else:
            # Addition mod grouporder
            return Ciclic((self.element + other.element) % self.grouporder, self.grouporder)

    def __mul__(self, other):
        # G(*)={1,2,3,4,5,6,7,8,9,10,...,p} is the group of integers g s.t gcd(p,g)=1. In this case, we set __mul__ to
        # be a multiplication of two element in the group G(+)
        if self.grouporder != other.grouporder:
            # Return error if not from same group
            return Ciclic(0, -1)
        else:
            # Multiplication mod grouporder
            return Ciclic((self.element * other.element) % self.grouporder, self.grouporder)

    def __sub__(self, other):
        if self.grouporder != other.grouporder:
            # Return error if not from same group
            return Ciclic(0, -1)
        else:
            # Subtration mod grouporder
            return Ciclic(self.element - other.element, self.grouporder)

    def __truediv__(self, other):
        # Defined for G(+)
        if self.grouporder != other.grouporder or Functions.composite(self.grouporder):
            # Return error if not from same group
            return Ciclic(0, -1)
        else:
            # Division mod group order
            aciclic = self.element
            while not (aciclic / other.element).is_integer():
                aciclic += self.grouporder
            return Ciclic((aciclic / other.element) % self.grouporder, self.grouporder)

    def subgroups(self):
        # Find the generators of non-trivial subgroups H<G
        subgrouplist = []
        for i in range(2, self.grouporder):
            if math.gcd(i, self.grouporder) != 1:
                subgrouplist.append(i)
        return subgrouplist

    def subgroupaddgenerator(self):
        # Return the list of subgroups of G
        subgrouplist = self.subgroups()
        subgroupH = []
        for i in range(len(subgrouplist)):
            subgroupHaux = [0]
            p = 0
            for j in range(self.grouporder):
                p = (p + subgrouplist[i]) % self.grouporder
                if p == subgroupHaux[0]:
                    break
                subgroupHaux.append(p)
            subgroupH.append(subgroupHaux)
        return subgroupH


class Symmetric:
    # Defined as the group of permutations of a set over itself, i.e, the collection of all bijective maps. Here we
    # define the elements as S_n = {e,a,b,c,d,...,g,g^2,g^3,...,ag,ag^2,ag^3,...,bg,bg^2,bg^3,...} were we have elements
    # of order 2 and one of order.
    def __init__(self, n, g=1):
        # We define the elements of this group as n = (1 6 2 7 9 1 11 34 13) the one-line notation, the input form is
        # the list input = 1 3 2 1 4, spaced numbers as a string type variable, turning them into list and placing in
        # self.x. And g is the number of points that can be permuted in thus function set, not all that useful but
        # will be important for some subgroups verifications later on. Return error if we have repetitions of elements
        # in n.
        if n == 'null':
            self.element = 'Symmetric'
        else:
            self.element = n.split()
            # print("debug2", self.element)
        self.grouporder = g

    def value(self):
        return [self.element, self.grouporder]

    def __mul__(self, other):
        # the operation that we define in this group, be g=(12357) and g'=(25413), two elements of S_7, the product g*g'
        # is a composition of functions from right to left: g*g'= (1 5 4 2 7), the element 3 cicles to 3 and here's the
        # composition.
        # Need to insert disjoint cicles multiplication in this boy, for now it does not understand good that
        if self.grouporder != other.grouporder:
            # Return error if not from same group
            return Ciclic(0, -1)
        else:
            # Function composition in S_n
            value = []
            value1 = []
            value2 = []
            test = False
            temp1 = other.element[0]
            i = 0
            for j in range(len(self.element)*len(other.element)):
                # print('j', j)
                if Functions.search(value1, temp1) == -1:
                    # print(value1)
                    value1.append(temp1)
                    # value1.sort()
                if Functions.search(other.element, temp1) != -1:
                    temp2 = other.element[int((Functions.search(other.element, temp1)+1) % len(other.element))]
                else:
                    temp2 = temp1
                if Functions.search(self.element, temp2) != -1:
                    temp3 = self.element[int((Functions.search(self.element, temp2)+1) % len(self.element))]
                    # print(temp3)
                else:
                    temp3 = temp2
                # print(temp1)
                # print(temp2)
                # print(temp3)
                if temp3 == temp1:  # Remove the fixed permutations
                    i += 1
                    temp1 = other.element[int((Functions.search(other.element, temp1) + i) % len(other.element))]
                    value1 = []
                elif Functions.search(value1, temp3) != -1:  # Verify if our output is in our cicle
                    temp4 = value1.copy()
                    temp5 = []
                    temp4.sort()
                    for i in range(len(value)):
                        temp5.append(value[i].copy())
                        temp5[i].sort()
                    # print('temp5', temp5)
                    # print('temp4', temp4)
                    if Functions.search(temp5, temp4) != -1:  # Verify if our cicle isn't repeating
                        i += 1
                        temp1 = other.element[int((Functions.search(other.element, temp1) + i) % len(other.element))]
                        value1 = []
                    else:
                        temp1 = other.element[int((Functions.search(other.element, temp1) + i) % len(other.element))]
                        # print(value)
                        # print('debug', temp1)
                        value.append(value1)
                        # print('value1', value1)
                        value1 = []
                else:  # In the case that our output isn't in our cicle, restart with him.
                    if Functions.search(value1, temp3) == -1:
                        # value.append(temp3)
                        temp1 = temp3
                # print(value)
                # print('')
                # print(value)
            # print(value)  # The list form, easy use
            value = str(value).replace("['", '(').replace("']", ')').replace("[", '').replace("]", '').replace(",", '').replace("'", '')
            print(value)  # The parenthesis form
            return Symmetric(value, self.grouporder)  # Returning as a Symmetric element, but with a parenthesis in the way


def isomorphism(element, string):
    x = element.value()[0]
    y = element.value()[1]
    if string == 'CiclicMul':
        # Return the smallest G'={a_1,a_2,...,a_n} | gcd(a_1,|G|)=1 and |G'(*)| = |G(+)|
        value = [1]
        counter = 0
        ay = 1
        while counter != y:
            counter = 1
            value = [1]
            ay += 1
            for i in range(2, ay):
                if math.gcd(y, i) == 1:
                    counter += 1
                    value.append(i)
        if x == 'Ciclic':
            # return and isomorphic example.
            return [value, ay]
        elif type(x) == int:
            # return the element x in the isomorphic G'(*) group
            return value[x]


a = Symmetric('4 3 5 1 2 7 6', 10)
b = Symmetric('1 7 2 4 6 3 5', 10)
print((a*b).value())
# a = Ciclic(9, 10)
# b = Ciclic(4, 10)
# print(a.value())
# print(b.value())
# print(a.subgroups())
# print(a.subgroupaddgenerator())
# c  = Ciclic(4, 12)
# d = Ciclic('null', 12)
# print(c.group())
# print(isomorphism(d, 'CiclicMul'))
# print(isomorphism(c, 'CiclicMul'))
