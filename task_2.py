visited = []

class Graph: 
    def __init__(self, dicts):
        self.graph = dicts

    def add_v(self, v):
        if v not in self.graph:
            self.graph[v] = []
        else:
            print("vertex already exists")

    def add_e(self, e):
        if len(e) != 2:
            print("Edge must connect exactly two vertices")
            return
        
        v1, v2 = tuple(e)
        if v1 in self.graph and v2 in self.graph:
            if v2 not in self.graph[v1]:  # Unikaj duplikatów
                self.graph[v1].append(v2)
            if v1 not in self.graph[v2]:  # Dodaj krawędź w obu kierunkach
                self.graph[v2].append(v1)
        else:
            print("One or both vertices do not exist. Edge cannot be added.")

    def all_edges(self, v):
        return self.graph[v]
        
    def all_vertices(self):
        return set(self.graph.keys())

    def remove_v(self, v):
        if v  in self.graph:
            self.graph.pop(v)
            for v2 in self.graph:
                if v in self.graph[v2]:
                    self.graph[v2].remove(v)
        else:
            print("Vertex does not exist")

    def remove_e(self, e):
        if len(e) != 2:
            print("Edge must connect exactly two vertices")
            return

        v1, v2 = tuple(e)
        if v1 in self.graph and v2 in self.graph:
            if v2 in self.graph[v1]:  # Sprawdzenie istnienia krawędzi przed usunięciem
                self.graph[v1].remove(v2)
            if v1 in self.graph[v2]:  # Usuwanie w obu kierunkach (dla grafu nieskierowanego)
                self.graph[v2].remove(v1)
        else:
            print("One or both vertices do not exist. Edge cannot be removed.")

    def __iter__(self, list0):
        self.list0 = iter(list0)
        return self.list0
    
    def __next__(self):
        return next(self.list0)

    def DFS(self, v, visited=None):
        visited = []
        if v not in visited:
            visited.append(v)
            for v2 in self.graph[v]:
                self.DFS(v2, visited)
        return self.__iter__(visited)

    def BFS(self, v):
        visited = []  
        queue = [v]  
        result = []   
        
        visited.append(v)
        
        while queue:
            current = queue.pop(0)  
            result.append(current)  
            
            # process the neighbors
            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.append(neighbor)
        
        return iter(result) 

    def find_all_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph:
            return []
        paths = []
        for vertex in self.graph[start]:
            if vertex not in path:
                new_paths = self.find_all_paths(vertex, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def shortest_path(self, start, end):
        visited = {start}
        queue = [(start, [start])]
        while queue:
            current, path = queue.pop(0)
            if current == end:
                return path
            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None
 
    def is_connected(self):
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        dfs(next(iter(self.graph)))  # Start from any vertex
        return len(visited) == len(self.graph)

dic = {"45": ["Anna", "1a"], "Anna": ["45"], "1a": ["45"]}
graph = Graph(dic)
print(graph.graph)
graph.add_v(2)
print(graph.graph)
graph.add_e(("45",2))
print(graph.graph)
graph.remove_e(("45",2))
print(graph.graph)
print(graph.edges("45"))
print(graph.all_vertices())
per = graph.DFS("45")
try:
    while per :
        print(next(per))
except StopIteration:
    pass
iterator = graph.BFS("45")
try:
    while iterator :
        print(next(iterator))
except StopIteration:
    pass
