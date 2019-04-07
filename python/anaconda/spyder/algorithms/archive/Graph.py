#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 11:34:34 2018

@author: Mjr
"""


# =============================================================================
# OBJECTS
# =============================================================================

class Node():

    def __init__(self):
        self.edges = []
        self.weights = []
        self.node = 0

    def addEdge(self, edge, weight):
        self.edges.append(edge)
        self.weights.append(weight)

    def getWeight(self, edge):
        idx = self.edges.index(edge)
        wgt = self.weights[idx]
        return wgt

    def getEdges(self):
        return self.edges


class Graph():

    def __init__(self):
        self.Nodes = []

    def addNode(self, node):
        self.Nodes.append(node)


# =============================================================================
# FUNCTIONS
# =============================================================================


def importGraph(file):

    # =============================================================================
    #     This function returns a graph object of graph class. It contains a
    #     list of nodes, which map to edges and weights.
    # =============================================================================

    mike = Graph()

    datfile = open(file, 'r')

    lines = datfile.readlines()
    info = lines[0].split(' ')
    len_n = int(info[0])
    len_e = int(info[1])

    pst_nd = 1
    this_node = Node()
    this_node.node = 1

    idx = 1

    for line in lines[1:]:
        info = line.split(sep=' ')
        crt_nd = int(info[0])
        if crt_nd == pst_nd:
            this_node.addEdge(int(info[1]), int(info[2]))
            pst_nd = crt_nd
        else:
            mike.addNode(this_node)
            this_node = Node()
            this_node.node = crt_nd
            this_node.addEdge(int(info[1]), int(info[2]))
            pst_nd = crt_nd
        idx += 1
        if crt_nd == len_n and idx == len_e:
            mike.addNode(this_node)

    return mike
