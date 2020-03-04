from __future__ import print_function
from ortools.algorithms import pywrapknapsack_solver
from ortools.linear_solver import pywraplp
from ortools.graph import pywrapgraph
import sys
from ortools.linear_solver import pywraplp

def kColorations(k):
    solver = pywraplp.Solver('simple_lp_program', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

    color_numbers = k

    # number of nodes
    n = 10
    # set of nodes
    V = list(range(n))

    num_edges = 15

    E = [[1,2],
         [1,3],
         [1,4],
         [2,5],
         [2,9],
         [3,7],
         [3,8],
         [4,6],
         [4,10],
         [5,6],
         [5,8],
         [6,7],
         [7,9],
         [8,10],
         [9,10]]
    
    # x[i,c] = 1 means that node i is assigned color c
    coloration = {}
    for v in V:
        for j in range(color_numbers):
          coloration[v, j] = solver.IntVar(0, 1, 'v[%i,%i]' % (v, j))

    # u[c] = 1 means that color c is used, i.e. assigned to some node
    u = [solver.IntVar(0, 1, 'u[%i]' % i) for i in range(color_numbers)]

    # number of colors used, to minimize
    obj = solver.Sum(u)

    # constraints
    # each node must be assigned exactly one color
    for i in V:
        solver.Add(solver.Sum([coloration[i, c] for c in range(color_numbers)]) == 1)

    # adjacent nodes cannot be assigned the same color
    # (and adjust to 0-based)
    for i in range(num_edges):
        for c in range(color_numbers):
          solver.Add(coloration[E[i][0] - 1, c] + coloration[E[i][1] - 1, c] <= u[c])

    # objective
    objective = solver.Minimize(obj)

    # solution
    solver.Solve()

    print()
    print('number of colors:', int(solver.Objective().Value()))
    print()

    for v in V:
       print('v%i' % v, ' color ', end=' ')
       for c in range(color_numbers):
          if int(coloration[v, c].SolutionValue()) == 1:
            print(c)

def sudoku():
    solver = pywraplp.Solver('simple_lp_program', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

    n = 9
    range_n = range(1, n + 1)

    X = -1
    # Example from Wikipedia
    givens = [[5, 3, X, X, 7, X, X, X, X],
            [6, X, X, 1, 9, 5, X, X, X],
            [X, 9, 8, X, X, X, X, 6, X],
            [8, X, X, X, 6, X, X, X, 3],
            [4, X, X, 8, X, 3, X, X, 1],
            [7, X, X, X, 2, X, X, X, 6],
            [X, 6, X, X, X, X, 2, 8, X],
            [X, X, X, 4, 1, 9, X, X, 5],
            [X, X, X, X, 8, X, X, 7, 9]]

    #
    # variables
    #

    # x[i,j,k] = 1 means cell [i,j] is assigned number k
    x = {}
    for i in range_n:
        for j in range_n:
            for k in range_n:      
                x[i,j, k] = solver.IntVar(0, 1, 'x[%i,%i,%i]' % (i, j, k))

    # constraints
    # assign pre-defined numbers using the "givens"
    for i in range_n:
        for j in range_n:
            for k in range_n:
                if givens[i-1][j-1] > X:
                    if givens[i-1][j-1] == k:
                        solver.Add(x[i,j,k] == 1)
                    else:
                        solver.Add(x[i,j,k] == 0)

    # each cell must be assigned exactly one number 
    for i in range_n:
        for j in range_n:
            solver.Add(solver.Sum([x[i,j,k] for k in range_n]) == 1)

    # cells in the same row must be assigned distinct numbers
    for i in range_n:
        for k in range_n:
            solver.Add(solver.Sum([x[i,j,k] for j in range_n]) == 1)

    # cells in the same column must be assigned distinct numbers
    for j in range_n:
        for k in range_n:
            solver.Add(solver.Sum([x[i,j,k] for i in range_n]) == 1)

    # cells in the same region must be assigned distinct numbers
    R = [1, 4, 7]
    for I in R:
        for J in R:
            for k in range_n:
                solver.Add(solver.Sum([x[i,j,k]
                               for i in range(I,I+3)
                               for j in range(J,J+3)])  == 1)


    # solution
    solver.Solve()

    res = []
    liste=[]
    print()
    print ('Modele:')
    print("¯¯¯¯¯¯¯")
    print_sudoku_jolie(givens)
    print()
    print ('Solution:')
    print("¯¯¯¯¯¯¯¯¯")
    print()
    for i in range_n:
        for j in range_n:
            for k in range_n:
                if x[i,j,k].solution_value() == 1:
                  liste.append(k)
        res.append(liste)
        liste=[]
    res=print_sudoku_jolie(res)


def print_sudoku_jolie(grille):
    print("-------------------------")
    bigcompteur=0
    for i in range(len(grille)):
        chaine = "| "
        compteur=0
        for j in range(len(grille[i])):
            compteur+=1
            if str(grille[i][j]) == str(-1):
                chaine += "."
            else:
                chaine += str(grille[i][j])
            if compteur == 3:
                chaine+= " | "
                compteur=0
            else:
                chaine+=" "
                
        print(chaine)
        bigcompteur+=1
        if bigcompteur == 3:
            print("-------------------------")
            bigcompteur=0

            

if __name__ == '__main__':
    print("Exercice k-colorations : ")
    kColorations(3)
    print()
    print("Sudoku:")
    print("¯¯¯¯¯¯¯")
    sudoku()
    print("")
    print("")
    print("")
    print("copyright © - Print de DE MENEZES Vincent M1 DOP1")
    print("copyright © - Development de MORTELIER Alexis M1 DOP1")

