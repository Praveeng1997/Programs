from sklearn import datasets
import numpy as np
import random
import matplotlib.pyplot as plt
import pdb


a = datasets.load_iris()
np.random.seed(0)  
class cluster:
        def __init__(self,a):
                self.centroid =a.data[np.random.randint(0,len(a.target))]
                self.elements = []
                
        def new_centroid(self):
                self.centroid =  np.round(np.mean(np.array(self.elements),axis = 0),decimals = 2)
                return self.centroid

        def distance(self,data):
                return np.sqrt(np.sum((data-self.centroid)**2,axis = 1))

        def add(self,ele):
                self.elements.append(ele)
                
print np.bincount(a.target)
             
k = 3
data = a.data
clusters = [cluster(a) for i in range(k)]



def kmeans(data,clusters,k):
        dist = []
        old = []
        new = []
        for i in range(k):
                dist.append(clusters[i].distance(data))
                old.append(clusters[i].centroid)
                clusters[i].elements[:] = []
        dist_min = np.min(dist,axis = 0)
        for i in range(len(dist[0])):
                for j in range(k):
                        if(dist_min[i] ==dist[j][i]):
                                clusters[j].add(data[i])
                                break
        for i in range(k):
                new.append(clusters[i].new_centroid())
        
        if(np.array_equal(old,new)):
                print("OLD",old)
                print("NEW",new)
                return
        else:
                kmeans(data,clusters,k)
                
kmeans(data,clusters,k)

print len(clusters[0].elements)
print len(clusters[1].elements)
print len(clusters[2].elements)




