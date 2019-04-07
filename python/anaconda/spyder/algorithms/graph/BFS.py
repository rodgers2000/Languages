#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:31:17 2019

@author: mrodgers
"""

import algorithms.graph as path1
import algorithms.graph.Queue as path2

class BreathFirstSearch:
    
    # this BFS will return a path from start to end node
    
    def __init__(self, graph, start, end):
        self.graph = graph
        self.start = start
        self.end = end
        
    def run(self):
        # use a Queue (FIFO)
        open_set = path2.Queue()
        # mark visitied; this is useful in the algorithm
        visited = set()
        # this is for book keeping
        child2par = dict()
        # get start node
        root = self.start
        child2par[root] = None
        open_set.enqueue(root)
        
        while not open_set.isempty():
            temp_root = open_set.dequeue()
            # if we are finished, find the path
            if temp_root == self.end:
                mjr = [temp_root]
                while child2par[temp_root] != None:
                    temp_root = child2par[temp_root]
                    mjr.append(temp_root)
                return mjr
            # else, do BFS
            for edge in self.graph.nodes[temp_root].edges:
                if edge not in visited:
                    visited.add(edge)
                    open_set.enqueue(edge)
                    child2par[edge] = temp_root
    
            visited.add(temp_root)
        
"""
run search 
"""

mjr = path1.ImportGraph.ImportGraph("/Users/mrodgers/Documents/other/languages/python/anaconda/spyder/algorithms/graph/data/graph1.txt")
mjr.run()
bfs = BreathFirstSearch(mjr.graph, 1, 13)
bfs.run()