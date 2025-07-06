import heapq
import networkx as nx
import matplotlib.pyplot as plt


def graph_create():    
    '''
    Створюємо граф
    '''
    edges = [
            ('A', 'B', 4), ('A', 'C', 2),
            ('B', 'C', 5), ('B', 'D', 10),
            ('C', 'D', 3), ('D', 'E', 1)
        ]

    G = nx.Graph()
    G.add_edges_from([
        ("A", "B", {"weight": 5}), ("A", "C", {"weight": 3}),
        ("B", "D", {"weight": 2}),
        ("C", "D", {"weight": 1}), ("C", "E", {"weight": 3}),
        ("D", "F", {"weight": 12}),
        ("E", "F", {"weight": 10}),
        ("F", "G", {"weight": 16}),   
    ])

    return G

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        current_dist, current_vertex = heapq.heappop(priority_queue)
        if current_vertex not in visited:
            visited.add(current_vertex)

            for neighbor in graph.neighbors(current_vertex):
                weight = graph[current_vertex][neighbor]['weight']
                if (current_dist + weight) < shortest_paths[neighbor]:
                    shortest_paths[neighbor] = current_dist + weight
                    heapq.heappush(priority_queue, (current_dist + weight, neighbor))

    return shortest_paths

def main():
    G = graph_create()
    # Використання алгоритму Дейкстри
    shortest_paths = dijkstra(G, "A")
    print(shortest_paths)

    # Візуалізація графа
    pos = nx.spring_layout(G)  # Positions for all nodes
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos, width=2)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()