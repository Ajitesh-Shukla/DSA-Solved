from collections import Counter, defaultdict
import heapq
import numpy as np
import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    queries.sort()
    i, j=0, 0
    max_sum=0
    elem=0
    while elem<n and i<len(queries) and j<len(queries):
        cur_sum=0
        prev_i=i
        print(i, j, elem)
        while i<len(queries) and elem+1>=queries[i][0]:
            i+=1
        print(i, j)
        while j<=i and elem+1<=queries[j][1]:
            print(j)
            cur_sum+=queries[j][2]
            j+=1
        i=prev_i
        j=prev_i
        max_sum=max(max_sum, cur_sum)
        elem+=1
        print(i, j, elem, max_sum)
    return max_sum

n=4
queries=[[2, 3, 603],
[1,1,286],
[4,4,882]]
print(arrayManipulation(n, queries))
# A single node of a singly linked list
class Node:
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

# A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
  
  # insertion method for the linked list
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  
  # print method for the linked list
  def printLL(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next

