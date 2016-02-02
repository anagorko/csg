#!/usr/bin/env python

import unittest, random

class MTZDD(object):
    def __init__(self):
        self.I = {}
        self.T = {}
        self.H = {}
        self.L = {}
        self.N = 0
        self.P = {}
        self.minCache = {}
        
    def Pa(self, node):
        return self.P[node]
    
    def addTNode(self, v, n = -1):
        if (n == -1):
            n = self.N + 1
        if (n > self.N):
            self.N = n

        self.T[n] = v
        return n
    
    def addINode(self, v, l, h, n = -1):
        if (n == -1):
            n = self.N + 1
        if (n > self.N):
            self.N = n

        self.I[n] = v
        self.H[n] = h
        self.L[n] = l
        if not n in self.P:
            self.P[n] = []
        if not h in self.P:
            self.P[h] = []
        if not l in self.P:
            self.P[l] = []
        self.P[h].append(n)
        self.P[l].append(n)
        return n
                    
    @classmethod
    def getExample(cls):
        r = MTZDD()
        
        r.addINode(1, 2, 3, 1)
        r.addINode(2, 4, 5, 2)
        r.addINode(2, 5, 6, 3)
        r.addINode(3, 7, 8, 4)
        r.addINode(4, 8, 9, 5)
        r.addINode(3, 9, 10, 6)
        r.addTNode(0, 7)
        r.addTNode(1, 8)
        r.addTNode(5, 9)
        r.addTNode(7, 10)
        
        return r
        
    @classmethod
    def getRandomRuleDecayDistribution(cls, agents, alpha, p):
        
        pass
    
    def __str__(self):
        r = ''
        
        for id, v in self.I.iteritems():
            r += str(id) + ' ' + str(v) + ' ' + str(self.L[id]) + ' ' + str(self.H[id]) + ' '
        
        r += '0 '
        
        for id, v in self.T.iteritems():
            r += str(id) + ' ' + str(v) + ' '
        
        r += '0'

        return r

    @classmethod
    def fromString(cls, s):
        r = MTZDD()
        
        i = iter(map(int, s.split(' ')))

        n = i.next()
        while n != 0:
            v = i.next()
            l = i.next()
            h = i.next()
            r.addINode(v,l,h,n)
            n = i.next()
        
        n = i.next()
        while n != 0:
            v = i.next()
            r.addTNode(v,n)
            n = i.next()
        
        return r
        
    def __eq__(self, r):
        return self.I == r.I and self.T == r.T and self.H == r.H and self.L == r.L and self.N == r.N and self.P == r.P

    def min(self, t):
        if t in self.minCache:
            return self.minCache[t]
            
        m = set()
        
        for n in self.Pa(t):
            if self.H[n] == t:
                s = set()
                s.add(n)
                m |= s
            else:
                m |= self.min(n)

        self.minCache[t] = m
        
        return m

    def goals(self, t):
        pass
    
    def GS(self):
        pass
        
    def nodes(self, i):
        pass

#
# Unit tests for the MTZDD class
#

class MTZDDTests(unittest.TestCase):
    def singleRuleSerializationTest(self, r):
        "Tests serialization to string and parsing of r"
        p = MTZDD.fromString(str(r))
        
        self.failUnless(r == p)

    def testSerialization(self):
        r = MTZDD.getExample()

        self.singleRuleSerializationTest(r)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
