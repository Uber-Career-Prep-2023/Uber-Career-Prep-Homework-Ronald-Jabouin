"""
Given an origin and a destination in a directed graph in which edges can be blue or red, 
determine the length of the shortest path from the origin to the destination in which the edges 
traversed alternate in color. Return -1 if no such path exists.

"""

from collections import deque, defaultdict
def alternatingPath(edges, origin, destination):
    graph = {}

    for org, dest, color in edges:

        if org not in graph:
            graph[org] = []
        graph[org].append((dest, color))

    queue = deque([(origin, 0, None)])  
    visited = set()

    while queue:
        
        node, length, last_color = queue.popleft()

        if node == destination:
            return length

        if node not in graph:
            continue

        for neighbor, color in graph[node]:
            if last_color is None or color != last_color:
                queue.append((neighbor, length + 1, color))

        visited.add(node)

    return -1


if __name__ == "__main__":
    edges = [("A", "B", "blue"), ("A", "C", "red"), ("B", "D", "blue"), ("B", "E", "blue"), ("C", "B", "red"), ("D", "C", "blue"), ("A", "D", "red"), ("D", "E", "red"), ("E", "C", "red")]
    input = "A"
    dest = "E"
    # Output: 4 (path: A→D (red), D→C (blue), C→B (red), B→E (blue))
    print(alternatingPath(edges,input,dest))
    input = "E"
    dest = "D"
    # Output: -1 (only path is: E→C (red), C→B (red), B→D (blue))
    print(alternatingPath(edges,input,dest))

