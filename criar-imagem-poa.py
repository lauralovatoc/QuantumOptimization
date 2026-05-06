import osmnx as ox

G = ox.load_graphml("dados/grafos/poa.graphml")

fig, ax = ox.plot_graph(
    G,
    node_size=0,
    edge_color="gray",
    edge_linewidth=0.5,
    edge_alpha=0.4,
    bgcolor="white",
    show=False,
    close=False
)

fig.savefig("dados/img/poa.png", dpi=300)