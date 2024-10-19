class Digraph:
    def __init__(self, edges=None) -> None:
        self.dict = {}
        if edges:
            for start, end in edges:
                self.add_edge(start, end)

    def add_edge(self, vertex, edge):
        if vertex in self.dict:
            self.dict[vertex].append(edge)
        else:
            self.dict[vertex] = [edge]

    def add_vertex(self, vertex):
        if vertex not in self.dict:
            self.dict[vertex] = []
            print(f"Vertex {vertex} is added")
        else:
            print(f"Vertex {vertex} already exists")

    def remove_vertex(self, vertex):
        if vertex in self.dict:
            for v in self.dict:
                if vertex in self.dict[v]:
                    self.dict[v].remove(vertex)  # FIXED HERE
            del self.dict[vertex]

    def remove_edge(self, vertex, edge):
        if vertex in self.dict and edge in self.dict[vertex]:
            self.dict[vertex].remove(edge)

    def find_paths(self, start, end, path=None):
        if path is None:
            path = []
        if start == end:
            return [path + [end]]
        if start not in self.dict:
            return []
        path = path + [start]
        paths = []
        for node in self.dict[start]:
            if node not in path:
                sp = self.find_paths(node, end, path)
                paths.extend(sp)
        return paths

    def shortest_path(self, start, end, path=None):
        if path is None:
            path = []
        if start == end:
            return path + [end]
        if start not in self.dict:
            return None
        path = path + [start]
        shortest_path = None
        for node in self.dict[start]:
            if node not in path:
                sp = self.shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path

    def bfs(self, start):
        visited = set()
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(node)
                visited.add(node)
                queue.extend(self.dict.get(node, []))
        return visited

    def dfs(self, start):
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                print(node)
                stack.extend(self.dict.get(node, []))
        return visited

    def __str__(self) -> str:
        return str(self.dict)


if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route_graph = Digraph(routes)

    # Test adding and removing vertices/edges
    route_graph.add_vertex("Berlin")
    route_graph.add_edge("Berlin", "New York")
    route_graph.remove_edge("Paris", "Dubai")

    print(route_graph)
    
    start, end = "Mumbai", "New York"
    print(f"All paths between {start} and {end}: {route_graph.find_paths(start, end)}")
    print(f"Shortest path between {start} and {end}: {route_graph.shortest_path(start, end)}")
    
    print("BFS from Mumbai:")
    route_graph.bfs("Mumbai")
    
    print("\nDFS from Mumbai:")
    route_graph.dfs("Mumbai")

