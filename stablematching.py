def stableMatching(n,menPreferences,womenPreferences):
    unmarriedMen = list(range(n))
    manSpouse = [None] * n                      
    womanSpouse = [None] * n                      
    nextManChoice = [0] * n
    pos=-1
    husbandpos=-1
    hepos=-1
    while(unmarriedMen):
        he = unmarriedMen[0]                    
        hisPreferences = menPreferences[he]       
        she = hisPreferences[nextManChoice[he]] 
        herPreferences = womenPreferences[she]
        currentHusband = womanSpouse[she]
        if(currentHusband==None):
            manSpouse[he]=she
            womanSpouse[she]=he
            del unmarriedMen[0];
            nextManChoice[he]+=1;
        else:
            for i in range(0,n):
                if(herPreferences[i]==he):
                    pos=i
                if(herPreferences[i]==currentHusband):
                    husbandpos=i
            if(pos<husbandpos):
                for i in range(0,n):
                    if(manSpouse[i]==she):
                        hepos=i
                manSpouse[hepos]=None
                del unmarriedMen[0];
                womanSpouse[she]=he
                manSpouse[he]=she
                unmarriedMen.append(currentHusband)
                nextManChoice[he]+=1
            else:
                nextManChoice[he]+=1
    return manSpouse
assert(stableMatching(1, [ [0] ], [ [0] ]) == [0])
assert(stableMatching(2, [ [0,1], [1,0] ], [ [0,1], [1,0] ]) == [0, 1])
