def removeelt(d, elt):
    d.remove(elt)
    return d

def ParameterizedVertexCover(V,E,k):
    if(k==0 and len(E)!=0):
        return -1
    if len(E)==0:
        return []
    for tup in E:
        for x in E:
            if tup[1] in x:
                E.remove(x)
        V2=V
        if tup[1] in V:
            V2=removeelt(V,tup[1])
        S2=ParameterizedVertexCover(V2,E,k-1)
        V1=V
        for x in E:
            if tup[0] in x:
                E.remove(x)
        if tup[0] in V:
            V1=removeelt(V,tup[0])
        S1=ParameterizedVertexCover(V1,E,k-1)
        if(S1!=-1 and (S2==-1 or len(S1) < len(S2))):
            S1.append(tup[0])
            return S1
        elif(S2!=-1 and (len(S2) <= len(S1))):
            S2.append(tup[1])
            return S2
        else:
            return -1

k=2
x=ParameterizedVertexCover(V,E,k)
print(x)
print(len(x))
