import matplotlib.cm as cm
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import networkx as nx

from books.models import Book
from connections.models import Connection
from recommendations.models import Recommendation
from users.models import User


def create_graph():
    D = nx.Graph()

    for book in Book.objects.all():
        D.add_node(f"book_{book.id}", type="book")

    for user in User.objects.all():
        D.add_node(f"user_{user.id}", type="user")

    for con in Connection.objects.select_related("book", "user"):
        user_node = f"user_{con.user.id}"
        book_node = f"book_{con.book.id}"
        weight = con.rating if con.rating else 1.0
        D.add_edge(user_node, book_node, weight=weight)

    return D


# def create_digraph():
#     DG = nx.DiGraph()
#
#     for book in Book.objects.all():
#         DG.add_node(f"book_{book.id}", type="book")
#
#     for user in User.objects.all():
#         DG.add_node(f"user_{user.id}", type="user")
#
#     for con in Connection.objects.select_related("book", "user"):
#         user_node = f"user_{con.user.id}"
#         book_node = f"book_{con.book.id}"
#         weight = con.rating if con.rating else 1.0
#         DG.add_edge(user_node, book_node, weight=weight)
#
#     return DG


def visualize_graph(G):
    pagerank = nx.pagerank(G)
    node_sizes = [v * 3000 for v in pagerank.values()]
    node_colors = list(pagerank.values())

    pos = nx.spring_layout(G, seed=42)

    norm = mcolors.Normalize(vmin=min(node_colors), vmax=max(node_colors))
    cmap = cm.viridis

    fig, ax = plt.subplots(figsize=(10, 8))

    nodes = nx.draw_networkx_nodes(
        G, pos, node_size=node_sizes, node_color=node_colors, cmap=cmap, ax=ax
    )

    nx.draw_networkx_edges(G, pos, arrows=True, ax=ax)
    labels = {node: f"{node}\n{rank:.2f}" for node, rank in pagerank.items()}
    nx.draw_networkx_labels(G, pos, labels, font_size=8, ax=ax)

    sm = cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])

    fig.colorbar(sm, ax=ax, label="PageRank")

    ax.set_title("Граф для визуализации алгоритма PageRank")
    ax.axis("off")
    plt.tight_layout()
    plt.show()


def create_recommendation(user, method, book_list):
    recommendation = Recommendation.objects.create(user=user, method=method)
    recommendation.books.add(*Book.objects.filter(id__in=book_list))
    recommendation.save()
    return recommendation
