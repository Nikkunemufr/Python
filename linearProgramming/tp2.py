from __future__ import print_function
from ortools.algorithms import pywrapknapsack_solver
from ortools.linear_solver import pywraplp
from ortools.graph import pywrapgraph

def exo1():
    # Create the solver.
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.
        KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')

    values = [40, 30, 25, 25, 10]
    weights = [[10, 4, 3, 2, 1]]
    capacities = [15]

    solver.Init(values, weights, capacities)
    computed_value = solver.Solve()

    packed_items = []
    packed_weights = []
    total_weight = 0
    print('Total value =', computed_value)
    for i in range(len(values)):
        if solver.BestSolutionContains(i):
            packed_items.append(i)
            packed_weights.append(weights[0][i])
            total_weight += weights[0][i]
    print('Total weight:', total_weight)
    print('Packed items:', packed_items)
    print('Packed_weights:', packed_weights)


def exo2():
    solver = pywraplp.Solver('simple_lp_program', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    x1 = solver.IntVar(0, solver.infinity(), 'x1')
    x2 = solver.IntVar(0, solver.infinity(), 'x2')
    x3 = solver.IntVar(0, solver.infinity(), 'x3')

    c1 = solver.Constraint(36, solver.infinity(), 'c1')
    c1.SetCoefficient(x1, 3)
    c1.SetCoefficient(x2, 1)
    c2 = solver.Constraint(24, solver.infinity(), 'c2')
    c2.SetCoefficient(x2, 1)
    c2.SetCoefficient(x3, 2)

    objective = solver.Objective()
    objective.SetCoefficient(x1, 16)
    objective.SetCoefficient(x2, 25)
    objective.SetCoefficient(x3, 10)
    objective.SetMinimization()

    solver.Solve()
    print('Solution:')
    print('Objective value =', objective.Value())
    print('x1 =', x1.solution_value())
    print('x2 =', x2.solution_value())
    print('x3 =', x3.solution_value())

def exo3():
    solver = pywraplp.Solver('simple_lp_program', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

    list_secteur = []
    for i in range(11):
        list_secteur.append(solver.IntVar(1, solver.infinity(), 'x'+str(i+1)))
    
    couverture = [[1,1,1,1,0,0,0,0,0,0,0],
           [0,1,1,0,1,0,0,0,0,0,0],
           [0,1,1,1,1,1,0,0,0,0,0],
           [1,0,1,1,0,1,1,0,0,0,0],
           [0,1,1,0,1,0,0,0,1,0,0],
           [0,0,1,1,1,1,1,1,0,0,0],
           [0,0,0,1,0,1,1,1,0,0,0],
           [0,0,0,0,1,1,1,1,1,1,0],
           [0,0,0,0,1,0,0,1,1,1,1],
           [0,0,0,0,0,0,0,1,1,1,1],
           [0,0,0,0,0,0,0,0,1,1,1]]
    for i in range(11):
        c = solver.Constraint(36, solver.infinity(), 'c'+str(i+1))
        for j in range(11):
            c.SetCoefficient(list_secteur[j], couverture[j][i])
    
    objective = solver.Objective()
    for secteur in list_secteur:
        objective.SetCoefficient(secteur,1)
    objective.SetMinimization()

    solver.Solve()
    print('Solution:')
    print('Objective value =', objective.Value())
    for secteur in list_secteur:
        print('x =', secteur.solution_value())


if __name__ == '__main__':
    print("Exercice 1 : ")
    exo1()
    print("Exercice 2 : ")
    exo2()
    print("Exercice 3 : ")
    exo3()
    
