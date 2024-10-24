class Digraph:
    def __init__(self, routes) -> None:
        self.digraph = {}
        for start, end in routes:
            self.add_edge(start, end)

    def add_vertex(self, vertex):
        if vertex not in self.digraph:
            self.digraph[vertex] = []
            return True
        else:
            return False

    def add_edge(self, vertex, edge):
        if vertex in self.digraph:
            self.digraph[vertex].append(edge)
        else:
            self.digraph[vertex] = [edge]
        return True

    def remove_vertex(self, vertex):
        if vertex in self.digraph:
            for v in self.digraph:
                if vertex in self.digraph[v]:
                    self.digraph[v].remove(vertex)
            del self.digraph[vertex]

    def remove_edge(self, vertex, edge):
        if vertex in self.digraph and edge in self.digraph[vertex]:
            self.digraph[vertex].remove(edge)

    def bfs(self, start):
        visited = set()
        queue = [start]
        while queue:
            curr = queue.pop(0)
            if curr not in visited:
                visited.add(curr)
                print(curr, end=" ")
                queue.extend(self.digraph.get(curr, []))
        return visited

    def dfs(self, start):
        stack = [start]
        visited = set()
        while stack:
            curr = stack.pop()
            if curr not in visited:
                visited.add(curr)
                print(curr, end=" ")
                stack.extend(self.digraph.get(curr, []))

    def find_path(self, start, end, path=None):
        if start not in self.digraph:
            return []
        if path is None:
            path = []
        if start == end:
            return [path + [end]]
        path = path + [start]
        paths = []
        for p in self.digraph.get(start, []):
            if p not in path:
                sp = self.find_path(p, end, path)
                paths.extend(sp)
        return paths

    def shortest_path(self, start, end, path=None):
        if start not in self.digraph:
            return []
        if path is None:
            path = []
        if start == end:
            return [path + [end]]
        path = path + [start]
        shortest_path = None
        for p in self.digraph[start]:
            if p not in path:
                sp = self.shortest_path(p, end, path)
                if shortest_path is None or len(shortest_path) > len(sp):
                    shortest_path = sp
        return shortest_path


routes = [
    ('a', 'b'),
    ('a', 'c'),
    ('b', 'c'),
    ('b', 'd'),
    ('c', 'a'),
    ('c', 'b'),
    ('d', 'b'),
    ('d', 'c'),
    ('e', 'f'),
    ('f', 'a')
]
graph = Digraph(routes)
graph.add_edge('i', 'k')
graph.add_vertex('v')
graph.add_edge('a', 'v')
# graph.remove_vertex('b')
graph.remove_edge('a', 'v')
print("BFS\n")
graph.bfs('a')
print("\n")
print("DFS\n")
graph.dfs('a')
print(graph.find_path('a', 'd'))
print(graph.shortest_path('a', 'd'))
