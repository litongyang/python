import networkx as nx
from pprint import pprint
import matplotlib.pyplot as plt

# Create the graph with unique edges to check the algorithm correctness
G = nx.DiGraph()
G.add_edges_from([
    [1,2],
    [1,2],
    [1,2],
    [2,3],
    [2,3],
    [2,3],
    [3,4],
    [3,4],
    [2,4]
])
G.add_edge(1,2,data='WAKA', weight=2)
G.add_edge(2,3,data='WAKKA',weight=2)
G.add_edge(2,4,data='WAKA-WAKA',weight=2)
G.add_edge(4,1,data='WAKA-WAKA',weight=2)
G.add_edge(1,3,data='WAKA-WAKA',weight=2)

# Our source and destination nodes
source = 1
destination = 4

# All unique single paths, like in nx.DiGraph
unique_single_paths = set(
    tuple(path)  # Sets can't be used with lists because they are not hashable
    for path in nx.all_simple_paths(G, source, destination)
)
print("dasda",unique_single_paths)
combined_single_paths = []
for path in unique_single_paths:
    # Get all node pairs in path:
    # [1,2,3,4] -> [[1,2],[2,3],[3,4]]
    pairs = [path[i: i + 2] for i in range(len(path)-1)]

    # Construct the combined list for path
    combined_single_paths.append([
        (pair, G[pair[0]][pair[1]])  # Pair and all node between these nodes
        for pair in pairs
    ])
pprint(combined_single_paths)

# 生成节点位置序列
pos = nx.circular_layout(G)

# 重新获取权重序列
weights = nx.get_edge_attributes(G, "weight")

# 画节点图
nx.draw_networkx(G, pos, with_labels=True,linewidths=0)
# 画权重图
nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)

# 展示
plt.show()