import uuid
import random
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root: Node, visual = False):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

    if not visual:
        fig, ax = plt.subplots(figsize=(10, 6))
        fig.canvas.manager.set_window_title("Вихідне дерево")
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    if not visual:
        plt.show()


def make_heap_tree(heap: list):
    '''
    Перетворення списку на купу та побудова бінарного дерева
    '''
    if heap:
        heapq.heapify(heap)
        print(f"Наша купа:\n{heap}")
        heap = [Node(val) for val in heap]

        i = 0
        while True:
            if 2 * i + 1 >= len(heap):
                break
            heap[i].left = heap[2 * i + 1]
            if 2 * i + 2 >= len(heap):
                break
            heap[i].right = heap[2 * i + 2]
            i += 1
        
        return heap[0]


def count_nodes(root: Node) -> int:
    '''
    Рахуємо кількість вершин
    '''
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def get_colors(root: Node) -> list:
    '''
    Підключаємо палітру кольорів
    '''
    count = count_nodes(root)
    cmap = plt.get_cmap('plasma')
    colors = [cmap(i / count) for i in range(count)]
    return colors


def reset_colors(root):
    '''
    Скидаємо кольори на стандартні
    '''
    if not root:
        return
    root.color = "skyblue"
    reset_colors(root.left)
    reset_colors(root.right)


def dfs_visualize(root):
    '''
    Візуалізація обходу дерева вглибину
    '''
    reset_colors(root)
    visited = set()
    stack = [root]
    colors = get_colors(root)
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.canvas.manager.set_window_title("DFS обхід")
    i = 0
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            vertex.color = colors [i]            
            if vertex.right:
                stack.append(vertex.right)
            if vertex.left:
                stack.append(vertex.left)
            i += 1
        draw_tree(root, visual = True)
        plt.pause(1)
    plt.show()


def bfs_visualize(root):
    '''
    Візуалізація обходу дерева вширину
    '''
    reset_colors(root)
    visited = set()
    queue = deque([root])
    colors = get_colors(root)
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.canvas.manager.set_window_title("BFS обхід")
    i = 0
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            vertex.color = colors [i] 
            if vertex.left:
                queue.append(vertex.left)
            if vertex.right:
                queue.append(vertex.right)
            i += 1
        draw_tree(root, visual = True)
        plt.pause(1)
    plt.show()


if __name__ == "__main__":
    #-------------------------СТАНДАРТНЕ ДЕРЕВО------------------------#
    # Створення дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # Відображення дерева
    draw_tree(root)

    # Візуалізація обходу вглибину
    dfs_visualize(root)

    # Візуалізація обходу вширину
    bfs_visualize(root)

    #-------------------------ДЕРЕВО-КУПА ЗІ СПИСКУ------------------------#
    heap = [random.randint(0, 100) for _ in range (20)]
    # Відображення купи
    root = make_heap_tree(heap)
    draw_tree(root)

    # Візуалізація обходу вглибину
    dfs_visualize(root)

    # Візуалізація обходу вширину
    bfs_visualize(root)