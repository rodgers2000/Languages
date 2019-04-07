#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 22:01:05 2018

@author: Mjr
"""


class Prim():

    def __init__(self, graph, start):
        self.Q = set(graph.nodes.keys())
        self.V = set()
        self.V.add(start)
        self.mst_cost = 0
        self.graph = graph

    def findMin(self, mapping):
        flag = 1
        for k, v in mapping.items():
            if flag == 1:
                min_k = k
                min_v = v
                flag = 0
            else:
                if v < min_v:
                    min_k = k
                    min_v = v
        return min_k, min_v

    def runPrim(self):
        T = self.Q.difference(self.V)
        while len(T) != 0:
            print(len(T))
            p_edges = {}  # node, cost
            for node in self.V:
                for nbr, cost in self.graph.nodes[node].items():
                    if nbr in T:
                        if nbr not in p_edges:
                            p_edges[nbr] = cost
                        else:
                            if p_edges[nbr] > cost:
                                p_edges[nbr] = cost
            star_n, star_c = self.findMin(p_edges)
            self.V.add(star_n)
            self.mst_cost += star_c
            T = self.Q.difference(self.V)
