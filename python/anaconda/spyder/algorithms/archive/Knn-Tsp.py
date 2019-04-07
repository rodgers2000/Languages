#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 18:46:13 2018

@author: Mjr
"""

import math
import numpy as np


class Tsp():

    def __init__(self):
        self.L = 33708
        self.C = {}  # a map from vertex to (x,y)
        self.Dist = np.zeros((self.L, self.L))

    def enterData(self, node, x, y):
        self.C[node] = (x, y)  # nodes start at 0, not 1

    def getDistM(self):
        for i in range(0, self.L, 1):
            print(i / self.L * 100, '%')
            for j in range(0, self.L, 1):
                pt1 = self.C[i]
                pt2 = self.C[j]
                x_d = math.pow(pt1[0] - pt2[0], 2)
                y_d = math.pow(pt1[1] - pt2[1], 2)
                dist = math.sqrt(x_d + y_d)
                self.Dist[i, j] = dist

    def KNN(self):
        unvisited = set(self.C.keys())
        visited = set()
        crt_vtx = 0
        unvisited.remove(0)
        visited.add(crt_vtx)
        cost = 0

        while len(unvisited) != 0:
            print(len(visited) / self.L * 100, '%')
            temp_dist = self.Dist[crt_vtx][:]
            # convert numpy array to list
            temp_dist.tolist()
            temp_value = []
            # create a sequence for value and node if
            for index, value in enumerate(temp_dist):
                temp_value.append((value, index))  # value, vtx
            temp_value = sorted(temp_value, key=lambda x: x[0])
            # find smallest element
            min_dist_idx = 0
            min_dist = temp_value[min_dist_idx]
            # eliminate till we find an unvisited vertex
            while min_dist[1] in visited:
                min_dist_idx += 1
                min_dist = temp_value[min_dist_idx]
            # check for doubles
            candidates = [i for i in temp_value if i[0] == min_dist[0]]
            if len(candidates) > 1:
                candidates = sorted(candidates, key=lambda x: x[1])
            # find winner who has not been visited
            winner_idx = 0
            winner_vtx = candidates[winner_idx]
            while winner_vtx[1] in visited:
                winner_idx += 1
                winner_vtx = candidates[winner_idx]
            # update data
            print(winner_vtx[1])
            visited.add(winner_vtx[1])
            unvisited.remove(winner_vtx[1])
            cost += winner_vtx[0]
            crt_vtx = winner_vtx[1]

        # now we have finished, we travel back to 0
        cost += self.Dist[winner_vtx[1]][0]
        return cost, winner_vtx
