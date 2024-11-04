# Exercise 1
from collections import deque

def bfs_shortest_path(graph, start, goal):
    queue = deque([[start]])
    visited = set([start])

    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node == goal:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

    return None

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(bfs_shortest_path(graph, 'A', 'F'))

# Exercise 2
def detect_cycle_bfs(graph):
    visited = set()
    for start in graph:
        if start not in visited:
            queue = deque([(start, None)])
            visited.add(start)

            while queue:
                current_node, parent = queue.popleft()

                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, current_node))
                    elif neighbor != parent:
                        return True


    return False
graph_with_cycle = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'C'],
    'D': ['C', 'E'],
    'E': ['B', 'D'],
}

graph_without_cycle = {
    'A': ['C', 'B'],
    'B': ['A', 'D','C'],
    'C': ['A'],
    'D': ['B']
}

print(detect_cycle_bfs(graph_with_cycle))  
print(detect_cycle_bfs(graph_without_cycle))  

# Exercise 3
import heapq
def dijkstra(graph, start):
    distances = {v: float('inf') for v in graph}
    distances[start] = 0
    prev = {v: None for v in graph}
    queue = [(0, start)]
    while queue:
        dist, node = heapq.heappop(queue)
        if dist > distances[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                prev[neighbor] = node
                heapq.heappush(queue, (new_dist, neighbor))             
    return distances, prev
def reconstruct_path(prev, start, goal):
    path = []
    while goal:
        path.append(goal)
        goal = prev[goal]
    return path[::-1] if path[-1] == start else []
graph = {
    'A': [('B', 8), ('C', 4)],
    'B': [('A', 1), ('C', 4), ('D', 6)],
    'C': [('A', 3), ('B', 2), ('D', 1)],
    'D': [('B', 6), ('C', 1)]
}
distances, prev = dijkstra(graph, 'A')
print("The shortest distance:", distances)
print("The shortest path from A-D:", reconstruct_path(prev, 'A', 'D'))


# Exercise 4
from collections import deque

def bipartite(graph):
    color = {}
    
    for node in graph:
        if node not in color:
            queue = deque([node])
            color[node] = 0
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[current]
                        queue.append(neighbor)
                    elif color[neighbor] == color[current]:
                        return False
    return True
graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'A']
}

print(bipartite(graph))