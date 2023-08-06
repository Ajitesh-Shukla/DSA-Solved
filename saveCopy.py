from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
'''Neetcode'solution is cleaner code'''
class Solution:
    def cloneGraph(self, node):
        if not node:
            return Node()
        new_graph=Node(node.val)
        # Pointers for new graph
        p2=new_graph
        hash={node.val: new_graph}

        def dfs(parent, pointer_new):
            for children in parent.neighbors:
                if children.val in hash:
                    pointer_new.neighbors.append(hash[children.val])
                else:
                    new_node=Node(children.val)
                    pointer_new.neighbors.append(new_node)
                    hash[children.val]=new_node
                    dfs(children, pointer_new.neighbors[-1])

        dfs(node, p2)

        return new_graph



            

            