def genStates():
    """
    A function to generate a set of all possible states (E/W,E/W,E/W)
    Input: None
    Output: Return a set of all possible states in a Python tuple. Each state is implemented as a string of three binary values 'E'/'W'.
    """

    direction = ("E","W")
    states = []
    for i in direction:
        for j in direction:
            for k in direction:
                    aState = i + j + k      # Concatenate the three locations into a string
                    states.append(aState)   # Add the newly created state to the set of states
    return tuple(states)


def fullyConnectedGraph(S):
    """
    A function to generate a graph which contains all possible links among the 8 nodes
    Input: A set of all possible states
    Output: Return a graph which contains all possible links among the 8 nodes.
    """
    graph = {}
    # consider each state s in S
    for state1 in S:
        neighbors = []
        # find out which states in S differ from s by only 1 position
        for state2 in S:
            diff = 0
            for i in range(3):
                if state1[i] != state2[i]:
                    diff += 1
            # add to the graph if neighbor found
            if diff == 1:
                neighbors.append(state2)
        graph[state1] = neighbors
                    
    return graph

print(fullyConnectedGraph(genStates()))
