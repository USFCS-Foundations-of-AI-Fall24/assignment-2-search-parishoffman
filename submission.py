from mapcoloring import solve_antenna
from mars_planner import *

# Name: Paris Hoffman
if __name__ == "__main__" :
    action_list = [
                   move_to_sample, extract_sample,
                   pick_up_sample, move_to_station, drop_sample,
                   move_to_battery, charge
                ]

    print("before adding tool functions")
    run_program(breadth_first_search, action_list, RoverState(), mission_complete)
    run_program(depth_first_search, action_list, RoverState(), mission_complete)
    run_program(depth_first_search, action_list, RoverState(), mission_complete, 5)

    print("after adding tool functions")
    action_list = [
                   move_to_sample, pick_up_tool, extract_sample, drop_tool,
                   pick_up_sample, move_to_station, drop_sample,
                   move_to_battery, charge
                ]
    run_program(breadth_first_search, action_list, RoverState(), mission_complete)
    run_program(depth_first_search, action_list, RoverState(), mission_complete)
    run_program(depth_first_search, action_list, RoverState(), mission_complete, 5)

    print("After using problem decomposition")
    def reached_sample(state):
        return state.loc == "sample"

    def extracted_sample(state):
        return state.sample_extracted and state.holding_tool == False

    print("BFS:")
    action_list = [move_to_sample]
    state = breadth_first_search(RoverState(), action_list, reached_sample)
    action_list = [pick_up_tool, extract_sample, drop_tool]
    next_state = breadth_first_search(state, action_list, extracted_sample)
    action_list = [move_to_station, drop_sample, move_to_battery, charge]
    breadth_first_search(next_state, action_list, mission_complete)

    print("DFS:")
    action_list = [move_to_sample]
    state = depth_first_search(RoverState(), action_list, reached_sample)
    action_list = [pick_up_tool, extract_sample, drop_tool]
    next_state = depth_first_search(state, action_list, extracted_sample)
    action_list = [move_to_station, drop_sample, move_to_battery, charge]
    depth_first_search(next_state, action_list, mission_complete)

    def complete(state) :
        return state.is_goal()
    start_state = map_state(location="8,8", mars_graph=read_mars_graph("marsmap"))
    print("A*: ")
    a_star(start_state, sld, complete)
    print("Uniform Cost Search: ")
    a_star(start_state, h1, complete)

    print("Antenna Problem:")
    solve_antenna()


