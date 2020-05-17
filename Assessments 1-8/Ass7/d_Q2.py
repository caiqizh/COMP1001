

def getRandomLinks(graph,n,i,m):
    T = all(n)
    k = T[i]
    T.remove(k)
    for j in range(len(graph)):
        if graph[j] == k:
            T.remove(j)
    list = random.sample(T, m)
    return list

#这个地方需要测试，因为我们要确定他是单向的

import random

def all(n):
    list = []
    for i in range(n):
        list.append(i)
    return list

def genRandomDirectedGraph(n, m):
    graph = {}
    S = all(n)
    for i in range(len(S)):
        set = getRandomLinks(graph,n, i, m)
        graph.update({S[i]: set})

    return graph


def findShortestPath(graph, start, end, path=[]):
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
randomGraph = genRandomDirectedGraph(15,2)

print("The graph is:")
print(randomGraph)
print()
print("The shortest paths are:")
for node in range(1,15):
    print(findShortestPath(randomGraph, node, 0, path=[]))

print()
randomGraph = genRandomDirectedGraph(25,2)
print("The graph is:")
print(randomGraph)
print()
print("The shortest paths are:")
for node in range(1,25):
    print(findShortestPath(randomGraph, node, 0, path=[]))


print()
randomGraph = genRandomDirectedGraph(50,2)
print("The graph is:")
print(randomGraph)
print()
print("The shortest paths are:")
for node in range(1,50):
    print(findShortestPath(randomGraph, node, 0, path=[]))

