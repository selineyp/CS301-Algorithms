def removeelt(d, elt):
    d.remove(elt)
    return d

import itertools,random
import statistics
from scipy import stats
import math
import numpy as np
import time, os, subprocess
def removeelt(d, elt):
    d.remove(elt)
    return d

def ParameterizedVertexCover(V,E,k):
    if(k==0 and len(E)!=0):
        return -1
    if len(E)==0:
        return []
    E1=list(E)
    for tup in E1:
        E3=list(E1)
        for x in E3:
            if x[0]==tup[1] or x[1]==tup[1]:
                E3.remove(x)
        V4=list(V)
        if tup[1] in V4:
            V4=removeelt(V4,tup[1])
        S2=ParameterizedVertexCover(V4,E3,k-1)
        E2=list(E)
        for x in E2:
            if x[0]==tup[0] or x[1]==tup[0]:
                E2.remove(x)
        V1=list(V)
        if tup[0] in V1:
            V1=removeelt(V1,tup[0])
        S1=ParameterizedVertexCover(V1,E2,k-1)
        if(S1!=-1 and (len(S1) < len(S2))):
            S1.append(tup[0])
            return S1
        elif(S2!=-1 and (len(S2) <= len(S1))):
            S2.append(tup[1])
            return S2
        else:
            return -1
