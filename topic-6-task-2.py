'''
Task 2

Write a program that uses the DFS and BFS algorithms to find paths in the graph that 
you developed in the first task.

Then compare the results of both algorithms for this graph, 
highlighting the difference in the paths obtained. Please explain why the paths for the 
algorithms are the way they are.

'''

import networkx as nx
import matplotlib.pyplot as plt

# граф транспортної мережі Києва
city_transport_graph = {
    'Central Station': ['University', 'Khreshchatyk', 'Beresteiska'],
    'University': ['Central Station', 'Politekhnichnyi Instytut'],
    'Khreshchatyk': ['Central Station', 'Arsenalna'],
    'Politekhnichnyi Instytut': ['University', 'Shuliavska'],
    'Arsenalna': ['Khreshchatyk', 'Dnipro'],
    'Shuliavska': ['Politekhnichnyi Instytut', 'Beresteiska'],
    'Dnipro': ['Arsenalna', 'Central Station'],
    'Beresteiska': ['Shuliavska']
}

# Створення графа NetworkX
G = nx.Graph()

# Додавання ребер до графа
for station, neighbors in city_transport_graph.items():
    for neighbor in neighbors:
        G.add_edge(station, neighbor)

# Аналіз графа
print("🔹 Кількість станцій (вершин):", G.number_of_nodes())
print("🔹 Кількість з'єднань (ребер):", G.number_of_edges())
print("🔹 Ступінь кожної станції:")
for station, degree in G.degree():
    print(f"   {station}: {degree}")

# DFS
dfs_tree = nx.dfs_tree(G, source='Central Station')
print("\nОбход в глибину DFS:")
print(list(dfs_tree.edges()))  # виведе ребра DFS-дерева з коренем у вузлі 'Central Station'

# BFS
bfs_tree = nx.bfs_tree(G, source='Central Station')
print("\nОбход в ширину BFS:")
print(list(bfs_tree.edges()))  # виведе ребра BFS-дерева з коренем у вузлі 'Central Station'

# Візуалізація графа
plt.figure(figsize=(10, 7))
pos = nx.circular_layout(G)  # Автоматичне розташування (seed=42)
nx.draw(
    G, pos,
    with_labels=True,
    node_color='skyblue',
    node_size=2000,
    font_size=10,
    font_weight='bold',
    edge_color='gray'
)
plt.title("Транспортна мережа Києва (Модель)", fontsize=14)
plt.show()