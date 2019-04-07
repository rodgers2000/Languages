#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 16:08:35 2019

@author: mrodgers
"""

import os

os.chdir("/Users/mrodgers/Documents/other/languages/python/anaconda/spyder/algorithms/graph")

import GraphNode as path2


class ImportGraph:
    def __init__(self, file):
        self.file = file
        self.graph = path2.Graph()
    def run(self):
        # grab the lines
        txt = open(self.file, 'r').readlines()
        # for each line in txt
        for line in txt:
            # split the line, if i is a digit, make it an int 
            a = []
            for i in line.split():
                if i.isdigit():
                    a.append(int(i))
            # the first one is the node
            node = a[0]
            temp_node = path2.Node(node)
            # the rest are the edges
            for i in a[1:]:
                temp_node.addEdge(i)
            self.graph.addNode(temp_node)
        
#mjr = ImportGraph("data/graph1.txt")
#mjr.run()
#mjr.graph.nodes