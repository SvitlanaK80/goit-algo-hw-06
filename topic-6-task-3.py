'''
Task 3

Implement Dijkstra's algorithm to find the shortest path in the developed graph: 
add weights to the edges and find the shortest path between all graph vertices.

'''

import networkx as nx

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

# Алгоритм Дейкстри: знаходимо найкоротші відстані від 'Central Station'
def dijkstra_shortest_paths(graph, start):
    return nx.single_source_dijkstra_path_length(graph, start, weight='weight')

# Виводимо найкоротші відстані від "Central Station" до інших
print("\n Найкоротші шляхи від 'Central Station':")
shortest_paths = dijkstra_shortest_paths(G, 'Central Station')
for destination, distance in shortest_paths.items():
    print(f"   до {destination}: {distance} хв")

# Знаходження шляху
print("\n Найкоротші маршрути (шляхи) від 'Central Station':")
for destination in G.nodes:
    if destination != 'Central Station':
        path = nx.shortest_path(G, source='Central Station', target=destination, weight='weight')
        print(f"   маршрут до {destination}: {' --- '.join(path)}")


