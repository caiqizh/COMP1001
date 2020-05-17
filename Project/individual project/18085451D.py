def solver():
    """
       The main program to print out the path that solves the problem.
       # Input: None
       # Output: None
       """
    setAllStates = genStates()  # Generate a set of all possible states
    # Each state consists of 7 characters, each of which could be
    # E(ast)/W(est)
    # The last character represents the boat's position.


    G = genGraph(setAllStates)  # Generate a graph G from the set of states (nodes)

    start = "EEEEEEE"  # The beginning state where all 7 objects are on the east side
    end = "WWWWWWW"  # The terminating state when the problem is solved

    path = findShortestPath(G, start, end)  # Generate the path by finding a shortest path from
    # a source node start to a destination node end

    printPath(path)  # Print the path in a reading-friendly format

    printMore(G, start, end)  # Print all the path in a reading-friendly format


def genStates(): #generates all 128 states
    """
       A function to generate a set of all possible states
       Input: None
       Output: Return a set of all possible states .
       """

    side = ("E", "W")
    states = []
    for i in side:
        for j in side:
            for k in side:
                for l in side:
                    for m in side:
                        for n in side:
                            for o in side:
                                aState = i + j + k + l + m + n + o  # Concatenate the four locations into a string
                                states.append(aState)  # Add the newly created state to the set of states
    return states

def genGraph(S):
    """
       A function to generate a graph from a set of all possible states S
       Input: A set of all possible states
       Output: Return a graph based on a set of all possible states and given constraints
       """

    setLegalStates = []

    graph = {}


    for n in range(len(S)):
        if isAStateLegal(S[n]) == True:  # check whether a node (state) is legal
            setLegalStates.append(S[n])  # If legal, add n to the set of all legal states

    #   For each legal state n,
    #   First: find the set of other legal nodes that n can connect to
    #   Second: add n and the links to other legal nodes to the graph
    for n in range(len(setLegalStates)):
        setNextNodes = nextStates(setLegalStates[n], setLegalStates)
        graph.update({setLegalStates[n]: setNextNodes})

    return graph

def isAStateLegal(s):
    """
       A function to determine whether a state is legal or not
       Input: A state
       Output: If a state is legal, return true; else, false
       """
    # blue husband/blue wife/green husband/green wife/red husband/red wife/boat
    if (s[1] != s[0] and (s[1] == s[2] or s[1] == s[4])) or \
    (s[3] != s[2] and (s[3] == s[0] or s[3] == s[4])) or \
    (s[5] != s[4] and (s[5] == s[0] or s[5] == s[2])):
    # The wife cannot stay with other men without her husband.

        return False
    else:
        return True

def nextStates(aState, allStates):
    """
       A function to return a set of states that a given state can go to directly.
       Input: aState is a state and allStates is a set of states.
       Output: Return a set of states that aState can go to (i.e., neighboring states).
       """
    neighborStates = []

    # classify the set of states into two: boat is on the east/west sides
    setManEast, setManWest = classifyManPos(allStates)

    if aState[6] == "E":
        setCandidates = setManWest
    else:
        setCandidates = setManEast

    # Determine which states could be reached by the given state
    for m in setCandidates:
        # Check whether node m is a neighbor of aState
        if neighborNode(aState, m) == True:
            neighborStates.append(m)

    return neighborStates

def classifyManPos(S):
    """
        A function to classify the states S into two groups:
        - States where the boat is on the east side
        - States where the boat is on the west side
        Input: A set of states
        Output: Return the two sets of states, first the east-side states and then the west-side states.
        """
    setEast = []
    setWest = []
    for n in S:
        if n[6] == "E":
            setEast.append(n)
        else:
            setWest.append(n)

    return setEast, setWest

def getPos(astate):
    '''
        A function to get how many people in the east side and west side in one state
        Input: astate
        Output: how many people in the west side and how many people in east side.
    '''

    east = 0
    west = 0
    for i in range(len(astate)-1):
        if astate[i] is 'E':
            east += 1
        else:
            west += 1
    return east, west

