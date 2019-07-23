#!/usr/bin/python3
from node import node

class nTree:

    def __init__(self, head):
        # head should be in type of node
        self._root = node("head")
        self._root.addChildren([head])

    def insert(self, path, value):
        # insert a node with value as the path
        # it the path doesn't exist, return False
        cur = self._root

        for step in path:
            if(cur.searchDown(step) == None):
                return False
            else:
                cur = cur.searchDown(step)

        cur.addChildren([node(value)])
        return True

    def delete(self, path, value):
        # delete a node with value as the path
        # it the path doesn't exist, return False
        cur = self._root

        for step in path:
            if(cur.searchDown(step) == None):
                return False
            else:
                cur = cur.searchDown(step)

        cur.deleteChildren([node(value)])
        return True

    def preOrder(self):
        # preorder traversal
        if(len(self._root.getChildren()) == 0):
            return []

        res = []

        def preOrder_helper(res, cur):
            if(cur != None):
                res.append(cur.getValue())
            else:
                return

            for child in cur.getChildren():
                if(child != None):
                    preOrder_helper(res, child)

        preOrder_helper(res, self._root.getChildren()[0])
        return res

    def levelOrder(self):
        # level order traversal
        if(len(self._root.getChildren()) == 0):
            return []

        res = []

        queue = [self._root.getChildren()[0]]

        while(len(queue) != 0):
            cur = queue.pop(0)
            res.append(cur.getValue())
            curChildren = cur.getChildren()

            for child in curChildren:
                queue.append(child)

        return res
