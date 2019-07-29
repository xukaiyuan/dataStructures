#!/usr/bin/python3

def init(graph, source):
    # initiate the distance dictionary and the previous node dictionary
    max = float("inf")
    dist = {}
    previous = {}

    for v in graph:
        dist[v] = max
        previous[v] = None
    dist[source] = 0

    return dist, previous

def bellmanFord(graph, source):
    # graph should be structured as {A: {B: 1}}
    # which means A -> B and the distance is 1

    dist, previous = init(graph, source)

    # do (number of node) - 1 times iteration
    for i in range(len(graph) - 1):
        for u in graph:
            for v in graph[u]:
                if(dist[v] > dist[u] + graph[u][v]):
                    dist[v] = dist[u] + graph[u][v]
                    previous[v] = u

    # check if there is a loop
    for u in graph:
        for v in graph[u]:
            if(dist[v] > dist[u] + graph[u][v]):
                return None, None

    return dist, previous

def showRoute(graph, source, destination):
    _, previous = bellmanFord(graph, source)
    #print(previous)
    if(source == destination):
        return [source]
    route = [destination]

    while(previous[destination] != None):
        route.append(previous[destination])
        destination = previous[destination]

    route.reverse()
    return route

def showForwardingTable(graph):
    forwardingTable = []
    forwardingDist = []

    for source in graph:
        dist, _ = bellmanFord(graph, source)
        forwardingDist.append(dist)

        currentRoute = []
        for destination in graph:
            route = showRoute(graph, source, destination)
            currentRoute.append(route)
        forwardingTable.append(currentRoute)

    return forwardingDist, forwardingTable


# test
graph = {
        'a': {'b': -1, 'c':  4},
        'b': {'c':  2, 'd':  3, 'e':  2},
        'c': {},
        'd': {'b':  3, 'c':  5},
        'e': {'d': -3}
    }

forwardingDist, forwardingTable = showForwardingTable(graph)
print(forwardingDist)
print
print(forwardingTable)
