def estPremier(n):
    for i in range(2,n):
        if n%i==0:
            return False
        return True
def estPremier_am(n):
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            return False
    return True

def liste_premiers(n):
    L=[]
    for k in range(2,n+1):
        if estPremier_am(k):
            L=L+[k]
    return L

def valuation_p_adique_it(n, p):
    if n%p!=0:
        return 0
    else:
        k=1
        while n%(p**k)==0:
            k=k+1
        return k-1

def val_p_adique_re(n,p):
    if n%p!=0:
        return 0
    return 1+val_p_adique_re(n/p,p)

def decomposition_facteurs_premiers(n):
    L=liste_premiers(n)
    DFP=[]
    for e in L:
        if n%e==0:
            DFP=DFP+[[e,valuation_p_adique_it(n,e)]]
    return DFP

def prefixe (M,S):
    for i in range(1,len(S)):
        if M==S[:i]:
            return True
    return False
def liste_suffixes (S):
    LS=[]
    for i in range(0,len(S)):
        LS=LS+[[S[i:],i]]
    return LS
def tri(L):
    n=len(L)
    for i in range(n):
        for j in range(n-1):
            if L[j]>L[j+1]:
                L[j],L[j+1]=L[j+1],L[j]
        print(L)

def tri_liste(L):
    n=len(L)
    for i in range(n):
        for j in range(n-1):
            if L[j][0]>L[j+1][0]:
                L[j],L[j+1]=L[j+1],L[j]
def recherche(M,L):
    if L==[]:
        return None
    if prefixe (M,L[0][0]):
        return L[0][1]
    else:
        return recherche(M,L[1:])

def matrice(P,Q):
    M=len(P)*[len(Q)*[0]]
    for j in range(0,len(Q)):
        if P[0]==Q[j]:
            M[0][j]=1
    for i in range(1,len(P)):
        if P[i]==Q[0]:
            M[0][j]=1
    for i in range(1,len(P)):
        for j in range(1,len(Q)):
            if P[i]==Q[j]:
                M[i][j]=M[i-1][j-1]+1
    return M

def plus_long_mc (P, M):
    (i,j)=max(M)
    L=[(i,j)]
    while i>0 and j>0 and M[i][j]!=0:
        L=L+[(i-1,j-1)]
        i=i-1
        j=j-1
    return [P[L[k][0]] for k in range(len(L)-1,-1,-1)]






