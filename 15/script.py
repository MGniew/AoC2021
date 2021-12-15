# dijkstra - https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/

import typing as tp
import sys
import heapq

from tqdm import tqdm
from collections import defaultdict


class Graph:

    def __init__(self, nodes, edges):
        """Constructor."""
        self.nodes = nodes
        self.edges = edges

    def __str__(self):
        result = ""
        for s_node in self.edges.keys():
            for e_node, edge_value in self.edges[s_node].items():
                result += f"{s_node} --{edge_value}-- {e_node}\n"
        return result

    def dijkstra(self, start=-1, end=None):
        distances = {node: sys.maxsize for node in self.nodes}
        distances[start] = 0

        pq = [(0, start)]
        while len(pq) > 0:
            current_distance, current_node = heapq.heappop(pq)
            if current_distance > distances[current_node]:
                continue

            for neighbor, edge_value in self.edges[current_node].items():
                distance = current_distance + edge_value

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        if end:
            return distances[end]
        return distances



def load_graph(filename, k=-1):

    with open(filename) as f:
        data = [[(int(v) + k) % 10 + 1 for v in line] for line in f.read().splitlines()]

    edges = defaultdict(dict)
    nodes = [-1]  # Dummy starting node
    edges[-1][0] = 0  # Edge to the first node

    for i, row in enumerate(data):
        for j, value in enumerate(row):
            idx = i * len(data) + j
            nodes.append(i * len(data) + j)
            if i > 0:
                edges[idx][idx - len(data)] = data[i - 1][j]
            if i + 1 < len(data):
                edges[idx][idx + len(data)] = data[i + 1][j]
            if j > 0:
                edges[idx][idx - 1] = data[i][j - 1]
            if j + 1 < len(row):
                edges[idx][idx + 1] = data[i][j + 1]

    return Graph(nodes, edges)


def load_graph_part2(filename):

    with open(filename) as f:
        data = [[int(v) for v in line] for line in f.read().splitlines()]

    def increment(value, i):
        value += i
        if value > 9:
            value -= 9
        return value

    new_data = list()
    for i in range(1, 5):
        new_data.append([[increment(v, i) for v in line] for line in data])
    for i, row in enumerate(data):
        for new_d in new_data:
            row.extend(new_d[i])

    new_data = list()
    for i in range(1, 5):
        new_data.append([[increment(v, i) for v in line] for line in data])
    for new_d in new_data:
        data.extend(new_d)

    edges = defaultdict(dict)
    nodes = [-1]  # Dummy starting node
    edges[-1][0] = 0  # Edge to the first node

    for i, row in enumerate(data):
        for j, value in enumerate(row):
            idx = i * len(data) + j
            nodes.append(i * len(data) + j)
            if i > 0:
                edges[idx][idx - len(data)] = data[i - 1][j]
            if i + 1 < len(data):
                edges[idx][idx + len(data)] = data[i + 1][j]
            if j > 0:
                edges[idx][idx - 1] = data[i][j - 1]
            if j + 1 < len(row):
                edges[idx][idx + 1] = data[i][j + 1]

    return Graph(nodes, edges)


def main():
    graph = load_graph("input")
    print("Part 1:", graph.dijkstra(end=graph.nodes[-1]))

    graph = load_graph_part2("input")
    print("Part 2:", graph.dijkstra(end=graph.nodes[-1]))

if __name__ == "__main__":
    main()



