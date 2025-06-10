'''
Task 1

Create a graph using the networkX library to model a real-world network 
(e.g., a city's transportation network, a social network, or an Internet topology).

Visualize the created graph, and analyze the main characteristics 
(for example, the number of vertices and edges, the degree of vertices).

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
print("Кількість станцій (вершин):", G.number_of_nodes())
print("Кількість з'єднань (ребер):", G.number_of_edges())
print("Ступінь кожної станції:")
for station, degree in G.degree():
    print(f"   {station}: {degree}")

# Візуалізація графа
plt.figure(figsize=(10, 7))
pos = nx.circular_layout(G)  # Автоматичне розташування seed=42
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