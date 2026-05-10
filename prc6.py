# Graph Coloring Problem using Backtracking
# Constraint Satisfaction Problem (CSP)

# Function to check whether current color assignment is safe
def is_safe(node, graph, colors, color, n):

    # Check adjacent vertices
    for k in range(n):

        # If connected and same color exists
        if graph[node][k] == 1 and colors[k] == color:
            return False

    return True


# Backtracking Function
def graph_coloring(graph, m, colors, node, n):

    # If all vertices are colored
    if node == n:
        return True

    # Try all colors one by one
    for color in range(1, m + 1):

        # Check if color can be assigned
        if is_safe(node, graph, colors, color, n):

            # Assign color
            colors[node] = color

            print(f"Color {color} assigned to Vertex {node}")

            # Recursive call for next vertex
            if graph_coloring(graph, m, colors, node + 1, n):
                return True

            # ---------------- BACKTRACKING ----------------
            # Remove color if solution not possible
            print(f"Backtracking on Vertex {node}")

            colors[node] = 0

    return False


# ---------------- MAIN PROGRAM ----------------

# Input number of vertices
n = int(input("Enter number of vertices: "))

# Create graph matrix
graph = []

print("\nEnter Adjacency Matrix:")

for i in range(n):

    row = list(map(int, input().split()))

    graph.append(row)

# Input number of colors
m = int(input("\nEnter number of colors: "))

# Initialize color list
colors = [0] * n

# Solve Graph Coloring Problem
if graph_coloring(graph, m, colors, 0, n):

    print("\nSolution Exists!")

    for i in range(n):
        print(f"Vertex {i} ---> Color {colors[i]}")

else:

    print("Solution does not exist")