import networkx as nx

from connections.models import Connection
from recommendations.services import create_graph, create_recommendation
from users.models import User


class PageRank:
    @staticmethod
    def recommendations(user_id, top_n=5):
        G = create_graph()

        if not G.nodes:
            return []
        pr = nx.pagerank(G, weight="weight")

        if not any(node.startswith("book_") for node in pr):
            return []

        user_books = set(
            Connection.objects.filter(user_id=user_id).values_list("book_id", flat=True)
        )
        ranked_books = {
            int(node.split("_")[1]): rank
            for node, rank in pr.items()
            if node.startswith("book_") and int(node.split("_")[1] not in user_books)
        }
        if not ranked_books:
            return []

        sorted_books = sorted(
            ranked_books.items(), key=lambda items: items[1], reverse=True
        )[:top_n]
        top_n_books = list(book_id for book_id, rank in sorted_books)

        user = User.objects.get(id=user_id)
        recommendation = create_recommendation(user, "pagerank", top_n_books)
        return list(recommendation.books.all())
