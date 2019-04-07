#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 22:50:34 2018

@author: Mjr
"""

exec(open("import-data.py").read())


class Dijkstra():

    def __init__(self, graph):
        # this graph has nodes, edges, and distances
        self.graph = graph
        self.Que = []
        self.Dist = {}

    def get_distances(self):
        return self.Dist

    def setup_data(self):
        for node in self.graph.getNodes():
            idd = node.getID()
            self.Dist[idd] = 1000000
            self.Que.append(idd)

    def traverse_graph(self, source):
        self.Dist[source] = 0

        while len(self.Que) != 0:
            this_min = 1000000
            u = 0
            for node in self.Que:
                if self.Dist[node] < this_min:
                    this_min = self.Dist[node]
                    u = node

            self.Que.remove(u)

            nodes = self.graph.getNodes()
            for node in nodes:
                if u == node.getID():
                    node_u = node.getAttrs()

            for nbr, dst in node_u.items():
                alt = self.Dist[u] + dst
                if alt < self.Dist[nbr]:
                    self.Dist[nbr] = alt


mike = Dijkstra(graph)
mike.setup_data()
mike.traverse_graph(1)
yesss = mike.get_distances()

for node in [7,37,59,82,99,115,133,165,188,197]:
    print(node, ':', yesss[node])