def neighborNode(n1, n2):
    '''
       A function to determine whether n1 and n2 are neighbor nodes.
       Input: n1 n2
       Output: True or False
    '''
    if n1[6] == n2[6]:  # The boat should be in different side.
        return False
    else:
        diff = 0
        for index in range(0,len(n1)-1):
            if n1[index] != n2[index]:
                    diff = diff + 1
            # Find how many people have been moved.

        if diff <= 2 and diff > 0: # There should be at least one person and at most 2 people moving to the other side.
            peopleInEast1, peopleInWest1= getPos(n1)
            peopleInEast2, peopleInWest2 = getPos(n2)
            if n1[6] == 'E':
                if (peopleInEast1 - peopleInEast2 >= 1 and peopleInEast1 - peopleInEast2 <= 2):
                    return True
            else:
                if (peopleInWest1 - peopleInWest2 >=1 and peopleInWest1 - peopleInWest2 <= 2):
                    return True
            # If the boat is in the east side, there must be at least 1 and at most 2 people moving from east to west.


        else:
            return False

def findShortestPath(graph, start, end, path=[]):
    """
       A function to find a shortest path from start to end on a graph
       This function is obtained from https://www.python.org/doc/essays/graphs/
       with one change due to the deprecation of the method has_key().

       Input: A graph, a starting node, an end node and an empty path
       Output: Return the shortest path in the form of a list.
       """
    path = path + [start]
    if start == end:
        return path
    if not (start in graph):
        return None
    shortestPath = None
    for node in graph[start]:
        if node not in path:
            newpath = findShortestPath(graph, node, end, path)
            if newpath:
                if not shortestPath or len(newpath) < len(shortestPath):
                    shortestPath = newpath
    return shortestPath

def find_all_paths(graph, start, end, path=[]):
    """
    A function to find all the shortest path from start to end on a graph
    This function is obtained from https://www.python.org/doc/essays/graphs/
    with one change due to the deprecation of the method has_key().

    Input: A graph, a starting node, an end node and an empty path
    Output: Return all the shortest path in the form of a list.
    """

    path = path + [start]
    if start == end:
        return [path]
    if not start in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def printPath(path):
    """
    A function to print out the solution in a reading friendly format.
    Input: A shortest path
    Output: None
    """
    for nodeOnPath in range(len(path) - 1):
        # For each node on the path, except the last one, determine
        if path[nodeOnPath][6] == "E":
            fromDirection = "east"
            toDirection = "west"
        else:
            fromDirection = "west"
            toDirection = "east"
        names = [] # A list containing the people who just crossed the river.
        for j in range(0, 6):
            if path[nodeOnPath][j] != path[nodeOnPath + 1][j]:
                names.append(j)
        nameList = ["blue husband","blue wife","green husband","green wife","red husband","red wife"]
        if len(names) == 1:
            print(str(nodeOnPath + 1) + " The " + nameList[names[0]] + " goes from the " + fromDirection + ' to the ' + toDirection + ".")
        # If only one person moved, there is another format for this situation.
        else:
            name1 = nameList[names[0]]
            name2 = nameList[names[1]]
            print(str(nodeOnPath + 1) + " The " + name1 + " and " \
                  + name2 + " go from the " + fromDirection + ' to the ' + toDirection + ".")


def printMore(G, start, end):
    """
        A function to print out all the solutions in a reading friendly format.
        Input: G(genGraph), start, end
        Output: None
        """
    print()
    print()
    print('Do you want to get all the methods?')
    print('You may wait a while to print all the methods.  (y/s)')
    
    if input() == 'y':
        path = find_all_paths(G, start, end)  # Generate the path by finding a shortest path from
        methodsNum = 0
        for i in path:
            if len(i) == 12:
                printPath(i)
                print()
                methodsNum += 1
        print('There are totally ' + str(methodsNum) + ' methods.')
        print()
        print('That is all of Alex\'s project.')
    else:
        print('That is all of Alex\'s project.')

solver()
