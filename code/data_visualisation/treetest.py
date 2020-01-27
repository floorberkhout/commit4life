import igraph
import plotly.graph_objects as go
from igraph import Graph, EdgeSeq

g = Graph()
g.add_vertices(3)
g = Graph([(0,1), (0,2), (2,3), (3,4), (4,2), (2,5), (5,0), (6,3), (5,6)])
g.add_edges([(0,1), (1,2)])
print(g)

fig = go.Figure()
fig.add_trace(go.Scatter(x=Xe,
                   y=Ye,
                   mode='lines',
                   line=dict(color='rgb(210,210,210)', width=1),
                   hoverinfo='none'
                   ))
fig.add_trace(go.Scatter(x=Xn,
                  y=Yn,
                  mode='markers',
                  name='nodes',
                  marker=dict(symbol='circle-dot',
                                size=18,
                                color='#008B8B',
                                line=dict(color='rgb(50,50,50)', width=1)
                                ),
                  text=labels,
                  hoverinfo='text',
                  opacity=0.8
                  ))
fig.show()

# class Tree(object):
#     def __init__(self):
#         self.left = None
#         self.child = []
#         self.data = []
#
#     def createChildren(self, amount):
#         for i in range(0, amount):
#             self.child.append(Tree())
#
#     def setChildrenValues(self, list):
#         for i in range(0,len(list)):
#             self.data.append(list[i])
#
# if __name__ == "__main__":
#     root = Tree()
#     root.createChildren(3)
#     root.setChildrenValues([5,6,7])
#     root.child[0].createChildren(2)
#     root.child[0].setChildrenValues([1,2])
#  # print some values in the tree
#     print(root.data[0])
#     print(root.child[0].data[0])
#