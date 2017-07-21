from __future__ import division
import math
import pdb
import pydot
graph = pydot.Dot(graph_type='graph')

class Bplus:
    def __init__(self):
        self.root = None
        
tree = Bplus()


class Node:
    def __init__(self):
        self.ele  =  []
        self.links = None
        self.right = None
        

def bplus(n,data):
    depth = 0
    node = Node()
    for i in range(len(data)):
        if depth ==0 :                               # Used to insert elements till first split
            if len(node.ele) ==0:
                node.ele.append(data[i])
                tree.root = node
            else:
                node.ele.append(data[i])
                node.ele.sort()
                if len(node.ele) > n-1 :
                    n1 = Node()
                    n2 = Node()
                    n2.ele = [node.ele.pop(n//2) for k in range(int(math.ceil(n/2)))]
                    n2.ele.sort()
                    n1.ele = [n2.ele[0]]
                    node.right = n2
                    n1.links =[node,n2]
                    tree.root = n1
                    depth +=1
        else:
            stack = []                             # A list used to keep track of nodes while traversing to leaf
            index = []                             #  # A list used to keep track of node indices while traversing to leaf
            node = tree.root
            while node.links != None:
                stack.append(node)
                if data[i] < node.ele[0]:
                    node = node.links[0]
                    index.append(0)
                elif data[i] >= node.ele[-1] :
                    node = node.links[-1]
                    index.append(-1)
                else :
                    for j in range(len(node.ele)-1):
                        if data[i] > node.ele[j] and data[i] < node.ele[j+1]:
                            node = node.links[j+1]
                            index.append(j+1)
                            break
            node.ele.append(data[i])
            node.ele.sort()
            while len(stack) !=0:
                if len(node.ele) > n-1:
                    n2 = Node()
                    n2.ele = [node.ele.pop(n//2) for k in range(int(math.ceil(n/2)))]
                    parent = stack.pop()
                    pos = index.pop()
                    if pos==-1:
                        parent.links.append(n2)
                    else :
                        parent.links.insert(pos+1,n2)
                    if node.links ==None:
                        k = node.right
                        node.right = n2
                        n2.right = k
                        parent.ele.append(n2.ele[0])
                        parent.ele.sort()
                    else:
                         n2.links = []
                         for i in range(n//2):
                             n2.links.insert(0,node.links.pop(-1))
                         parent.ele.append(n2.ele.pop(0))
                         parent.ele.sort()
                    node = parent
                    
                else :
                    parent = stack.pop()
                    parent.links[index.pop()] = node
                    node = parent
            tree.root = node
            if len(tree.root.ele) > n-1:
                node = Node()
                n2   = Node()
                n2.ele = [tree.root.ele.pop(n//2) for i in range(int(math.ceil(n/2)))]
                n2.ele.sort()
                node.ele.append(n2.ele.pop(0))
                node.ele.sort()
                n2.links = []
                for i in range(n//2):
                    n2.links.insert(0,tree.root.links.pop(-1) )
                node.links = [tree.root,n2]
                tree.root = node
    return tree

data = [i+1 for i in range(60)]    # The Input elements

tree = bplus(4,data)               # Here ,4 is the order


# A utility function to print the leaf nodes
def print_leaf(tree):
    node = tree.root
    while node.links != None:
        node = node.links[0]
        print node.ele
    while node.right !=None:
        print node.right.ele
        node = node.right

print_leaf(tree)


k = tree.root
s = ' '.join(str(e) for e in k.ele)

# A function to display the tree and store it in the required file

def func(k,s):
    for i in range(len(k.links)):
        l = k.links[i].ele
        s1 = ' '.join(str(e) for e in l)
        edge = pydot.Edge(s,s1)
        graph.add_edge(edge)
        if k.links[i].links ==None:
            continue
        else:
            func(k.links[i],s1)
func(k,s)
graph.write_png('Tree.png')

    



            
