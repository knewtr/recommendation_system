from recommendation.services import create_graph, visualize_graph

if __name__ == "__main__":
    G = create_graph()
    visualize_graph(G)
