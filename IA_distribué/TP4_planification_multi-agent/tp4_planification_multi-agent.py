from random import *
import itertools
"""
    author: Alexis MORTELIER - 21605783
    date:04/05/2020
"""

def generate_grid(n):
    """ Genere une grille en deux dimensions de taille n
    :param n: taille de la grille
    :return: grille vide
    """
    grid = ['_'] * n
    for i in range(n):
        grid[i] = ['_'] * n
    return grid


def alea_grid(n, nbObstacle, nbRobot=1):
    """
    Retourne une grille remplis aleatoirement d'obstacles, de robots et de cible
    :param n: taille de la grille
    :param nbObstacle: nombre d'obstacle
    :param nbRobot:  nombre de robots
    :return: grille de taille n remplis aleatoirement d'obstacles, de robots et de cible
    """
    grid = generate_grid(n)
    res = {"grid": grid, "robot": [], "target": [], "length": n}

    cases = [(x, y) for x in range(n) for y in range(n) if x != 0 or y != 0]
    alea = sample(cases, nbObstacle + nbRobot * 2)
    for (i, j) in alea[0:nbObstacle]:
        grid[i][j] = 'O'
    for (i, j) in alea[nbObstacle:nbObstacle + nbRobot]:
        grid[i][j] = '*'
        res["robot"].append((i, j))
    for (i, j) in alea[nbObstacle + nbRobot:nbObstacle + 2 * nbRobot]:
        grid[i][j] = 'T'
        res["target"].append((i, j))
    return res


def show_grid(grid):
    """
    Affiche la grille bien formaté
    :param grid: grille de jeu
    :return: string d'affichage de la grille
    """
    res = ""
    for i in range(len(grid)):
        for j in range(len(grid)):
            res += str(grid[i][j]) + " "
        res += "\n"
    return res


def progression(etat, action):
    """
    Avancement de l'etat actuelle de la grille à son état suivant
    :param etat: etat de la grille
    :param action: action de deplacements du ou des robots
    :return: l'etat suivant de la grille
    """
    for indexRobot in range(len(etat["robot"])):
        etat["grid"][etat["robot"][indexRobot][0]][etat["robot"][indexRobot][1]] = "_"
        etat["robot"][indexRobot] = (
            etat["robot"][indexRobot][0] + action[indexRobot][0], etat["robot"][indexRobot][1] + action[indexRobot][1])
        etat["grid"][etat["robot"][indexRobot][0]][etat["robot"][indexRobot][1]] = "*"
    return etat


def Activable(I):
    """
    Retourne la liste des actions possible pour chaque robot à un etat I
    :param I: etat de la grille
    :return: la liste des actions possible pour chaque robot
    """
    actions = []
    for i,robot in enumerate(I["robot"]):
        action = [(0, 0)]
        if robot != I["target"][i]:
            if robot[0] - 1 >= 0 and robot[0] - 1 < I["length"] and I["grid"][robot[0] - 1][robot[1]] != 'O' and \
                    I["grid"][robot[0] - 1][robot[1]] != '*':
                action.append((-1, 0))
            if robot[0] + 1 >= 0 and robot[0] + 1 < I["length"] and I["grid"][robot[0] + 1][robot[1]] != 'O' and \
                    I["grid"][robot[0] + 1][robot[1]] != '*':
                action.append((1, 0))
            if robot[1] - 1 >= 0 and robot[1] - 1 < I["length"] and I["grid"][robot[0]][robot[1] - 1] != 'O' and \
                    I["grid"][robot[0]][robot[1] - 1] != '*':
                action.append((0, -1))
            if robot[1] + 1 >= 0 and robot[1] + 1 < I["length"] and I["grid"][robot[0]][robot[1] + 1] != 'O' and \
                    I["grid"][robot[0]][robot[1] + 1] != '*':
                action.append((0, 1))
        actions.append(action)
        i += 1
    return actions

def Heuristique(etat, indexRobot, action):
    """
    Heurisitque du coup de l'action pour un robot donné
    :param etat: etat de la grille
    :param indexRobot: numero du robot
    :param action: action demandé au robot
    :return: un entier indiquant le coup de l'action
    """
    return abs((etat["robot"][indexRobot][0] + action[0]) - etat["target"][indexRobot][0]) + abs(
                (etat["robot"][indexRobot][1] + action[1]) - etat["target"][indexRobot][1])


def meilleur_action(etat, actions):
    """
    Retourne une liste de la meilleur action pour chaque robot
    :param etat: etat de la grille
    :param actions: liste des actions possible des robots
    :return: une liste de la meilleur action pour chaque robot
    """
    best_action = []
    for indexRobot in range(len(actions)):
        heuristique = float("infinity")
        robot_best_action = ()
        for action in actions[indexRobot]:
            h = Heuristique(etat, indexRobot, action)
            if h < heuristique:
                heuristique = h
                robot_best_action = action
        best_action.append(robot_best_action)
    return best_action

