"""
Given an array of pairs of values representing edges in an unweighted graph, 
create the equivalent adjacency list/set representation 
(a map from element to a list or set of elements). 
Pairs represent directed edges: (A, B) means there is an edge from A to B. 
If the pair (B, A) is also provided then there is an undirected edge between A and B. 
For simplicity, you may assume that each node of the graph stores an integer 
rather than a generic data type and that the elements are distinct. 
Implement a basic DFS and BFS searching for a target value and a 
topological sort (using either DFS or Kahn’s algorithm).

"""

# TODO: 0 is at the end and the process for checking for 0 is a bit inefficient
def adjacencyList(data: list):
    result = {}
    seenNumbers = set()

    for tupleData in data:

        for item in tupleData:
            if item not in seenNumbers:
                seenNumbers.add(item)


        if tupleData[0] in result:
            result[tupleData[0]].append(tupleData[1])
        else:
            result[tupleData[0]] = [tupleData[1]]
        

        for number in seenNumbers:
            if number not in result:
                result[number] = []

    print(result)
    return result


if __name__ == "__main__" :
    adjacencyList([(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)])


def bfs(target: int, graph: dict):
    # study bfs solution
    #  bfs solution for this problem
    pass


def dfs(target: int, graph: dict):
    pass