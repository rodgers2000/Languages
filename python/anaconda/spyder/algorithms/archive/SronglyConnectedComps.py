#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 19:44:31 2018

@author: Mjr
"""

from collections import defaultdict

import itertools

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.count = 1

    def count_nodes(self):
        return len(self.graph.keys())

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] is False:
                self.count = self.count + 1
                self.DFSUtil(i, visited)

    def fillOrder(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] is False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)

    def getTranspose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

    def makeVisited(self):
        visited = {}
        n = self.graph.keys()
        v = self.graph.values()

        merged = list(itertools.chain.from_iterable(v))
        unique_nodes1 = set(merged)
        unique_nodes2 = set(n)
        nodes_to_add = unique_nodes1.difference(unique_nodes2)
#        for i in unique_nodes1:
#            if i not in nodes:
#                nodes.append(i)
#                print 'unique nodes of %d' % len(nodes)

        nodes = list(unique_nodes2) + list(nodes_to_add)

        for i in nodes:
            visited[i] = False
        return visited

    def resetVisited(self, visited):
        for i in visited.keys():
            visited[i] = False
        return visited

    def countSCC(self):
        print ('just entered count SCC')
        stack = []
        visited = self.makeVisited()
        print ('just reset visited')
        for i in self.graph.keys():
            #print 'current node is %d in 1 run' % index
            if visited[i] is False:
                self.fillOrder(i, visited, stack)
                print ('just filled an order')
        gr = self.getTranspose()
        print ('just transposed the graph')
        visited = self.resetVisited(visited)
        chart = []
        index = 1
        while stack:
            i = stack.pop()
            #print 'current node is %d in 2 run' % index
            index += 1
            if visited[i] is False:
                gr.count = 1
                gr.DFSUtil(i, visited)
                #print 'current count is ', gr.count
                chart.append(gr.count)
        chart.sort(reverse=True)
        return chart


#g = Graph(9)
#g.addEdge(1, 4)
#g.addEdge(2, 8)
#g.addEdge(3, 6)
#g.addEdge(4, 7)
#g.addEdge(5, 2)
#g.addEdge(6, 9)
#g.addEdge(7, 1)
#g.addEdge(8, 5)
#g.addEdge(8, 6)
#g.addEdge(9, 7)
#g.addEdge(9, 3)

#g = Graph([8])
#g.addEdge(1, 2)
#g.addEdge(2, 3)
#g.addEdge(3, 1)
#g.addEdge(3, 4)
#g.addEdge(5, 4)
#g.addEdge(6, 4)
#g.addEdge(8, 6)
#g.addEdge(6, 7)
#g.addEdge(7, 8)

#g = Graph([1])
#g.addEdge(1, 2)
#g.addEdge(2, 6)
#g.addEdge(2, 3)
#g.addEdge(2, 4)
#g.addEdge(3, 1)
#g.addEdge(3, 4)
#g.addEdge(4, 5)
#g.addEdge(5, 4)
#g.addEdge(6, 5)
#g.addEdge(6, 7)
#g.addEdge(7, 6)
#g.addEdge(7, 8)
#g.addEdge(8, 5)
#g.addEdge(8, 7)

#g = Graph([1])
#g.addEdge(1, 2)
#g.addEdge(2, 3)
#g.addEdge(3, 1)
#g.addEdge(3, 4)
#g.addEdge(5, 4)
#g.addEdge(6, 4)
#g.addEdge(8, 6)
#g.addEdge(6, 7)
#g.addEdge(7, 8)
#g.addEdge(4, 3)
#g.addEdge(4, 6)

g = Graph([1])
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(2, 5)
g.addEdge(3, 6)
g.addEdge(4, 5)
g.addEdge(4, 7)
g.addEdge(5, 2)
g.addEdge(5, 6)
g.addEdge(5, 7)
g.addEdge(6, 3)
g.addEdge(6, 8)
g.addEdge(7, 8)
g.addEdge(7, 10)
g.addEdge(8, 7)
g.addEdge(9, 7)
g.addEdge(10, 9)
g.addEdge(10, 11)
g.addEdge(11, 12)
g.addEdge(12, 10)

print(g.countSCC())