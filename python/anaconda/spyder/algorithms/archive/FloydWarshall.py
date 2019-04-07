#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 12:10:08 2018

@author: Mjr
"""

import numpy as np
import math


class FloydWarshall():

    def __init__(self, graph):
        self.Graph = graph
        self.Dist = 0
        self.V = len(graph.Nodes)  # len of nodes
        self.Dist = np.zeros((self.V, self.V))
        self.Dist[self.Dist == 0] = math.inf

    def setupDist(self):
        for vertex in range(0, self.V, 1):
            self.Dist[vertex][vertex] = 0

        for node in self.Graph.Nodes:
            row_idx = node.node - 1
            # you subtract one since matrix starts at 0
            for att_idx in range(0, len(node.edges), 1):
                col_idx = node.edges[att_idx] - 1
                wght = node.weights[att_idx]
                self.Dist[row_idx][col_idx] = wght

    def runAlgo(self):
        for k in range(0, self.V, 1):
            print((k + 1) / self.V * 100, '%')
            for i in range(0, self.V, 1):
                for j in range(0, self.V, 1):
                    if self.Dist[i][j] > self.Dist[i][k] + self.Dist[k][j]:
                        self.Dist[i][j] = self.Dist[i][k] + self.Dist[k][j]

    def checkNegCycles(self):
        for i in range(0, self.V, 1):
            if self.Dist[i][i] < 0:
                return True
        return False
