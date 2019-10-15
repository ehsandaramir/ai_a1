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

    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


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
