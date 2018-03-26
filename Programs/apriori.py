from __future__ import division
import numpy as np
import csv
import copy



class items:
    def __init__(self):
        self.data = []
        self.l = []
        self.count = []
        self.c = {}


    def _1_itemset(self,data):
        _1_set = sorted(set().union(*data))
        self.data = [[k] for k in _1_set]
        self.count = [0 for i in range(len(self.data))]
        for item in range(len(self.data)):
            for i in range(len(data)):
                if self.data[item] in data[i]:
                    self.count[item]+=1
                    
                    
    def generate(self,data,size):
        for i in range(len(data)):
            temp = []
            first = data[i][:size]
            start = copy.copy(first)
            temp.append(first)
            temp[0].append(data[i][-1])
            j = i+1
            while(j <len(data) and data[j][:size]==start):
                temp[0].append(data[j][-1])
                self.data.extend(copy.deepcopy(temp))
                del temp[0][-1]
                j+=1

    def dict_count(self,data,support):
        self.count = [0 for i in range(len(self.data))]
        for i in range(len(self.data)):
            for j in range(len(data)):
                cn = 0
                for s in self.data[i] :
                    if(s in data[j]):
                        cn+=1
                if(cn == len(self.data[i])):
                        self.count[i]+=1
                        index = ''.join(self.data[i])
                        self.c[index] = self.count[i]
            if(self.count[i]>=support):
                self.l.append(self.data[i])
        #print ""
        #print self.c
        print ""
        print self.l

       


def apriori(item,data,support):    
    item._1_itemset(data)
    item.dict_count(data,support)
    stop = False
    item_obj = [item]
    count = 0
    while(stop!=True):
        prev = item_obj[count]
        i = items()
        i.generate(prev.l,count)
        i.dict_count(data,support)
        item_obj.append(i)
        count+=1
        if(i.l == []):
            stop = True
    return item_obj

def combinations(target,data,s):
     for i in range(len(data)):
         new_target = copy.copy(target)
         new_data = copy.copy(data)
         new_target.append(data[i])
         new_data = data[i+1:]
         s.append(new_target)
         combinations(new_target,
                      new_data,s)




''' Read Input '''


#a = [('1','2','5'),('2','4'),('2','3'),('1','2','4'),('1','3'),('2','3'),('1','3'),('1','2','3','5'),('1','2','3')]


fileName = ('/home/praveen/Programs/Bakery-Apriori/1000/1000-out1.csv')

a = []
with open(fileName) as f:
    reader = csv.reader(f)
    for row in reader:
        a.append(row[1:]) 

#print len(a)


a = [tuple(sorted(s)) for s in a]


min_support  = 30
min_confidence = .7


I = apriori(items(),a,min_support)


itemsets  = I[-2].l
rule_set = {}
final_rules = {}



for itemset in itemsets:
    print ""
    t = []
    s = []
    combinations(t,itemset,s)
    s = sorted(s,key=len)
    for k in s:
        if(k==itemset):
            continue
        new = [e for e in itemset if e not in k]
        s1 = ''.join(sorted(k))
        s2 = ''.join(sorted(new))
        # Compute Confidence
        freq = I[-2].c[''.join(sorted(itemset))]
        con = freq/I[len(k)-1].c[s1]
        string = s1+"-->"+s2
        rule_set[string] = con

        
for rule in rule_set:
    if(rule_set[rule] >= min_confidence):
        final_rules[rule] = rule_set[rule]

#print rule_set
print final_rules

