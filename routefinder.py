from queue import PriorityQueue

from Graph import Graph, Node, Edge


class map_state() :
    ## f = total estimated cost
    ## g = cost so far
    ## h = estimated cost to goal
    def __init__(self, location="", mars_graph=None,
                 prev_state=None, g=0,h=0):
        self.location = location
        self.mars_graph = mars_graph
        self.prev_state = prev_state
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

    def __repr__(self):
        return "(%s)" % (self.location)

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def is_goal(self):
        return self.location == '1,1'


def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True) :
    search_queue = PriorityQueue()
    closed_list = {}
    search_queue.put((start_state, "start"))
    ## you do the rest.

    while search_queue.qsize() > 0:
        next_state = search_queue.get()

        if goal_test(next_state[0]) :
            ptr = next_state[0]
            while


## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

## you do this - return the straight-line distance between the state and (1,1)
def sld(state) :
    sqt(a^ + b2)

## you implement this. Open the file filename, read in each line,
## construct a Graph object and assign it to self.mars_graph().
def read_mars_graph(filename):
    new_graph = Graph()
    file = open(filename)
    lines = file.readlines()
    data = [(source, destinations.split()) for line in lines for source, destinations in
            [line.split(':')]]

    for tuple in data:
        source_node, destinations = Node(tuple[0]), tuple[1]
        for destination in destinations:
            dest_node = Node(destination)
            new_graph.add_edge(Edge(source_node, dest_node))
    return new_graph
