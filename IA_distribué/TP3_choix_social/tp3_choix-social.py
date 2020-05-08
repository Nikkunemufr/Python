def showMatrix(matrix, c1, c2):
    res = "   | "
    for i in range(len(matrix)):
        res+= c1+str(i+1)+" "
    res+="\n--------------\n"
    for i in range(len(matrix)):
        res+= c2+str(i+1)+" | "
        for j in range(len(matrix[i])):
            res += str(matrix[i][j]) + "  "
        res+= "\n"
    return res

def initMatrix(matrix):
    initMatrix = []
    for i in range(len(matrix)):
        initMatrix.append([])
        for j in range(len(matrix[i])):
            initMatrix[i].append(0)
    return initMatrix

def condorcet(matVote, agent1, agent2):
    cpt=0
    for i in range(len(matVote)):
        if matVote[agent1][i] < matVote[agent2][i]:
            cpt+=1
    return cpt
            
def condorcetMatrix(matVote):
    condorcetMat = initMatrix(matVote)
    for idVotant in range(len(matVote)):
        for idVote in range(len(matVote[idVotant])):
            condorcetMat[idVotant][idVote] += condorcet(matVote, idVotant, idVote)

    return condorcetMat

def winnerCondorcetMatrix(matCondorcet):
    winnerMat = initMatrix(matCondorcet)
    for i in range(len(winnerMat)):
        for j in range(len(winnerMat)):                
            if i==j or matCondorcet[i][j] > matCondorcet[j][i] :
                winnerMat[i][j] += 1

    return winnerMat

def winnerCondorcert(winnerMat):
    winner = "pas de gagnant"
    for i in range(len(winnerMat)):
        if sum(winnerMat[i]) == len(winnerMat):
            winner = "c"+str(i+1)
    return winner
            

def bordaVector(matVote, nbVotant):
    dic = [0]*nbVotant
    for idVotant in range(len(matVote)):
        cpt = len(matVote)
        for idVote in range(len(matVote[idVotant])):
            i=int(matVote[idVotant][idVote])-1
            dic[i] += cpt
            cpt -= 1
    return dic

def eliminationSuccessive(matVote):
    return 
            

            #c1 c2 c3
matVote = [[1,2,3],# v1
           [3,1,2],# v2
           [2,3,1]]# v3

matVote2 = [[2,1,3,4],
            [2,1,3,4],
            [2,1,3,4],
            [2,1,3,4],
            [2,1,3,4],
            [2,1,3,4],
            [2,1,3,4],
            [2,1,3,4],
            [2,1,3,4],
            [2,1,3,4],
            [3,1,4,2],
            [3,1,4,2],
            [3,1,4,2],
            [3,1,4,2],
            [3,1,4,2],
            [3,1,4,2],
            [1,4,2,3],
            [1,4,2,3],
            [1,4,2,3],
            [1,4,2,3],
            [1,4,2,3]]
print("Matrice des votes : \n") 
print(showMatrix(matVote,"c","v"))

print("Matrice de condorcet : \n")
matCondorcet = condorcetMatrix(matVote)
print(showMatrix(matCondorcet,"c","c"))

print("Matrice des supérieurs de condorcert : \n")
condoMat = winnerCondorcetMatrix(matCondorcet)
print(showMatrix(condoMat,"c","c"))
print("Gagnant de condorcet : " + winnerCondorcert(condoMat) +"\n")

print("Vecteur de Borda : \n") 
vecBorda = bordaVector(matVote, 3)
print(vecBorda)

