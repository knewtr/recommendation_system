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
    # Вычисление PageRank
    pagerank = nx.pagerank(G)

    # Получаем размер и цвет узлов по значению PageRank
    node_sizes = [v * 3000 for v in pagerank.values()]
    node_colors = list(pagerank.values())

    # Положение узлов
    pos = nx.spring_layout(G)

    # Рисуем узлы в соответствии с PageRank
    nodes = nx.draw_networkx_nodes(
        G, pos, node_size=node_sizes, node_color=node_colors, cmap=plt.cm.viridis
    )

    # Рисуем ребра и метки
    nx.draw_networkx_edges(G, pos, arrows=True)
    labels = {node: f"{node}\n{rank:.2f}" for node, rank in pagerank.items()}
    nx.draw_networkx_labels(G, pos, labels, font_size=10)

    sm = plt.cm.ScalarMappable(cmap=plt.cm.viridis)
    sm.set_array(node_colors)
    plt.colorbar(sm, label="PageRank")

    plt.title("Граф для визуализации алгоритма PageRank")
    plt.show()


def create_recommendation(user, method, book_id):
    recommendation = Recommendation.objects.create(user=user, method=method)
    recommendation.books.set(Book.objects.filter(id__in=book_ids))
    recommendation.save()
    return recommendation
