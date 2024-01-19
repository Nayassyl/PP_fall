import math
from collections import deque

import tkinter as tk
from tkinter import messagebox

class GraphGUI:
    def __init__(self, graph_ops):
        self.graph_ops = graph_ops
        self.window = tk.Tk()
        self.window.title("Graph Operations GUI")

        # Canvas for drawing the graph
        self.canvas = tk.Canvas(self.window, width=600, height=600, bg='white')
        self.canvas.pack()

        #Entries for finding shortest path
        self.start_vertex_entry = tk.Entry(self.window)
        self.start_vertex_entry.pack(side=tk.LEFT)
        self.end_vertex_entry = tk.Entry(self.window)
        self.end_vertex_entry.pack(side=tk.LEFT)

        # Buttons for different operations
        tk.Button(self.window, text='Draw Graph', command=self.draw_graph).pack(side=tk.LEFT)
        tk.Button(self.window, text='Find Shortest Path', command=self.find_shortest_path).pack(side=tk.LEFT)
        tk.Button(self.window, text='Hamiltonian Cycle', command=self.check_hamiltonian_cycle).pack(side=tk.LEFT)
        tk.Button(self.window, text='Hamiltonian Path', command=self.check_hamiltonian_path).pack(side=tk.LEFT)
        tk.Button(self.window, text='Euler Path', command=self.check_euler_path).pack(side=tk.LEFT)
        tk.Button(self.window, text='Euler Circuit', command=self.check_euler_circuit).pack(side=tk.LEFT)
        tk.Button(self.window, text='Find Hamiltonian Path', command=self.find_hamiltonian_path).pack(side=tk.LEFT)

    def draw_graph(self):
        self.canvas.delete("all")  # Clear the canvas
        self.graph_ops.draw_graph(canvas=self.canvas)  # Pass the canvas to the graph drawing function

    def find_shortest_path(self):
        # Get the start and end vertices from the entries
        start = self.start_vertex_entry.get()
        end = self.end_vertex_entry.get()
        if start.isdigit() and end.isdigit():
            start, end = int(start), int(end)
            path = self.graph_ops.find_shortest_path(start, end)
            if path:
                self.draw_graph()  # Redraw the graph
                self.highlight_path(path)  # Highlight the shortest path
                messagebox.showinfo("Shortest Path", f"The shortest path is: {path}")
            else:
                messagebox.showinfo("Shortest Path", "No path exists between the specified vertices.")
        else:
            messagebox.showinfo("Invalid Input", "Please enter valid vertex numbers.")
    
    def find_hamiltonian_path(self):
        exists, path = self.graph_ops.is_hamilton_path()
        if exists:
            self.draw_graph()  # Redraw the graph
            self.highlight_path(path, color='green')  # Highlight the Hamiltonian path
            messagebox.showinfo("Hamiltonian Path", f"Hamiltonian Path exists: {path}")
        else:
            messagebox.showinfo("Hamiltonian Path", "No Hamiltonian Path exists.")
    
    def highlight_path(self, path, color='red'):
        # Highlight the path on the canvas
        for i in range(len(path) - 1):
            x1, y1 = self.graph_ops.vertices[path[i]]
            x2, y2 = self.graph_ops.vertices[path[i + 1]]
            self.canvas.create_line(x1, y1, x2, y2, fill=color, width=2)
            self.canvas.create_oval(x1 - 10, y1 - 10, x1 + 10, y1 + 10, fill=color)
            self.canvas.create_oval(x2 - 10, y2 - 10, x2 + 10, y2 + 10, fill=color)

    def check_hamiltonian_cycle(self):
        exists = self.graph_ops.is_hamilton_cycle()
        message = "Hamiltonian Cycle Exists" if exists else "No Hamiltonian Cycle exists"
        messagebox.showinfo("Result", message)

    def check_hamiltonian_path(self):
        exists, path = self.graph_ops.is_hamilton_path()
        message = f"Hamiltonian Path Exists: {path}" if exists else "No Hamiltonian Path exists"
        messagebox.showinfo("Result", message)

    def check_euler_path(self):
        path = self.graph_ops.find_euler_path()
        message = f"Euler Path: {path}" if path else "No Euler Path exists"
        messagebox.showinfo("Result", message)

    def check_euler_circuit(self):
        circuit = self.graph_ops.find_euler_circuit()
        message = f"Euler Circuit: {circuit}" if circuit else "No Euler Circuit exists"
        messagebox.showinfo("Result", message)

    def run(self):
        self.window.mainloop()

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
    
    def draw_graph(self, canvas):
        # Draw a graphical representation of the graph with vertices forming a polygon on a Tkinter canvas.
        canvas_width = int(canvas['width'])
        canvas_height = int(canvas['height'])
        num_vertices = len(self.vertices)
        if num_vertices == 0:
            return

        # Calculate the center of the canvas
        center_x = canvas_width / 2
        center_y = canvas_height / 2
        polygon_radius = min(canvas_width, canvas_height) / 2.5  # Adjust the radius of the polygon

        # Calculate vertex positions and store them in self.vertices
        angle_step = 2 * math.pi / num_vertices
        for i, vertex in enumerate(self.vertices.keys()):
            angle = i * angle_step
            x = center_x + polygon_radius * math.cos(angle)
            y = center_y + polygon_radius * math.sin(angle)
            self.vertices[vertex] = (x, y)

        # Draw edges
        for u, v in self.edges:
            x1, y1 = self.vertices[u]
            x2, y2 = self.vertices[v]
            canvas.create_line(x1, y1, x2, y2, fill='black')

        # Draw vertices
        vertex_radius = 10  # Adjust size as needed
        for vertex, (x, y) in self.vertices.items():
            canvas.create_oval(x - vertex_radius, y - vertex_radius, x + vertex_radius, y + vertex_radius, fill='skyblue')
            canvas.create_text(x, y, text=str(vertex), font=('Arial', 12), fill='black')

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
        # Check if the graph contains a Hamiltonian path and return the path if it exists.
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
        # Find the shortest path between two vertices using BFS.
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
        # Find an Euler path or circuit in the graph.
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
        # Find an Euler circuit in the graph.
        path = self.find_euler_path()
        if path and path[0] == path[-1]:
            return path
        return None


# Example usage:
if __name__ == "__main__":
    graph = GraphOperations()
    
    #Here you should input cases from test.py, default case is given below.
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_vertex(8)
    graph.add_vertex(9)
    graph.add_vertex(10)


    graph.add_edge(1, 2)
    graph.add_edge(1, 7)
    graph.add_edge(1, 5)
    graph.add_edge(2, 4)
    graph.add_edge(2, 6)
    graph.add_edge(2, 9)
    graph.add_edge(2, 10)
    graph.add_edge(3, 4)
    graph.add_edge(3, 7)
    graph.add_edge(3, 10)
    graph.add_edge(4, 6)
    graph.add_edge(4, 9)
    graph.add_edge(5, 7)
    graph.add_edge(5, 8)
    graph.add_edge(5, 10)
    graph.add_edge(5, 9)
    graph.add_edge(6, 7)
    graph.add_edge(6, 9)
    graph.add_edge(7, 9)
    graph.add_edge(7, 10)
    graph.add_edge(8, 10)

    
    app = GraphGUI(graph)
    app.run()