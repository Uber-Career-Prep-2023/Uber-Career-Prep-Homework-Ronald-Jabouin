# Given a binary matrix in which 1s represent land and 0s represent water. 
# Return the number of islands (contiguous 1s surrounded by 0s or the edge of the matrix).

# Time: 
# Implementation: BFS
    # Find a 1, then keep checking it's neighbors till theres no more 1's. This represents an islands.
    # Check every node

# Time Complexity: O (|vertices| + |edges|) since im doing a bfs on a graph
# Space Complexity: O(|v| + |e|)
from collections import deque


def numberOfIslands(matrix: list[list[str]]):

    # Making sure a matrix was inputted
    if not matrix:
        return 0
    
    # Getting dimensions of grid
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    islands = 0

    def bfs(row, col):
        queue = deque()
        visited.add((row,col))
        queue.append((row,col))

        while queue:
             row,col = queue.popleft()
            #  right, left, up, down
             directions = [[1,0], [-1,0], [0,1], [0,-1]]

             for dirRow, dirCol in directions:
                #   Check if the node I'm moving to is in range, is a 1, and is not in visited already
                  if (row + dirRow) in range(rows) and (col + dirCol) in range(cols) and matrix[row + dirRow][col + dirCol] == 1 and (row+dirRow, col+dirCol) not in visited:
                       queue.append((row+dirRow, col+dirCol))
                       visited.add((row+dirRow, col+dirCol))

    for row in range(rows):
        for col in range(cols):
               if matrix[row][col] == 1 and (row,col) not in visited:
                    bfs(row,col)
                    islands += 1 
    
    return islands

if __name__ == "__main__" :
    print(numberOfIslands([[1,0,1,1,1],
                           [1,1,0,1,1],
                           [0,1,0,0,0],
                           [0,0,0,1,0],
                           [0,0,0,0,0]]
                    ))
    
    
    print(numberOfIslands([[1,0,0],
                     [0,0,0]]
                    ))