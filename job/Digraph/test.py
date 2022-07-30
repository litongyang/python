# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt

# 创建图
G = nx.DiGraph()

# 增加节点
G.add_nodes_from(['USD', 'boncor:ETH', 'boncor:BNT', 'HUOBI:BNT', 'HUOBI:BTC'])

# 增加权重，数据格式（节点1，节点2，权重）
e = [('USD', 'boncor:ETH', -1100), ('boncor:ETH', 'boncor:BNT', -2), ('boncor:BNT','HUOBI:BNT',-0.1),('HUOBI:BNT', 'HUOBI:BTC', -3), ('HUOBI:BTC', 'USD', 1150)]
for k in e:
    G.add_edge(k[0], k[1], weight=k[2])
T1_edges = list(G.edges())
# print(nx.dfs_successors(G,"USD"))

path = nx.shortest_path(G.to_undirected(), source='USD', target='USD')
print("DSADASD",path)
path_edges = zip(path, path[1:])
path_subgraph = G.subgraph(path)

for i in path_edges:
    if i in path_subgraph.edges():
        print(f'{i[0]} to {i[1]} (forward)')
    else:
        print(f'{i[0]} to {i[1]} (reverse)')
# T2 = nx.dfs_tree(G, source=0,depth_limit=4)
# T2_edges =list(T2.edges())
# print(T1_edges)
# 普通的画图方式
# nx.draw(G, with_labels=True)

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





# import time
# import pytz
# import datetime
#
# def get_local_format_time(timestamp):
#   local_time=time.localtime()
#   format_time=time.strftime("%Y-%m-%d %H:%M:%S", local_time)
#   return format_time
# x = get_local_format_time(1629789355531)
# print(x)
