#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 12:38:57 2021

@author: max
"""

from collections import defaultdict

def load(path):
    """Read file from disk by path."""
    data = []
    with open(path, 'r') as file:
        for line in file:
            data.append(line.strip('\n'))
    return data
        

# Read data
data = load('data/day12.txt')


# Class for Cave Graph
class CaveGraph():
    
    def __init__(self, data):
        self.data = data
        self.buildGraph()
    
    def buildGraph(self):
        self.nodes = dict()
        
        # Parse file by land and add to dictionary
        for line in self.data:
            n1, n2 = line.split('-')
            
            if n1 not in self.nodes:
                self.nodes[n1] = []
            self.nodes[n1].append(n2)
            
            if n2 not in self.nodes:
                self.nodes[n2] = []
            self.nodes[n2].append(n1)

    def traverse(self, node, visited):
      # recursively find paths - and add 'em to res (resulting list)
      result = []
      new_visit = visited + [node]
      
      if node == 'end':
        return [new_visit]
    
      for n in self.nodes[node]:
        if n != 'start':
          if n not in visited or n.isupper():
            result.extend(self.traverse(n, new_visit))
      return result
                

Caves = CaveGraph(data)
res1 = Caves.traverse('start', [])

print(f'>> Day 12 / Part 1: {len(res1)}')

