import networkx as nx
import string
from sys import maxsize

class BigramGraph:

    def __init__(self, document):
        self.word_list1 = document.split(None)
        self.word_list2 = [word.lower().rstrip(',.!?;') for word in self.word_list1]
        self.directed_graph = self.build_graph()

    def build_graph(self): 
        dG = nx.DiGraph()

        for i, word in enumerate(self.word_list2):
            try:
                next_word = self.word_list2[i + 1]
                if not dG.has_node(word):
                    dG.add_node(word, count=1)
                else:
                    nx.get_node_attributes(dG, word)['count'] += 1

                if not dG.has_node(next_word):
                    dG.add_node(next_word, count=0)

                if not dG.has_edge(word, next_word):
                    dG.add_edge(word, next_word, weight=maxsize - 1)
                else:
                    dG.get_edge_data(word, next_word)['weight'] -= 1
            except IndexError:
                if not dG.has_node(word):
                    dG.add_node(word, count=1)
                else:
                    nx.get_node_attributes(dG, word)['count'] += 1
            except:
                raise

        return dG

    def print_graph(self):
        print_nodes()
        print_edges()

    def print_nodes(self):
        for node in self.directed_graph.nodes():
            print('%s:%d\n' % (node, self.directed_graph.node[node]['count']))

    def print_edges(self):
        for edge in self.directed_graph.edges():
            print('%s:%d\n' % (edge, maxint - self.directed_graph.edge[edge[0]][edge[1]]['weight'])) 

    def get_nodes(self):
        return self.directed_graph.nodes()

    def get_edges(self):
        return self.directed_graph.edges()




