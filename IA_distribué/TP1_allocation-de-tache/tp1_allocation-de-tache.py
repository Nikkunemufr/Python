#Calcul la somme de collectivité et la retourne
def compute_SWutilitarian(collectivity):
    utilitarian = 0
    for tache in collectivity:
        utilitarian += tache
    return utilitarian

#Calcul le minimum de la collectivité et le retourne
def compute_SWEgalitarianism(collectivity):
    return min(collectivity)

#Calcul le maximum de la collectivité et le retourne
def compute_SWElitist(collectivity):
    return max(collectivity)

#Calcul le produit de la collectivité et le retourne
def compute_SWNashProduct(collectivity):
    nashProduct = 1
    for tache in collectivity:
        nashProduct *= tache
    return nashProduct

#Donne la liste de priorité la plus haute pour chaque tache en utilisant la méthode indiqué via le SWcode
def computeCommunities(utilityMatrix, allocations, SWcode):
    communities = []
    for alloc in allocations:
        collectivity = []
        for i in range(len(utilityMatrix)):
            collectivity.append(utilityMatrix[i][alloc[i]-1])
        communities.append(SWcode(collectivity))
    return communities

#Retourne la meilleur allocation en fonction de la meilleur collectivité d'après le SW choisis
def compareCommunities(allocations, communities):
    tampon = 0
    bestAllocation = []
    for i in range(len(communities)):
        if communities[i] >= tampon:
            tampon = communities[i]
            bestAllocation = allocations[i]
    return bestAllocation

def showMatrix(matrix):
    res = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            res += str(matrix[i][j]) + " "
        res+= "\n"
    return res

                  #t1 t2 t3 t4
utilityMatrix = [[4, 2, 7, 5], #a1
                 [8, 3, 10,8], #a2
                 [12,5 ,4 ,5], #a3
                 [6 ,3 ,7 ,15]]#a4

               #a1 a2 a3 a4
allocations = [[2, 3, 1, 4], #A1
              [ 1, 2, 3, 4], #A2
              [ 3, 4, 1, 2]] #A3
print("Utility matrix : \n" + showMatrix(utilityMatrix))
print("Allocations matrix : \n" + showMatrix(allocations))

listSW = [compute_SWutilitarian, compute_SWEgalitarianism, compute_SWElitist, compute_SWNashProduct]
nameFunction = ["Utilitariste","Egalitarism","Elitist","Nash Product"]
for i in range(len(listSW)):
    communities = computeCommunities(utilityMatrix, allocations, listSW[i])
    bestAlloc = compareCommunities(allocations, communities)
    print(nameFunction[i] + " : " + str(bestAlloc))
