from queue import PriorityQueue

# Graph with costs
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5), ('G', 2)],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 5,
    'B': 3,
    'C': 2,
    'D': 6,
    'E': 4,
    'F': 1,
    'G': 0
}

def a_star(start, goal):

    pq = PriorityQueue()

    pq.put((0, start))

    cost = {start: 0}

    parent = {start: None}

    while not pq.empty():

        current = pq.get()[1]

        if current == goal:
            break

        for neighbour, weight in graph[current]:

            new_cost = cost[current] + weight

            if neighbour not in cost or new_cost < cost[neighbour]:

                cost[neighbour] = new_cost

                priority = new_cost + heuristic[neighbour]

                pq.put((priority, neighbour))

                parent[neighbour] = current

    # Reconstruct path
    path = []

    node = goal

    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()

    return path


path = a_star('A', 'G')

print("Shortest Path:", path)