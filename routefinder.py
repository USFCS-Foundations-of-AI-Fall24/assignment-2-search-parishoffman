from queue import PriorityQueue
from Graph import Graph, Node, Edge
import math


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
    search_queue.put(start_state)
    ## you do the rest.
    states = 0

    if use_closed_list :
        closed_list[start_state] = True

    while search_queue.qsize() > 0 :
        states += 1
        next_state = search_queue.get()
        # print("Next state: ", next_state)
        if goal_test(next_state):
            print("Goal found")
            print("States: ", states)
            # print(next_state)
            # ptr = next_state
            # while ptr is not None :
            #     ptr = ptr.prev
            #     # print(ptr)
            return
        else :
            # successors = next_state.successors(action_list)
            successors = []
            heuristic = heuristic_fn(next_state)
            for edge in next_state.mars_graph.get_edges(Node(next_state.location)) :
                successors.append(
                    map_state(
                        g=next_state.g + 1,
                        h=heuristic,
                        location=edge.dest.value,
                        mars_graph=next_state.mars_graph,
                        prev_state=next_state,
                    )
                )
            if use_closed_list :
                successors = [item for item in successors
                                    if item not in closed_list]
                for s in successors :
                    closed_list[s] = True
            for succ in successors :
             search_queue.put(succ)

## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

## you do this - return the straight-line distance between the state and (1,1)
def sld(state) :
    data = state.location.split(",")
    return math.sqrt(math.pow(1 - int(data[0]), 2) + math.pow(1 - int(data[1]), 2))

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
