import util

from game import Directions

UNREACHABLE_GOAL_STATE = [Directions.STOP]


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def bfs(problem):
    """
    Q3: BFS
    """
    pass


def iddfs(problem):
    """
    Q1: Iterative deepening depth-first search

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's next states:", problem.getNextStates(problem.getStartState())

    :param problem: instance of SearchProblem
    :return: list of actions
    """
    s = Directions.SOUTH

    current_state = problem.startState, s, 0
    visited = set()
    visited.add(current_state[0])
    route = []

    while not problem.isGoalState(current_state[0]):
        non_visited = False
        nxt = problem.getNextStates(current_state[0])
        for item in nxt:
            if item[0] not in visited:
                route.append(item)
                visited.add(item[0])
                current_state = item
                non_visited = True
                break

        if not non_visited:
            # when we should go back:
            if len(route) == 0:
                return [Directions.STOP]
            current_state = route.pop()

            non_visited = False
            nxt = problem.getNextStates(current_state[0])
            for item in nxt:
                if item[0] not in visited:
                    non_visited = True
                    break

            if non_visited:
                route.append(current_state)

    route = list(map(lambda item: item[1], route))

    return route


def find_nearest_corner(problem, start_state, forbidden, to_target=False):
    current_state = start_state
    queue = [start_state]
    visited = set()

    parents = {current_state[0]: current_state}

    while queue:
        current_state = queue.pop(0)
        visited.add(current_state[0])
        nxt = problem.getNextStates(current_state[0])

        if to_target:
            if problem.isGoalState(current_state[0]):
                route = [current_state[1]]
                current_parent = parents[current_state[0]]
                while parents[current_parent[0]][0] != current_parent[0]:
                    route.append(current_parent[1])
                    current_parent = parents[current_parent[0]]

                route.reverse()
                return route, current_state
        elif len(nxt) == 2 and current_state[0] not in forbidden:
            c1 = nxt[0][0]
            c2 = nxt[1][0]

            if c1[0] != c2[0] and c1[1] != c2[1]:
                route = [current_state[1]]
                current_parent = parents[current_state[0]]
                while parents[current_parent[0]][0] != current_parent[0]:
                    route.append(current_parent[1])
                    current_parent = parents[current_parent[0]]

                route.reverse()
                return route, current_state

        for item in nxt:
            if item[0] not in visited:
                queue.append(item)
                parents[item[0]] = current_state


def hide_and_seek(problem):
    """
    Q2: Hide and seek game !!!!!
    """
    s = Directions.SOUTH
    current_state = problem.startState, s, 0
    forbidden = set()
    forbidden.add(current_state[0])

    route = []

    while True:
        results = find_nearest_corner(problem, current_state, forbidden)
        if results is None:
            break
        else:
            route_curr, current_state = results[0], results[1]
            forbidden.add(current_state[0])
            route += route_curr
            print route

    if not problem.isGoalState(current_state[0]):
        forbidden.clear()
        results = find_nearest_corner(problem, current_state, forbidden, True)
        if results is None:
            route += [Directions.STOP]
        else:
            route_curr, current_state = results[0], results[1]
            route += route_curr
            print route

    return route


def ucs(problem):
    """
    Q4: Search the node of least total cost first.
    """

    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
