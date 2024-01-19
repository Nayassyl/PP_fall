import matplotlib.pyplot as plt
import math
from collections import deque

class GraphOperations:
    def __init__(self):
        self.vertices = {}
        self.edges = []
        self.adjacency_list = {}
    
    def add_vertex(self, v):
        self.vertices[v] = None
        self.adjacency_list[v] = []
    
    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.edges.append((u, v))
            self.adjacency_list[u].append(v)
            self.adjacency_list[v].append(u)  # Assuming an undirected graph
    
    def draw_graph(self):
        """
        Draw a graphical representation of the graph with vertices forming a polygon.
        """
        num_vertices = len(self.vertices)
        if num_vertices == 0:
            return

        G = plt.figure()
        ax = G.add_subplot(111)

        polygon_radius = 2.0  # Adjust the radius of the polygon
        angle_step = 2 * math.pi / num_vertices

        # Calculate vertex positions and store them in self.vertices
        for i, vertex in enumerate(self.vertices.keys()):
            angle = i * angle_step
            x = polygon_radius * math.cos(angle)
            y = polygon_radius * math.sin(angle)
            self.vertices[vertex] = (x, y)

        # Draw edges
        for u, v in self.edges:
            x1, y1 = self.vertices[u]
            x2, y2 = self.vertices[v]
            ax.plot([x1, x2], [y1, y2], 'k-')

        # Draw vertices
        for vertex, (x, y) in self.vertices.items():
            ax.add_patch(plt.Circle((x, y), 0.2, color='skyblue', zorder=2))
            ax.text(x, y, str(vertex), ha='center', va='center', fontsize=12, zorder=3, color='black')

        ax.set_aspect('equal', adjustable='datalim')
        ax.set_axis_off()
        plt.show()

    def is_hamilton_cycle(self):
        """
        Check if the graph contains a Hamiltonian cycle.
        """
        def visit(vertex, visited, path):
            visited.add(vertex)
            path.append(vertex)
            if len(path) == len(self.vertices):
                # Check if it forms a cycle back to the starting vertex
                if path[0] in self.adjacency_list[vertex]:
                    return True
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    if visit(neighbor, visited, path):
                        return True
            visited.remove(vertex)
            path.pop()
            return False

        for start_vertex in self.vertices:
            if visit(start_vertex, set(), []):
                return True
        return False

    def is_hamilton_path(self):
        """
        Check if the graph contains a Hamiltonian path and return the path if it exists.
        """
        def visit(vertex, visited, path):
            visited.add(vertex)
            path.append(vertex)
            if len(path) == len(self.vertices):
                return True, path  # Return the path as well
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    result, found_path = visit(neighbor, visited, path)
                    if result:
                        return True, found_path
            visited.remove(vertex)
            path.pop()
            return False, []

        for start_vertex in self.vertices:
            result, path = visit(start_vertex, set(), [])
            if result:
                return True, path
        return False, []

    def find_shortest_path(self, start, end):
        """
        Find the shortest path between two vertices using BFS.
        """
        queue = deque([(start, [start])])
        visited = set()
        while queue:
            current_vertex, path = queue.popleft()
            if current_vertex == end:
                return path
            visited.add(current_vertex)
            for neighbor in self.adjacency_list[current_vertex]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
        return None
    
    def find_euler_path(self):
        """
        Find an Euler path or circuit in the graph.
        """
        # Check if the graph has 0 or 2 vertices with odd degree
        odd_degree_vertices = [v for v in self.vertices if len(self.adjacency_list[v]) % 2 != 0]
        if len(odd_degree_vertices) not in [0, 2]:
            return None  # No Euler path or circuit exists

        # Make a copy of the adjacency list to modify it while finding the path
        graph = {v: self.adjacency_list[v][:] for v in self.vertices}

        def find_path(start_vertex):
            path = []
            stack = [start_vertex]
            while stack:
                vertex = stack[-1]
                if graph[vertex]:
                    next_vertex = graph[vertex].pop()
                    graph[next_vertex].remove(vertex)
                    stack.append(next_vertex)
                else:
                    path.append(stack.pop())
            return path[::-1]

        # Start from a vertex with odd degree if any, otherwise from any vertex
        start_vertex = odd_degree_vertices[0] if odd_degree_vertices else next(iter(self.vertices))
        path = find_path(start_vertex)

        if any(graph.values()):  # Check if all edges are used
            return None

        return path

    def find_euler_circuit(self):
        """
        Find an Euler circuit in the graph.
        """
        path = self.find_euler_path()
        if path and path[0] == path[-1]:
            return path
        return None


# Example usage:
if __name__ == "__main__":
    graph = GraphOperations()
    
    # [Set up your graph with vertices and edges as before]
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)

    # Adding edges to the graph
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 1)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(4, 5)
    graph.add_edge(3, 5)
    
    graph.draw_graph()
    print("Hamiltonian Cycle Exists:", graph.is_hamilton_cycle())
    exists, path = graph.is_hamilton_path()
    if exists:
        print("Hamiltonian Path Exists:", path)
    else:
        print("No Hamiltonian Path exists.")
    print("Shortest Path from Vertex 1 to 5:", graph.find_shortest_path(1, 5))

    euler_path = graph.find_euler_path()
    if euler_path:
        print("Euler Path:", euler_path)
    else:
        print("No Euler Path exists.")

    euler_circuit = graph.find_euler_circuit()
    if euler_circuit:
        print("Euler Circuit:", euler_circuit)
    else:
        print("No Euler Circuit exists.")