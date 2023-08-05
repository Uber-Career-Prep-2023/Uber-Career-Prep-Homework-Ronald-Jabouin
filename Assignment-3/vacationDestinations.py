"""
Given an origin city, a maximum travel time k, and pairs of destinations that can be reached 
directly from each other with corresponding travel times in hours, 
return the number of destinations within k hours of the origin. 
Assume that having a stopover in a city adds an hour of travel time.


"""
from collections import deque

def vacationDestination(origin, k, destinations):

    connections = {}
    result = []

    for start,end,dist in destinations: 
        if start not in connections:
            connections[start] = [(end,dist)]
        else:
            connections[start].append((end,dist))
    queue = deque([(origin, 0)])
    visited = set([origin])
    count = 0

    while queue:
        city, time = queue.popleft()

        if time > k:
            break

        if time <= k:
            result.append(city)
        
        for neighbor, travel_time in connections[city]:
            stop_over = time + travel_time + 1
            if stop_over <= k and neighbor not in visited:
                queue.append((neighbor, stop_over))
                visited.add(neighbor)
    
    return result



if __name__ == "__main__":
    destinations = [("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)]

# Origin = "New York", k=5
# Output: 2 (["Boston", "Philadelphia"])

# Origin = "New York", k=7
# Output: 2 (["Boston", "Philadelphia", "Washington, D.C", "Newport"])

# Origin = "New York", k=8
# Output: 2 (["Boston", "Philadelphia", "Washington, D.C", "Newport", "Harper's Ferry", "Portland"])
    print(vacationDestination("New York", 5, destinations))
    print(vacationDestination("New York", 7, destinations))
    print(vacationDestination("New York", 8, destinations))
