from collections import deque

## We will append tuples (state, "action") in the search queue
def breadth_first_search(startState, action_list, goal_test, use_closed_list=True) :
    search_queue = deque()
    closed_list = {}
    states = 0

    search_queue.append((startState,""))
    if use_closed_list :
        closed_list[startState] = True
    while len(search_queue) > 0 :
        states += 1
        ## this is a (state, "action") tuple
        next_state = search_queue.popleft()
        # print("Next state: ", next_state)
        if goal_test(next_state[0]):
            print("Goal found")
            print("States: ", states)
            # print(next_state)
            ptr = next_state[0]
            while ptr is not None :
                ptr = ptr.prev
                # print(ptr)
            return next_state[0]
        else :
            successors = next_state[0].successors(action_list)
            if use_closed_list :
                successors = [item for item in successors
                                    if item[0] not in closed_list]
                for s in successors :
                    closed_list[s[0]] = True
            search_queue.extend(successors)

### Note the similarity to BFS - the only difference is the search queue
## use the limit parameter to implement depth-limited search
def depth_first_search(startState, action_list, goal_test, use_closed_list=True, limit=0) :
    search_queue = deque()
    closed_list = {}
    states = 1

    search_queue.append((startState,""))
    if use_closed_list :
        closed_list[startState] = True

    depth = 0
    while len(search_queue) > 0 :
        depth += 1
        if depth == limit :
            break
        next_state = search_queue.pop()
        if goal_test(next_state[0]):
            print("Goal found")
            # print(next_state)
            ptr = next_state[0]
            while ptr is not None :
                ptr = ptr.prev
                # print(ptr)
            print("States: ", states)
            return next_state[0]
        else :
            successors = next_state[0].successors(action_list)
            states += len(successors)
            if use_closed_list :
                successors = [item for item in successors
                                    if item[0] not in closed_list]
                for s in successors :
                    closed_list[s[0]] = True
            search_queue.extend(successors)
