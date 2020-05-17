def genStates(): #generates all 64 states
    side = ("E", "W")
    states = []
    for i in side:
        for j in side:
            for k in side:
                for l in side:
                    for m in side:
                        for n in side:
                            for o in side:
                                aState = i + j + k + l + m + n + o
                                states.append(aState)
    return states

def isAStateLegal(s):
    if (s[1] != s[0] and (s[1] == s[2] or s[1] == s[4])) or \
    (s[3] != s[2] and (s[3] == s[0] or s[3] == s[4])) or \
    (s[5] != s[4] and (s[5] == s[0] or s[5] == s[2])):
        return False
    else:
        return True
    '''
        (s[0] != 'W' and (s[2] == 'W' or s[4] == 'W')) or \
        (s[1] != 'W' and (s[3] == 'W' or s[5] == 'W')) or \
        (s[2] != 'W' and s[4] == 'W') or \
        (s[3] != 'W' and s[5] == 'W'):
        '''





def classifyManPos(S):
    setEast = []
    setWest = []
    for n in S:
        if n[6] == "E":
            setEast.append(n)
        else:
            setWest.append(n)

    return setEast, setWest

def getPos(astate):
    east = 0
    west = 0
    for i in range(len(astate)-1):
        if astate[i] is 'E':
            east += 1
        else:
            west += 1
    return east, west

def neighborNode(n1, n2):
    if n1[6] == n2[6]:
        return False
    else:
        diff = 0
        for index in range(0,len(n1)-1):
            if n1[index] != n2[index]:
                    diff = diff + 1

        if diff <= 2 and diff > 0:
            a, b = getPos(n1)
            c, d = getPos(n2)
            if n1[6] == 'E':
                if (a - c >= 1 and a - c <= 2):
                    return True
            else:
                if (b - d >=1 and b - d <= 2):
                    return True


        else:
            return False

def nextStates(aState, allStates):
    neighborStates = []


    setManEast, setManWest = classifyManPos(allStates)


    if aState[6] == "E":
        setCandidates = setManWest
    else:
        setCandidates = setManEast


    for m in setCandidates:

        if neighborNode(aState, m) == True:
            neighborStates.append(m)

    return neighborStates

def genGraph(S):


    setLegalStates = []

    graph = {}


    for n in range(len(S)):
        if isAStateLegal(S[n]) == True:  # check whether a node (state) is legal
            setLegalStates.append(S[n])  # If legal, add n to the set of all legal states

    # For each legal state n,
    #   First: find the set of other legal nodes that n can connect to
    #   Second: add n and the links to other legal nodes to the graph
    for n in range(len(setLegalStates)):
        setNextNodes = nextStates(setLegalStates[n], setLegalStates)
        graph.update({setLegalStates[n]: setNextNodes})

    return graph


def findShortestPath(graph, start, end, path=[]):

    path = path + [start]         #加一步
    if start == end:            #没到尽头
        return path
    if not (start in graph):
        return None
    shortestPath = []
    for node in graph[start]:   #下一步可以走的有
        if node not in path:    #没重复
            newpath = findShortestPath(graph, node, end, path)
            if newpath:
                if not shortestPath or len(newpath) < len(shortestPath):
                    shortestPath = newpath + shortestPath

    return shortestPath

def find_all_paths(graph, start, end, path=[]):
    '查找所有的路径'
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

def solver():

    setAllStates = genStates()
    G = genGraph(setAllStates)
    for i in G :
        print(i,G[i])
    print()
    src = "EEEEEEE"  # The beginning state where all four objects are on the east side
    des = "WWWWWWW"  # The terminating state when the problem is solved
    list = []
    step = set()
    path = find_all_paths(G, src, des)  # Generate the path by finding a shortest path from
    for i in path:
        if len(i) == 12:
            list.append(i)
    for i in list:
        for j in i:
            step.add(j)
    print(step)
    print(len(step))




solver()