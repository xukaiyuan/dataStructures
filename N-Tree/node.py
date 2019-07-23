#!/usr/bin/python3

class node:

    def __init__(self, value):
        self._maxChildren = 10
        self._value = value
        self._children = []

    def getValue(self):
        return self._value

    def getChildren(self):
        return self._children

    def searchDown(self, target):
        for child in self._children:
            if(child.getValue() == target):
                return child

        return None

    def addChildren(self, children):
        # children should be in type of list
        for child in children:
            if(self._maxChildren == 0):
                return False
            else:
                self._children.append(child)
                self._maxChildren -= 1

    def deleteChildren(self, children):
        # children should be in type of list
        deleteSet = set(children)
        childrenTmp = self._children[:]
        self._children = []

        for child in childrenTmp:
            if(child in deleteSet):
                self._maxChildren += 1
                continue
            else:
                self._children.append(child)
