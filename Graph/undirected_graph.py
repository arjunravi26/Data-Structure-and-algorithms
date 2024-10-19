class UiGraph:
    def __init__(self, edges=None) -> None:
        self.graph_dict = {}
        if edges:
            for start, end in edges:
                self.add_edge(start, end)

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, v, e):
        if v not in self.graph_dict:
            self.add_vertex(v)
        if e not in self.graph_dict:
            self.add_vertex(e)
        self.graph_dict[v].append(e)
        self.graph_dict[e].append(v)

    def remove_vertex(self, v):
        if v in self.graph_dict:
            for e in self.graph_dict[v]:
                self.graph_dict[e].remove(v)
            del self.graph_dict[v]

    def remove_edge(self, v, e):
        if v in self.graph_dict and e in self.graph_dict[v]:
            self.graph_dict[v].remove(e)
            self.graph_dict[e].remove(v)

    def get_neighbours(self, v):
        return self.graph_dict[v] if v in self.graph_dict else []

    def has_edge(self, v, e):
        return v in self.graph_dict and e in self.graph_dict[v]

    def find_paths(self, start, end, path=None):
        if path is None:
            path = []
        if start == end:
            return [path + [end]]
        if start not in self.graph_dict:
            return []
        path = path + [start]
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.find_paths(node, end, path)
                paths.extend(sp)
        return paths

    def shortest_path(self, start, end, path=None):
        if path is None:
            path = []
        if start == end:
            return path + [end]
        if start not in self.graph_dict:
            return []
        path = path + [start]
        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path if shortest_path else []

    def bfs(self, start):
        visited = set()
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                print(node)
                queue.extend(self.graph_dict.get(node, []))
        return visited

    def dfs(self, start):
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                print(node)
                stack.extend(self.graph_dict.get(node, []))
        return visited

    def __str__(self) -> str:
        return str(self.graph_dict)


if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route_graph = UiGraph(routes)

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
