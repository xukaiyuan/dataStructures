#!/usr/bin/python3

class trieNode:

    def __init__(self):
        self._children = [None] * 26
        self._isEnd = False

class trie:

    def __init__(self):
        self._root = self.getNode()

    def getNode(self):
        return trieNode()

    def charToIndex(self, char):
        # lowercase only
        return ord(char) - ord("a")

    def insert(self, word):
        if(len(word) == 0):
            return
        cur = self._root

        for char in word:
            index = self.charToIndex(char)
            if(not cur._children[index]):
                cur._children[index] = self.getNode()
            cur = cur._children[index]

        cur._isEnd = True

    def search(self, word):
        if(len(word) == 0):
            return True
        cur = self._root

        for char in word:
            index = self.charToIndex(char)
            if(not cur._children[index]):
                return False
            cur = cur._children[index]

        return cur != None and cur._isEnd

    def isEmpty(self, node):
        # judge if the node has no children
        for i in range(26):
            if(node._children[i]):
                return False
        return True

    def delete(self, cur, word, depth = 0):
        if(not self._root or len(word) == 0 or not self.search(word)):
            return

        if(depth == len(word)):
            if(cur._isEnd):
                cur._isEnd = False

            if(self.isEmpty(cur)):
                del cur
                cur = None

            return cur

        index = ord(word[depth]) - ord("a")
        cur._children[index] = self.delete(cur._children[index], word, depth + 1)

        if(self.isEmpty(cur) and cur._isEnd == False):
            del cur
            cur = None
        return cur

    # TO DO: frequency count
