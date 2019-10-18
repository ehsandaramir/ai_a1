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

    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


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


def hide_and_seek(problem):
    """
    Q2: Hide and seek game !!!!!
    """

    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def ucs(problem):
    """
    Q4: Search the node of least total cost first.
    """

    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
