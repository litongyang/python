import networkx as nx
import matplotlib.pyplot as plt

import networkx as nx
import matplotlib.pyplot as plt


def main():
    G = nx.DiGraph()

    # 添加对应的边和点
    for i in range(1, 10):
        G.add_node(i, desc='v' + str(i))  # 结点名称不能为str,desc为标签即结点名称
    G.add_edge(1, 2, weight='6')  # 添加边， 参数name为边权值
    G.add_edge(1, 3, weight='4')
    G.add_edge(1, 4, weight='5')
    G.add_edge(2, 5, weight='111')
    G.add_edge(5, 2, weight='2')
    G.add_edge(3, 5, weight='1')
    G.add_edge(4, 6, weight='2')
    G.add_edge(5, 7, weight='9')
    G.add_edge(5, 8, weight='7')
    G.add_edge(6, 8, weight='4')
    G.add_edge(7, 9, weight='2')
    G.add_edge(8, 9, weight='4')
    print(list(G.nodes()))
    # print(nx.dfs_successors(G, 1, depth_limit=5))

    path = nx.shortest_path(G.to_undirected(), source=1, target=2)
    print(path)
    path_edges = zip(path, path[1:])
    path_subgraph = G.subgraph(path)

    for i in path_edges:
        if i in path_subgraph.edges():
            print(f'{i[0]} to {i[1]} (forward)')
        else:
            print(f'{i[0]} to {i[1]} (reverse)')

    #画点和边
    pos = nx.circular_layout(G)
    nx.draw(G, pos)

    #画点标签
    node_labels = nx.get_node_attributes(G, 'desc')
    nx.draw_networkx_labels(G, pos, labels=node_labels)

    #画边标签
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,label_pos=0.3, font_size=7)
    plt.show()


if __name__ == '__main__':
    main()
