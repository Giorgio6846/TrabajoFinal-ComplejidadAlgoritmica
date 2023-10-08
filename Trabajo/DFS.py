import pandas as pd
import networkx as nx

# Crear el grafo
G = nx.Graph()
G.add_node("Perú")

# Cargar los datos desde el archivo CSV y agregar nodos y aristas al grafo#
#qUIZAS deban cambiar la direccion (quizas = deben fabio la maama de fabio)
df = pd.read_csv('Dataframe.csv')
for index, row in df.iterrows():
    persona = row['quien_respondio']
    departamento = row['departamento']
    G.add_node(departamento)
    G.add_edge(departamento, persona)

# Nodo inicial para el recorrido en profundidad (puede ser cualquier departamento)
start_node = "Perú"  # Puedes cambiar esto al departamento deseado
for departamento in G.nodes():
    if departamento != "Perú":
        G.add_edge("Perú", departamento)

# Función para realizar el recorrido en profundidad sin recursión
def dfs(graph, start):
    contador = 0
    stack = [(start, None)]  # Usar una pila de tuplas (nodo, persona)
    visited = set()  # Conjunto para llevar un seguimiento de los nodos visitados

    while stack:
        node, persona = stack.pop()
        if node and node not in visited:
            visited.add(node)
            if persona:
                print(contador)
                print(f"Persona: {persona}, Departamento: {node}")
                contador +=1
            neighbors = list(graph.neighbors(node))
            for neighbor in neighbors:
                stack.append((neighbor, node))

# Llamar a la función DFS con el nodo inicial
dfs(G, start_node)
