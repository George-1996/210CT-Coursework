class Graph(object):
    def __init__(self,dictionary=None):
        if not dictionary!=None:
            dictionary = {}
        self.dictionary = dictionary

    def Shownode(self,dictionary):
        print(self.dictionary)

    def add_node(self,node):
        if node not in self.dictionary:
            self.dictionary[node] = []
        return self.dictionary

    def add_edge(self, fromnode, tonode):
        if fromnode in self.dictionary and tonode in self.dictionary:
            self.dictionary[fromnode].append(tonode)
            self.dictionary[tonode].append(fromnode)
        return self.dictionary
            

if __name__ == "__main__":

    G = {"a":["d","h"],
         "b":["i"],
         "c":["i"],
         "d":["f","a"],
         "e":["g"],
         "f":["d","j"],
         "g":["e"],
         "h":["a"],
         "i":["b","c"],
         "j":["f"]}

    gr = Graph(G)
    gr.add_node("y")
    gr.add_edge("y","h")
    gr.Shownode(G)



#CLASS GRAPH(object)
#    __INIT__(self, dictionary <- NONE )
#        if not dictionary != NONE
#            dictionary <- {}
#        self.dictionary <- dictionary
#
#    SHOWNODE(self, dictionary)
#        print self.dictionary
#
#    ADD_NODE(self,node)
#        if node not in self.dictionary
#            self.dictionary[node] <- []
#        return self.dictionary
#
#    ADD_EDGE(self,fromnode, tonode)
#        if fromnode in self.dictionary AND tonode in self.dictionary
#            self.dictionary[fromnode].append(tonode)
#            self.dictionary[tonode].append(fromnode)
#        return self.dictionary
