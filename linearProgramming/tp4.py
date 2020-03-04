from __future__ import print_function
from ortools.algorithms import pywrapknapsack_solver
from ortools.linear_solver import pywraplp
from ortools.graph import pywrapgraph
import sys
from ortools.linear_solver import pywraplp

def mustLink(solver, coloration, k, t1, t2):
    for i in range(k):
        solver.Add(coloration[t1][i] == coloration[t2][i])

def cannotLink(solver, coloration, k, t1, t2):
    for i in range(k):
        solver.Add(coloration[t1][i] + coloration[t2][i] <= 1)

def distanceHaming(transactions,a,b):
    cpt = 0
    for i in range(len(transactions[0])):
        if not(transactions[a][i] == transactions[b][i]):
            cpt+=1
    return cpt

def loadFile(nomFichier):
    f = open(nomFichier, "r")
    lines = f.read().split('\n')
    f.close()
    tab = []
    for line in lines[:-1]:
        tab.append(line.split())
    return tab

def size(solver, k, coloration, transactions,delta):
    for c in range(k):
        solver.Add(solver.Sum([coloration[i][c] for i in range(len(transactions))]) >= delta)

def equilibre(solver, k, coloration, transactions, delta):
    for c1 in range(k):
        for c2 in range(k):
            diff = solver.Sum([coloration[i][c1] for i in range(len(transactions))]) - solver.Sum([coloration[i][c2] for i in range(len(transactions))])
            if not(diff >= 0):
                diff = -diff
            else:
                diff
            solver.Add(diff <= delta*len(transactions))
            
def exo1(k, transactions, alpha, beta, delta):
    solver = pywraplp.Solver('simple_lp_program', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

    coloration = [[solver.IntVar(0,1,'x(%i,%i' % (i,j)) for i in range(k)] for j in range(len(transactions))]

    #coverTransactions
    for i in range(len(transactions)):
        solver.Add(solver.Sum([coloration[i][c] for c in range(k)]) == 1)
    #isNotEmpty
    for c in range(k):
        solver.Add(solver.Sum([coloration[i][c] for i in range(len(transactions))]) >= 1)
    
    for i in range(len(transactions)):
        for j in range(len(transactions)):
            if i != j:
                distance = distanceHaming(transactions,i,j)
                if distance <= beta:
                    mustLink(solver, coloration, k, i, j)
                if distance >= alpha:
                    cannotLink(solver, coloration, k, i, j)
    deltaMaj = solver.NumVar(0,1,"deltaMaj")
    
    size(solver, k, coloration, transactions, delta)
    equilibre(solver, k, coloration, transactions, deltaMaj)
    # solution
    solver.Minimize(deltaMaj)
    solver.Solve()
    print("Delta = ", deltaMaj.solution_value())
    res = ""
    for i in range(len(coloration)):
        for j in range(len(coloration[i])):
            res+=str(int(coloration[i][j].solution_value())) + " "
        res+= "\n"
    print(res)
        
                    
    
if __name__ == '__main__':
    
    listFichier=["animal.txt", "molecules.txt", "mushroom.txt", "vote.txt"]
    print("Dataset animal : ")
    f = loadFile(listFichier[0])
    exo1(3, f, 8, 2, 2)
    print("Dataset molecules : ")
    f = loadFile(listFichier[1])
    exo1(2, f, 20, 5, 5)
##    print("Dataset mushroom : ")
##    f = loadFile(listFichier[2])
##    exo1(3, f, 8, 2, 2)
##    print("Dataset vote : ")
##    f = loadFile(listFichier[3])
##    exo1(3, f, 8, 2, 2)
    print()
    print("copyright © - MORTELIER Alexis et DE MENEZES Vincent M1 DOP1")
