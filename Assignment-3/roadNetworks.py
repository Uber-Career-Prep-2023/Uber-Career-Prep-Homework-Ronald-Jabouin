
"""
In some states, it is not possible to drive between any two towns because they are not connected to the same road network. 
Given a list of towns and a list of pairs representing roads between towns, return the number of road networks. 
(For example, a state in which all towns are connected by roads has 1 road network, and a state in which none of the towns
 are connected by roads has 0 road networks.)
"""

# Implementation: create adjancey list of data then perform dfs.
from collections import deque


def roadNetworks(towns,connections):

    mapOfConnections = {}
    result = 0


    # # # Creating adjancency list
    for connection in connections:
        loc1,loc2 = connection[0],connection[1]
    # #     # Roads are two ways so have to add connection for location 1 and 2
        if loc1 not in mapOfConnections:
            mapOfConnections[loc1] = []
        if loc2 not in mapOfConnections:
            mapOfConnections[loc2] = []
        mapOfConnections[loc1].append(loc2)
        mapOfConnections[loc2].append(loc1)


    
    # dfs through road networks
    visited = set()

    def dfs(town):
        visited.add(town)
        for neighbor in mapOfConnections[town]:
            if neighbor not in visited:
                dfs(neighbor)
    
    for town in towns: 
        if town not in visited and len(mapOfConnections.get(town,[])) != 0:
            dfs(town)
            result += 1

    return result
        

if __name__ == "__main__":
    # should be 2
    towns = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy"]
    connections = [("Anchorage", "Homer"), 
 ("Glacier Bay", "Gustavus"),
 ("Copper Center", "McCarthy"), 
 ("Anchorage", "Copper Center"), 
 ("Copper Center", "Fairbanks"),
   ("Healy", "Fairbanks"), 
   ("Healy", "Anchorage")]

    print(roadNetworks(towns, connections))


    # should be 2
    towns = ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"]
    connections = [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")]
    print(roadNetworks(towns, connections))


