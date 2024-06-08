
import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        node = Node(key)
        self.heap.append(node)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[parent_index].val > self.heap[index].val:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self.heapify_up(parent_index)

    def get_tree_root(self):
        if not self.heap:
            return None
        for i in range(len(self.heap)):
            left_index = 2 * i + 1
            right_index = 2 * i + 2
            if left_index < len(self.heap):
                self.heap[i].left = self.heap[left_index]
            if right_index < len(self.heap):
                self.heap[i].right = self.heap[right_index]
        return self.heap[0]


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
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


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


# Створення та заповнення бінарної купи
binary_heap = BinaryHeap()
binary_heap.insert(10)
binary_heap.insert(20)
binary_heap.insert(5)
binary_heap.insert(30)
binary_heap.insert(40)
binary_heap.insert(15)

# Отримання кореня дерева та відображення дерева
heap_root = binary_heap.get_tree_root()
draw_tree(heap_root)
