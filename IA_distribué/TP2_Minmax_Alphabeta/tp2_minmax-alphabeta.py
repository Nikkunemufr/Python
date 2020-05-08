def minmax(depth, arbre, noeud, MAX):
    if depth==0:
        return noeud,[None]
    bestMove=[]
    if MAX:
        bestScore = float('-infinity')
        for fils in arbre[noeud][1]:
            score,move = minmax(depth-1, arbre, fils, False)
            if score > bestScore:
                bestScore = score
                bestMove.extend([fils])
                bestMove.extend(move)
    else:
        bestScore = float('infinity')
        for fils in arbre[noeud][1]:
            score,move = minmax(depth-1, arbre, fils, True)
            if score < bestScore:
                bestScore = score
                bestMove.extend([fils])
                bestMove.extend(move)
    return bestScore,bestMove

def alphabeta(depth, arbre, noeud, MAX, alpha=float('-infinity'), beta=float('infinity')):
    if depth==0:
        return noeud,[None]
    bestMove = []
    
    if MAX:
        for fils in arbre[noeud][1]:
            score,move = alphabeta(depth-1, arbre, fils, False, alpha,beta)
            if score > alpha:
                alpha = score
                bestMove.extend([fils])
                bestMove.extend(move)
                if alpha >= beta:
                    break
        return alpha,bestMove
    else:
        for fils in arbre[noeud][1]:
            score,move = alphabeta(depth-1, arbre, fils, True, alpha,beta)
            if score < beta:
                beta = score
                bestMove.extend([fils])
                bestMove.extend(move)
                if alpha >= beta:
                    break
        return beta,bestMove

arbre = {
    "A":[None,["B","C"]],
    "B":["A",["D","E"]],
    "C":["A",["F","G"]],
    "D":["B",["H","I"]],
    "E":["B",["J","K"]],
    "F":["C",["L","M"]],
    "G":["C",["N","O"]],
    "H":["D",[10,11]],
    "I":["D",[9,12]],
    "J":["E",[14,15]],
    "K":["E",[13,14]],
    "L":["F",[5,2]],
    "M":["F",[4,1]],
    "N":["G",[3,22]],
    "O":["G",[20,21]]
    }
print("arbre :", arbre,"\n")
minMax = minmax(4, arbre, "A", True)
print("Min Max :")
print("-----------------------------")
print("best score : ", minMax[0], "\n")
print("best move : ", minMax[1],"\n")

alphaBeta = alphabeta(4, arbre, "A", True)
print("Alpha beta :")
print("-----------------------------")
print("best score : ", alphaBeta[0], "\n")
print("best move : ", alphaBeta[1],"\n")

