from collections import defaultdict
class Graph:

    def __init__(self, temp):
        self.count = 0

    def isPallindrome(self, arr):
        str = ''.join(arr)
        return str == str[::-1]

    def transverseAllPossiblePaths_pallindrom(self, TB, Si, Sj , Di, Dj, N, visited, path):
        if Si == Di and Sj == Dj:
            path.append(TB[Si][Sj])
            if self.isPallindrome(path):
                self.count += 1
        elif Si < 0 or Sj < 0 or Si >= N or Sj >= N or visited[Si][Sj]:
            return
        else:
            visited[Si][Sj] = True
            path.append(TB[Si][Sj])
            self.transverseAllPossiblePaths_pallindrom(TB, Si + 1, Sj, Di, Dj, N, visited, path); # go right
            self.transverseAllPossiblePaths_pallindrom(TB, Si - 1, Sj, Di, Dj, N, visited, path); # go left
            self.transverseAllPossiblePaths_pallindrom(TB, Si, Sj + 1, Di, Dj, N, visited, path); # go down
            self.transverseAllPossiblePaths_pallindrom(TB, Si, Sj - 1, Di, Dj, N, visited, path); # go up
            self.transverseAllPossiblePaths_pallindrom(TB, Si + 1, Sj + 1, Di, Dj, N, visited, path);  # go up
            self.transverseAllPossiblePaths_pallindrom(TB, Si - 1, Sj - 1, Di, Dj, N, visited, path);  # go up

        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[Si][Sj] = False

    # Prints all paths from 's' to 'd'
    def transverseAllPossiblePaths(self,TB, Si, Sj , Di, Dj, N):

        # Mark all the vertices as not visited
        visited = [[False for x in range(N)] for y in range(N)]

        # Create an array to store paths
        path = []

        # Call the recursive helper function to print all paths
        self.transverseAllPossiblePaths_pallindrom(TB, Si, Sj, Di, Dj, N, visited, path)



N = 4
g = Graph(0)
TB = [
    ['Z', 'B', 'C', 'G'],
    ['B', 'Y', 'Z', 'Y'],
    ['C', 'D', 'Y', 'B'],
    ['W', 'C', 'B', 'Z'],
]


Si = 0
Sj = 0
Di = 1
Dj = 2


g.transverseAllPossiblePaths(TB, Si, Sj, Di, Dj, N)
print(g.count)