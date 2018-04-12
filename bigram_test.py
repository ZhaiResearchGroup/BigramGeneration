from Bigram import BigramGraph
import networkx as nx

if __name__ == "__main__":
	str1 = "Man who run in front of car, get tired. Man who run behind car, get exhausted."
	graph = BigramGraph(str1)
	path = nx.shortest_path(graph.directed_graph, source='man', target='exhausted', weight='weight')
	print(path)
	# print(graph.directed_graph.edges())
	# print(graph.directed_graph.nodes())