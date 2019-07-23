#!/usr/bin/python3

from trie import trie

tree = trie()
tree.insert("test")
print(tree.search("test")) # return True
print(tree.search("tes")) # return False

tree.insert("apple")
tree.insert("tes")
tree.insert("trestt")
print(tree.search("tes")) # return True

tree.delete(tree._root, "tes")
tree.delete(tree._root, "apple")
print(tree.search("apple")) # return False
print(tree.search("tes")) # return False
print(tree.search("test")) # return True
