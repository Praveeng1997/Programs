import math
import pdb
import random

class Bplus:
    def __init__(self):
        self.Nodes = None
        self.layer = [[]]
        
tree = Bplus()


def split(node,n):
    n1 = node[:(n/2)]
    n2 = node[(n/2):]
    return [n1,n2]

def insert(ele,tree,n,l,size):
    global L
    size = n**(l-1)
    index = 0
    status = 0
    for k in range(len(tree.layer[l-1])-1):
                if (ele < tree.layer[l-1][k+1][0]):
                    tree.layer[l-1][k].append(ele)
                    tree.layer[l-1][k].sort()
                    index = k
                    status = 1
                    break
    if (status !=1):
        tree.layer[l-1][-1].append(ele)
        tree.layer[l-1][-1].sort()
        index = -1
    #pdb.set_trace()
    if len(tree.layer[l-1][index]) > n-1:
        nodes = split(tree.layer[l-1][index],n)
        del tree.layer[l-1][index]
        tree.layer[l-1].append(nodes[0])
        tree.layer[l-1].append([nodes[1][1]])
        tree.layer[l-1].sort()
        p_s = size
        if len(tree.layer[l-1]) > size:
            if l==1:
                tree.layer.insert(0,[[nodes[1][0]]])
                l+=1
                L+=1
                size*=n
            else :
                #pdb.set_trace()
                insert(nodes[1][0],tree,n,l-1,p_s)
                l+=1
                
        else :
            insert(nodes[1][0],tree,n,l-1,p_s)
    return l,size
            

def bplus(n,data):
    l = 0
    size = 1
    node = []
    global L
    L = 0
    for i in range(len(data)):
        #pdb.set_trace()
        if l==0:
        
           node.append(data[i])
           node.sort()
           if len(tree.layer[l]) <= (n-1):
               tree.layer[l] = node
           else :
               l+=1
               L = l
               #pdb.set_trace()
               nodes = split(node,n)
               tree.layer.append(nodes)
               tree.layer[l-1] = [[nodes[1][0]]]
               node = tree.layer[l]

        else :
            
            index = 0
            #pdb.set_trace()
            status = 0
            L = l
            for k in range(len(node)-1):
                if (data[i] < node[k+1][0]):
                    node[k].append(data[i])
                    node[k].sort()
                    index = k
                    status = 1
                    break
            if (status !=1):
                node[-1].append(data[i])
                node[-1].sort()
                index = -1
            if data[i] == 4:
                pdb.set_trace()
            if len(node[index]) <= n-1 :
                tree.layer[l] = node
            else :
                #pdb.set_trace()
                nodes = split(node[index],n)
                del node[index]
                node.append(nodes[0])
                node.append(nodes[1])
                node.sort()
                #pdb.set_trace()
                
                l,size = insert(nodes[1][0],tree,n,l,size)
                if L!= l:
                    l = L
                    
            
                        
                              
    return tree

data = [0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0]
tree = bplus(3,data)
pdb.set_trace()

            
