##########################################################################
#   test_random.py
#   Let's you test the depth and breadth algorithms in range(x) and plots a graph
##########################################################################

import igraph
import plotly.graph_objects as go
from igraph import Graph, EdgeSeq

def tree(nodes_list):
    amount_nodes = len(nodes_list)
    nr_vertices = amount_nodes
    v_label = list(map(str, range(nr_vertices)))
    G = Graph.Tree(nr_vertices, 2) # 2 stands for children number
    lay = G.layout('rt')
    position = {k: lay[k] for k in range(nr_vertices)}
    Y = [lay[k][1] for k in range(nr_vertices)]
    M = max(Y)

    es = EdgeSeq(G) # sequence of edges
    E = [e.tuple for e in G.es] # list of edges

    L = len(position)
    Xn = [position[k][0] for k in range(L)]
    Yn = [2*M-position[k][1] for k in range(L)]
    Xe = []
    Ye = []
    for edge in E:
        Xe+=[position[edge[0]][0],position[edge[1]][0], None]
        Ye+=[2*M-position[edge[0]][1],2*M-position[edge[1]][1], None]

    labels = v_label
    
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
    for nodes in nodes_list.values():       
        dict_nodes = nodes
    if dict_nodes['solved'] == True:
        fig.add_trace(go.Scatter(x=Xn,
                          y=Yn,
                          mode='markers',
                          name='winning_node',
                          marker=dict(symbol='circle-dot',
                                        size=40,
                                        color='#DC143C')))
                                                

    axis = dict(showline=False, # hide axis line, grid, ticklabels and  title
                zeroline=False,
                showgrid=False,
                showticklabels=False,
                )

    fig.update_layout(title= 'Depth first algorithm 6x6_1 board',
            
                  font_size=12,
                  xaxis=axis,
                  yaxis=axis,
                  margin=dict(l=40, r=40, b=85, t=100),
                  hovermode='closest',
                  plot_bgcolor='rgb(248,248,248)'
                  )
    fig.show()

