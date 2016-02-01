#!/usr/bin/env python

class Node(object):
    def isTerminal(self):
        return False
    
    def isInternal(self):
        return False
    
class TerminalNode(Node):
    def isTerminal(self);
        return True

class InternalNode(Node):
    def isInternal(self);
        return True

class MTZDD(object):
    def __init__(self):
        N = set()
        H = {}
        L = {}
    
    def addINode(self, node, low, high):
        H[node] = high
        L[node] = low
        N.add(node)

    def addTNode(self, node):
        N.add(node)

    def Pa(self, node):
        pass
        
t = [ TNode(0), TNode(1), TNode(5), TNode(7) ]
i = [ INode(1), Inode(2), Inode(2), Inode(3), Inode(3), Inode(4) ]

p = MTZDD()

p.addINode(i[0], i[1], i[2])
