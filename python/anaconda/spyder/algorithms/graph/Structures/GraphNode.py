#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:24:25 2019

@author: mrodgers
"""

class Node:
    
    def __init__(self, name):
        self.name = name
        self.edges = []
        self.weights = []
        
    def addEdge(self, edge):
        self.edges.append(edge)
    
    def addWeight(self, weight):
        self.weights.append(weight)


class Graph:
    
    def __init__(self):
        self.nodes = dict() # takes a Node object
    
    def addNode(self, node):
        self.nodes[node.name] = node
