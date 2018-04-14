import networkx as nx
import string
from sys import maxsize

class BigramGraph:

    def __init__(self, document):
        self.word_list1 = document.split(None)
        self.word_list2 = [word.lower().rstrip(',.!?;') for word in self.word_list1]
        self.directed_graph = self.build_graph()
        self.normalize_node_counts()

    def build_graph(self): 
        dG = nx.DiGraph()

        for i, word in enumerate(self.word_list2):
            try:
                next_word = self.word_list2[i + 1]
                if not dG.has_node(word):
                    dG.add_node(word)
                    nx.set_node_attributes(dG, {word: 1}, 'count')
                else:
                    dG.nodes(data=True)[word]['count'] += 1

                if not dG.has_node(next_word):
                    dG.add_node(next_word, count=0)

                if not dG.has_edge(word, next_word):
                    dG.add_edge(word, next_word, times_taken=1, probability=0)
                else:
                    dG[word][next_word]['times_taken'] += 1
            except IndexError:
                if not dG.has_node(word):
                    dG.add_node(word, count=1)
                else:
                    dG.nodes(data=True)[word]['count'] += 1
            except:
                raise

        return dG

    def print_graph(self):
        print_nodes()
        print_edges()

    def print_nodes(self):
        for node in self.directed_graph.nodes():
            print('%s:%d' % (node, self.directed_graph.nodes(data=True)[node]['count']))

    def print_edges(self):
        for edge in self.directed_graph.edges():
            print('%s:%d' % (edge, maxsize - self.directed_graph[edge[0]][edge[1]]['weight'])) 

    def get_nodes(self):
        return self.directed_graph.nodes()

    def get_edges(self):
        return self.directed_graph.edges()

    def normalize_node_counts(self):
        nodes = self.directed_graph.nodes(data=True)
        for node in nodes:
            total_apps = 0
            edge_map = self.directed_graph[node[0]]
            for edge in edge_map:
                total_apps += edge_map[edge]['times_taken']
            for edge in edge_map:
                edge_map[edge]['probability'] = edge_map[edge]['times_taken'] / total_apps


    def get_all_nodes_at_distance(self, dir_graph, word, num_steps):
        nodes_at_distance = set()
        queued_words = [(word, 0)]
        while len(queued_words) > 0:
            curr_word, distance = queued_words.pop(0)

            if distance == num_steps:
                nodes_at_distance.add(curr_word)

            if distance < num_steps:
                neighbors = nx.neighbors(dir_graph, curr_word)
                for neighbor in neighbors:
                    if neighbor not in nodes_at_distance:
                        queued_words.append((neighbor, distance + 1))

        return nodes_at_distance


    def most_similar_words(self, word, num_steps):
        """
        Returns a list of words within 'num steps' forward
        then backward on the graph.
        """
        related_words = set()

        nodes_forward = self.get_all_nodes_at_distance(self.directed_graph, word, num_steps)

        related_words = set()
        reversed_graph = self.directed_graph.reverse(copy=True)
        for node in nodes_forward:
            nodes_backward = self.get_all_nodes_at_distance(reversed_graph, node, num_steps)
            related_words.update(nodes_backward)

        return related_words





