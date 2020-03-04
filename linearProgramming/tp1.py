from ortools.linear_solver import pywraplp
from ortools.graph import pywrapgraph

def exo2():
    solver = pywraplp.Solver('simple_lp_program', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    x1 = solver.IntVar(0, solver.infinity(), 'x1')
    x2 = solver.IntVar(0, solver.infinity(), 'x2')

    c1 = solver.Constraint(-solver.infinity(), 400, 'c1')
    c1.SetCoefficient(x1, 1)
    c1.SetCoefficient(x2, 1)
    c2 = solver.Constraint(-solver.infinity(), 600, 'c2')
    c2.SetCoefficient(x1, 1)
    c2.SetCoefficient(x2, 2)

    objective = solver.Objective()
    objective.SetCoefficient(x1, 10000)
    objective.SetCoefficient(x2, 16000)
    objective.SetMaximization()

    solver.Solve()

    print('Solution:')
    print('Objective value =', objective.Value())
    print('petite voiture =', x1.solution_value())
    print('grosse voiture =', x2.solution_value())

def exo3():
    solver = pywraplp.Solver('simple_lp_program', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    x1 = solver.IntVar(0, solver.infinity(), 'x1')
    x2 = solver.IntVar(0, solver.infinity(), 'x2')

    c1 = solver.Constraint(-solver.infinity(), 3, 'c1')
    c1.SetCoefficient(x1, 1)
    c1.SetCoefficient(x2, 2)
    c2 = solver.Constraint(-solver.infinity(), 15, 'c2')
    c2.SetCoefficient(x1, 6)
    c2.SetCoefficient(x2, 8)

    objective = solver.Objective()
    objective.SetCoefficient(x1, -3)
    objective.SetCoefficient(x2, -5)
    objective.SetMinimization()

    solver.Solve()

    print('Solution:')
    print('Objective value =', objective.Value())
    print('x1 =', x1.solution_value())
    print('x2 =', x2.solution_value())

def exo4():
    start_nodes =   [0, 0, 1, 1, 2, 3, 3, 4]
    end_nodes =     [1, 2, 2, 3, 4, 4, 5, 5]
    capacities =    [3, 3, 2, 3, 2, 4, 2, 3]

    # Instantiate a SimpleMaxFlow solver.
    max_flow = pywrapgraph.SimpleMaxFlow()
    # Add each arc.
    for i in range(0, len(start_nodes)):
        max_flow.AddArcWithCapacity(start_nodes[i], end_nodes[i], capacities[i])
        # Find the maximum flow between node 0 and node 4.
    if max_flow.Solve(0, 5) == max_flow.OPTIMAL:
        print('Max flow:', max_flow.OptimalFlow())
        print('')
        print('  Arc    Flow / Capacity')
        for i in range(max_flow.NumArcs()):
            print('%1s -> %1s   %3s  / %3s' % (
            max_flow.Tail(i),
            max_flow.Head(i),
            max_flow.Flow(i),
            max_flow.Capacity(i)))
        print('Source side min-cut : ', max_flow.GetSourceSideMinCut())
        print('Sink side min-cut : ', max_flow.GetSinkSideMinCut())
    else:
        print("Il y a eu un problème avec l'entrée du flot maximum.")

def exo5():
    #start_nodes =   [1,1,1,2,2,3,3,4,4,5,5,5,6,7,7,8,9,10,11,11]
    #end_nodes =     [3,5,6,5,6,4,5,8,9,8,9,10,7,9,10,12,12,12,1,2]
    #capacities =    [17,14,0,6,15,7,10,7,0,10,5,15,15,5,10,17,15,20,31,21]
    #unit_costs =   [20,15,12,6,22,15,10,7,10,10,15,15,22,10,10,18,15,20,35,25]
    #supplies =      [1,2,3,4,5,6,7,8,9,10,11,12]
    start_nodes = [ 0, 0,  1, 1,  1,  2, 2,  3, 4]
    end_nodes   = [ 1, 2,  2, 3,  4,  3, 4,  4, 2]
    capacities  = [15, 8, 20, 4, 10, 15, 4, 20, 5]
    unit_costs  = [ 4, 4,  2, 2,  6,  1, 3,  2, 3]
    supplies = [20, 0, 0, -5, -15]

    min_cost_flow = pywrapgraph.SimpleMinCostFlow()

    for i in range(0, len(start_nodes)):
        min_cost_flow.AddArcWithCapacityAndUnitCost(start_nodes[i], end_nodes[i],
                                                capacities[i], unit_costs[i])
    for i in range(0, len(supplies)):
        min_cost_flow.SetNodeSupply(i, supplies[i])

    if min_cost_flow.Solve() == min_cost_flow.OPTIMAL:
        print('Minimum cost:', min_cost_flow.OptimalCost())
        print('')
        print('  Arc    Flow / Capacity  Cost')
        for i in range(min_cost_flow.NumArcs()):
            cost = min_cost_flow.Flow(i) * min_cost_flow.UnitCost(i)
            print('%1s -> %1s   %3s  / %3s       %3s' % (
                min_cost_flow.Tail(i),
                min_cost_flow.Head(i),
                min_cost_flow.Flow(i),
                min_cost_flow.Capacity(i),
                cost))
    else:
        print("Il y a eu un problème avec l'entrée du flot minimal.")



if __name__ == '__main__':
    print("Exo2 : \n")
    exo2()
    print("Exo3 : \n")
    exo3()
    print("Exo4 : \n")
    exo4()
    print("Exo5 : \n")
    exo5()
