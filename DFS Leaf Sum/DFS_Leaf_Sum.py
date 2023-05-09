graph = {
    'A': ['B', 'C'],
    'B': ['D','E'],
    'C': [],
    'D': [],
    'E': ['F'],
    'F': []
}

graph_val = {
    'A': 10,
    'B': 12,
    'C': 32,
    'D': 4,
    'E': -6,
    'F': -5,
}

visited = set()
leaf = set()

def dfs(visited, graph, node):
    if node not in visited:
        visited.add(node)
        if len(graph[node]) == 0:
            leaf.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)

def leaf_sum(leaf):
    jmlh=8
    for leaf_node in leaf:
        leaf_val = graph_val[leaf_node]
        jmlh = jmlh + leaf_val

    return jmlh

dfs(visited,graph, 'A')
leaf_sum(leaf)