def gen_utility_matrix(etat, actions):
    utilityMatrix = []
    for indexRobot in range(len(actions)):
        heuristique_robot = []
        for action in actions[indexRobot]:
            heuristique_robot.append(Heuristique(etat, indexRobot, action))
        utilityMatrix.append(heuristique_robot)
    return utilityMatrix

def gen_index_matrix(matrix):
    newMatrix = []
    for i in range(len(matrix)):
        line = []
        for j in range(len(matrix[i])):
            line.append(j)
        newMatrix.append(line)
    return newMatrix

def compute_CUFutilitarist(collectivity):
    utilitarist = 0
    for tache in collectivity:
        utilitarist += tache
    return utilitarist

def computeCommunities(utilityMatrix, allocations):
    communities = []
    for alloc in allocations:
        collectivity = []
        for i in range(len(utilityMatrix)):
            collectivity.append(utilityMatrix[i][alloc[i]-1])
        communities.append(compute_CUFutilitarist(collectivity))
    return communities

def meilleur_actionJointe(etat, actions):
    """
    Retourne une liste de la meilleur combinaisons d'actions pour chaque robot
    :param etat: etat de la grille
    :param actions: liste des actions possible des robots
    :return: une liste de la meilleur action pour chaque robot
    """  
    utilityMatrix = gen_utility_matrix(etat, actions)
    matrixIndexActions = gen_index_matrix(actions)
    allocations = list(itertools.product(*matrixIndexActions))

    communities = computeCommunities(utilityMatrix, allocations)
    tampon = 0
    index_best_action = []
    for i in range(len(communities)):
        if communities[i] >= tampon:
            tampon = int(communities[i])
            index_best_action = allocations[i]
    
    return [actions[0][index_best_action[0]],actions[1][index_best_action[1]]]


def planification_mixte(IG, mixte, plan):
    """
    Retourne un plan mixte donnant les déplacements du robot pour atteindre sa cible
    :param IG: etat de la partie
    :param mixte: ordre d'action à un état définie.
    :param plan: plan d'action du robot
    :return: liste d'actions
    """
    if IG["robot"] == IG["target"]:
        return plan
    else:
        Iinmixte = False
        a_mixte = 0
        for S_mixte, A_mixte in mixte:
            if IG["grid"] == S_mixte:
                Iinmixte = True
                a_mixte = A_mixte
                break
        if Iinmixte:
            plan.append(a_mixte)
            planification_mixte(progression(IG, a_mixte), mixte, plan)
        else:
            actions = Activable(IG)
            best_action = meilleur_action(IG, actions)
            plan.append(best_action)
            planification_mixte(progression(IG, best_action), mixte, plan)
    return plan


def egal(IG):
    """
    teste l’égalité composant par composant
    :param IG: état de la grille
    :return: booléen indiquant si les robot ont atteint leur cible
    """
    for i in range(len(IG["robot"])):
        if IG["robot"][i] != IG["target"][i]:
            return False
    return True


def planification_jointe(IG, plan):
    """
    Construction d'un plan d'actions jointe
    :param IG: etat de la partie
    :param plan: plan d'action du robot
    :return: liste d'actions
    """
    if egal(IG):
        return plan
    else:
        JointActions = Activable(IG)
        best_action = meilleur_actionJointe(IG, JointActions)
        plan.append(best_action)
        planification_jointe(progression(IG, best_action), plan)
    return plan

def planification_avant_coordination(IG):
    planif_locale = planification_jointe(IG,[])
    game = IG
    for etape in planif_locale:
        game = progression(game,etape)
        for i,robot1 in enumerate(game["robot"]):
            for j,robot2 in enumerate(game["robot"]):
                if robot1 == robot2:
                    break
                    #Change ton plan
    return plan

def planification_pendant_coordination(IG):
    return

game = alea_grid(10, 2)
print("Planfication mixte :")
print(show_grid(game["grid"]))
print("Taille du jeu :", game["length"])
print("position du robot :", game["robot"])
print("position de la cible :", game["target"])
print("-------------------------------------")
plan = planification_mixte(game, [((3, 3), (-1, 0)), ((2, 2), (-1, 0)), ((15, 15), (1, 0))], [])
print(plan)
print("-------------------------------------")
game = alea_grid(10, 2, 2)
print("Planfication jointe :")
print(show_grid(game["grid"]))
print("Taille du jeu :", game["length"])
print("position du robot :", game["robot"])
print("position de la cible :", game["target"])
print("-------------------------------------")
plan = planification_jointe(game, [])
print(plan)
print("-------------------------------------")
