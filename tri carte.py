'''Spécification Le tri par insertion Le tri par sélection Le tri à bulle
Fonction tri_insertion(liste L) :
 début
 n ← taille de L
 pour i variant de 1 à n −1 (inclus) faire
 temp ←L[i ]
 j ←i
 tant que j >0 et temp <L[j −1] faire
 L[j ] ←L[j −1]
 j ←j −1
L[j ] ←temp;
 Résultats : L est triée
 (Correction de l’algorithme)'''
    
def tri_insertion(L):
    n=len(L)
    for i in range(1,n):
        temp=L[i]
        j=i
        while j > 0 and temp < L[j-1]:
            L[j],L[j-1] = L[j-1], L[j]
            j = j-1
    return L

'''
Spécification Le tri par insertion Le tri par sélection Le tri à bulle
Pseudo-code
Fonction tri_bulles(liste L) :
 début
 N ← taille de L
 pour i variant de n −1 à 1 faire
 pour j variant de 0 à i −1 faire
 si L[j ] >L[j + 1] alors
 Echanger L[j ] et L[j + 1]'''


def tri_bulles(L):
    n=len(L)
    for i in range(n-1,1):
        for i in range(0,i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    return L