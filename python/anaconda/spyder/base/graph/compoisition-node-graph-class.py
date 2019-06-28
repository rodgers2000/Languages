#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 14:53:56 2018

@author: Mjr
"""

# =============================================================================
# This is a graph formed by two objects.
# =============================================================================

import numpy as np


class Node():

    def __init__(self, idd):
        self.idd = idd
        self.edges = list()
        self.visited = False

    def addEdge(self, nodeid):
        self.edges.append(nodeid)

    def removeEdge(self, nodeid):
        self.edges.remove(nodeid)


class Graph():

    def __init__(self):
        self.Nodes = []

    def addNode(self, node):
        self.Nodes.append(node)

    def removeNode(self, node):
        self.Nodes.remove(node)

    def printGraph(self):
        for i in self.Nodes:
            print(i.idd, end=' ')
            print(i.edges)


# create nodes
nodes = []
for i in range(0, 10):
    size = np.random.randint(1, 5, 1)
    this_node = Node(i)
    for j in np.random.randint(0, 9, size):
        if j == i:
            continue
        this_node.addEdge(j)
    nodes.append(this_node)

# create graph
graph = Graph()
for node in nodes:
    graph.addNode(node)

# print graph
graph.printGraph()
