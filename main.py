import numpy as np
import math
from sympy import symbols
import networkx as nx
import matplotlib.pyplot as plt
import graph_tool.all as gt

#I'm mostly following what I learned in
#Peskin & Schoeder's introductory section on Feynman Diagrams.

λ = symbols('lambda')  # Define λ as a symbolic variable
ϕ = symbols('phi')  # Define ϕ as a symbolic variable
H_I_ϕ_pow = 4
H_I = (ϕ**H_I_ϕ_pow)*λ/math.factorial(4) #Lagrangian term for ϕ^n theory

order = 2
externals=2

def Wick(operators, contraction, contractions=[], verbose=True, recursion=0): #Executes Wick's theorem
    if len(operators) % 2 == 1: return [0]

    if len(operators)==2:
        return contraction + [tuple(operators)]
    
    contractees = operators[1:]
    for i in range(len(contractees)):
        
        if verbose==False and i>0 and len(contractions)<30 or True:
            wick = Wick(
                contractees[0:i]+contractees[i+1:],
                contraction + [(operators[0], contractees[i])],
                contractions, recursion+1
            )
            if wick:
                contractions.append(wick)

    if recursion==0:
        n=len(operators)
        print("Expected number of contractions:",int(math.factorial(n) / ( math.factorial(int(n/2)) * (2**(int(n/2))) )))
        print("Number of contractions found:",len(contractions))
        return contractions
    
def FeynmanDiagram(contractions, points):
    # Create an empty graph
    g = gt.Graph(directed=False)
    vertices = []
    vertex_map = {}

    # Add some vertices (nodes)
    for point in points:
        vertex = g.add_vertex()
        vertices.append(vertex)
        vertex_map[point] = vertex

    # Add edges (connections between nodes)
    for c in contractions:
        g.add_edge(vertex_map[c[0]], vertex_map[c[1]])

    # Assign names to the vertices
    vertex_labels = g.new_vertex_property("string")
    for map in vertex_map.items():
        vertex_labels[map[1]] = map[0]

    # Use a force-directed layout to improve spacing
    pos = gt.random_layout(g)  # Adjust C to bring nodes closer

    # Draw the graph
    gt.graph_draw(g, pos,
                vertex_text=vertex_labels, vertex_font_size=14,
                vertex_fill_color="skyblue", vertex_size=30,
                edge_color="black", edge_pen_width=2)


operators = [-i-1 for i in range(externals)]
for i in range(order):
    operators += [i+1]*H_I_ϕ_pow

wick = Wick(operators,[], verbose=False)
for l in wick:
    print(l)

points = [-i-1 for i in range(externals)] + [i+1 for i in range(order)]
print(points)

contraction = wick[550] #Tries to get a diagram with no vacuum bubbles
print(contraction)
FeynmanDiagram(contraction,points)

