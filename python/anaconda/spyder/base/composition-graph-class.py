#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 15:11:48 2018

@author: Mjr
"""

# =============================================================================
# This is a graph formed by one object.
# =============================================================================

import numpy as np


class Graph():

    def __init__(self):
        self.Nodes = dict()

    def addPoint(self, node, edge):
        if node not in self.Nodes:
            self.Nodes[node] = [edge]
        else:
            self.Nodes[node].append(edge)

    def printGraph(self):
        for node, edge in self.Nodes.items():
            print(node, edge, sep=':')


mike = Graph()

# make graph

nodes = range(0, 10)

for node in nodes:
    size = np.random.randint(1, 5, 1)
    edges = np.random.choice(nodes, size, False)
    for edge in edges:
        if edge == node:
            continue
        mike.addPoint(node, edge)

mike.printGraph()
