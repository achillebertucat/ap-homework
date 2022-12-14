# EXERCICE 1

def parse(filename):
    dico = {}
    with open(filename, 'r') as f:
        for line in f:
            content= line.rstrip().split(',')
            sommet, arrete, poids = content
            if sommet not in dico:
                dico[sommet] = {arrete: int(poids)}
            else:
                dico[sommet][arrete] = int(poids)
    return(dico)

print('EXERCICE 1')
data = parse('TP_graphes/graph.csv')
print(data)

# pour la suite on pose

G= {'a': {'b': 7, 'd': 9, 'c': 14},
 'b': {'d': 10, 'e': 15},
 'c': {'d': 2, 'f': 9},
 'd': {'e': 11},
 'e': {'f': 6}}

 #EXERCICE 2

# +
print('EXERCICE 2')
 def number_vertices(graph):
    summits= []
    for sommet, arrete in graph.items():
        if sommet not in summits:
            summits.append(sommet)
            if arrete not in summits:
                summits.append(arrete)
        else:
            if arrete not in summits:
                summits.append(arrete)
    return(len(summits))


# -


from graphs import parse_graph1
from graphs import to_graphviz


# +
#EXERCICE 3
def reachable(key,graph,res=set()):
    if key in graph:
        for m in graph[key].keys():
            if m not in res:
                res.add(m)
                res=reachable(m,graph,res)
    return res

import distance

def shortest_distance(graph, v1, v2):

    # initialisation : on se définit une variable locale à la fonction qui matérialise le marquage

    visited = {}
    visited[v1]=0
    parents = {}
    # ensuite on fait une boucle jusqu'à ce que la condition soit remplie
    while True:

        # les arêtes qui satisfont le critère 
        edges = set()
        #on localise toutes les arêtes qui lient un noeud visité à un noeud non visité
        # on énumère toutes les arêtes, et on ajoute dans edges celles qui satisfont le critère
        for s_visited in visited.keys():
            if s_visited in graph: 
                for s in graph[s_visited].keys():
                    if s not in visited : 
                        edges.add((s_visited,s))
         

        # si on n'a aucune arête c'est que c'est raté
        if not edges:
            return None 

        # sinon on trouve la meilleure
        shortest_length = math.inf
        shortest_vertex = None
        for edge in edges:
             # trouver la plus courte et mémoriser le sommet correspondant
            if visited[edge[0]]+graph[edge[0]][edge[1]] < shortest_length :
                shortest_length = visited[edge[0]]+graph[edge[0]][edge[1]]
                shortest_vertex = edge[1]

        # marquer le sommet correspondant
        visited[shortest_vertex] = shortest_length
        # regarder si c'est le sommet 
        if shortest_vertex == v2:
            return shortest_length
        


# +
 #EXERCICE5
def shortest_path(graph, v1, v2):

    # initialisation : on se définit une variable locale à la fonction qui matérialise le marquage

    visited = {}
    visited[v1]=0
    source = {}

    # ensuite on fait une boucle jusqu'à ce que la condition soit remplie
    while True:

        # les arêtes qui satisfont le critère 
        edges = set()
        #on localise toutes les arêtes qui lient un noeud visité à un noeud non visité
        # on énumère toutes les arêtes, et on ajoute dans edges celles qui satisfont le critère
        for s_visited in visited.keys():
            if s_visited in graph: 
                for s in graph[s_visited].keys():
                    if s not in visited : 
                        edges.add((s_visited,s))
         

        # si on n'a aucune arête c'est que c'est raté
        if not edges:
            return None 

        # sinon on trouve la meilleure
        shortest_length = math.inf
        shortest_vertex = None
        shortest_edge = None 
        for edge in edges:
             # trouver la plus courte et mémoriser le sommet correspondant
            if visited[edge[0]]+graph[edge[0]][edge[1]] < shortest_length :
                shortest_length = visited[edge[0]]+graph[edge[0]][edge[1]]
                shortest_vertex = edge[1]
                shortest_edge = edge

        # marquer le sommet correspondant
        visited[shortest_vertex] = shortest_length
        source[shortest_vertex] = shortest_edge[0]
        # regarder si c'est le sommet 
        if shortest_vertex == v2:
            return shortest_length, reversepath(source, v1, v2)
    
print(shortest_path(G, 'a', 'f'))
