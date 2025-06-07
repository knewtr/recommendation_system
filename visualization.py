import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from recommendations.services import create_graph, visualize_graph

if __name__ == "__main__":
    G = create_graph()
    visualize_graph(G)
