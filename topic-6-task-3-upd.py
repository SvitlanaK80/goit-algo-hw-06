'''
Task 3

Implement Dijkstra's algorithm to find the shortest path in the developed graph: 
add weights to the edges and find the shortest path between all graph vertices.

'''

import heapq

import networkx as nx
import matplotlib.pyplot as plt

# Граф транспортної мережі Києва з вагами
# Вага означає умовний час у хвилинах між станціями
city_transport_graph = {
    'Central Station': {'University': 4, 'Khreshchatyk': 5, 'Beresteiska': 7},
    'University': {'Central Station': 4, 'Politekhnichnyi Instytut': 3},
    'Khreshchatyk': {'Central Station': 5, 'Arsenalna': 2},
    'Politekhnichnyi Instytut': {'University': 3, 'Shuliavska': 6},
    'Arsenalna': {'Khreshchatyk': 2, 'Dnipro': 4},
    'Shuliavska': {'Politekhnichnyi Instytut': 6, 'Beresteiska': 5},
    'Dnipro': {'Arsenalna': 4, 'Central Station': 8},
    'Beresteiska': {'Shuliavska': 5, 'Central Station': 7}
}

# Створення графа
G = nx.Graph()

# Додавання ребер з вагами
for station, neighbors in city_transport_graph.items():
    for neighbor, weight in neighbors.items():
        G.add_edge(station, neighbor, weight=weight)

# Аналіз графа
print("Кількість станцій (вершин):", G.number_of_nodes())
print("Кількість з'єднань (ребер):", G.number_of_edges())
print("Ступінь кожної станції:")
for station, degree in G.degree():
    print(f"   {station}: {degree}")

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    return


# Використання алгоритму Дейкстри
shortest_paths = dijkstra(G, "Central Station")
print(shortest_paths)

# Візуалізація графа
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()

