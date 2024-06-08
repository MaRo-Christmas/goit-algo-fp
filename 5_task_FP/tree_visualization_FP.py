
import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if not node.left:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        else:
            if not node.right:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)

def create_sample_tree():
    tree = BinaryTree()
    values = [50, 30, 70, 20, 40, 60, 80]
    for value in values:
        tree.insert(value)
    return tree

def generate_colors(num_colors):
    colors = []
    for i in range(num_colors):
        hex_color = '#{:02x}{:02x}{:02x}'.format(i * 255 // num_colors, 100 + i * 155 // num_colors, 255 - i * 255 // num_colors)
        colors.append(hex_color)
    return colors

def visualize_tree_bfs(tree):
    if not tree.root:
        return

    G = nx.Graph()
    queue = deque([tree.root])
    levels = {tree.root: 0}
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        if node.left:
            queue.append(node.left)
            levels[node.left] = levels[node] + 1
            G.add_edge(node.value, node.left.value)

        if node.right:
            queue.append(node.right)
            levels[node.right] = levels[node] + 1
            G.add_edge(node.value, node.right.value)

    colors = generate_colors(len(order))
    color_map = {node.value: colors[i] for i, node in enumerate(order)}

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=[color_map[node] for node in G.nodes], node_size=2000, font_size=15)
    plt.show()

def visualize_tree_dfs(tree):
    if not tree.root:
        return

    G = nx.Graph()
    stack = [tree.root]
    order = []
    visited = set()

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)

            if node.right:
                stack.append(node.right)
                G.add_edge(node.value, node.right.value)

            if node.left:
                stack.append(node.left)
                G.add_edge(node.value, node.left.value)

    colors = generate_colors(len(order))
    color_map = {node.value: colors[i] for i, node in enumerate(order)}

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=[color_map[node] for node in G.nodes], node_size=2000, font_size=15)
    plt.show()

if __name__ == "__main__":
    tree = create_sample_tree()
    visualize_tree_bfs(tree)
    visualize_tree_dfs(tree)
