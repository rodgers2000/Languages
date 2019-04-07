#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 22:08:43 2018

@author: Mjr
"""


class Node():

    def __init__(self, idd):
        self.attrs = {}
        self.idd = idd

    def addAttrs(self, edge, dist):
        if edge not in self.attrs:
            self.attrs[edge] = dist

    def getDist(self, edge):
        return self.attrs[edge]

    def getAttrs(self):
        return self.attrs

    def getID(self):
        return self.idd


class Graph():

    def __init__(self):
        # edges are contained in the nodes
        self.nodes = []

    def addNode(self, node):
        if node not in self.nodes:
            self.nodes.append(node)

    def getNodes(self):
        return self.nodes

    def printGraph(self):
        for node in self.nodes:
            print(node.getID(), ': ', node.getAttrs())
