#!/usr/bin/python3
from node import node
from nTree import nTree

a = node("a")
b = node("b")
c = node("c")
d = node("d")
e = node("e")
f = node("f")
g = node("g")
h = node("h")

a.addChildren([b, c, d])
c.addChildren([e])
d.addChildren([f, g, h])

tree = nTree(a)
print(tree.levelOrder())
print(tree.preOrder())
