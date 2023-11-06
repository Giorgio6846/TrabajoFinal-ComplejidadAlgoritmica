import src.tools as tools

startingNode = "Pais.Peru"

def getAllProvincias(Grafo):
    visited = []
    
    visited.append(startingNode)
    queue = getAll(Grafo, 1)
    
    provinciasDep = []
    
    """
    for item in queue:
        #print(item)
        for node in Grafo.edges(item):
            if getTipoNodo(node[1]) == "Prov":
                provinciasDep.append(node[1])        
        
        visited.append(item)
    """
    
    while queue:
        item = queue.pop()
        
        for nodo0, nodo1 in Grafo.edges(item):
            if tools.getTipoNodo(nodo1) == "Prov":
                provinciasDep.append(nodo1)
            
    return provinciasDep

def getProvincia(Grafo, Departamento):
    #Departamento = addDepartamentoString(Departamento)
    visited = []
    
    visited.append(startingNode)
    queue = getAll(Grafo, 1)
        
    provinciasDep = []
    
    for departamento in queue:
        if departamento == Departamento:
            for nodosConectados0, nodosConectados1 in Grafo.edges(departamento):
                if nodosConectados1 not in visited:
                    provinciasDep.append(nodosConectados1)
                    
    return provinciasDep


def getAll(Grafo, Nivel):
    listDatos = []
    
    visited = []
    visited.append(startingNode)
    
    queue = []
    queue.append(startingNode)

    while queue:
        item = queue.pop()
        
        for node0, node1 in Grafo.edges(item):
            
            tipoNodo = tools.getTipoNodo(node1)
            
            if Nivel == 1:
                
                if tipoNodo == "Dep":
                    listDatos.append(node1)
            
            elif Nivel == 2:
            
                if tipoNodo == "Dep":
                    if node1 not in visited:
                        queue.append(node1)                  
                elif tipoNodo == "Prov":
                    listDatos.append(node1)
                    
            elif Nivel == 3:
                
                if tipoNodo == "Dep" or tipoNodo == "Prov":
                    if node1 not in visited:
                        queue.append(node1)
                elif tipoNodo == "Dis":
                    listDatos.append(Grafo.nodes[node1]["provincia"] + "." + Grafo.nodes[node1]["Label"])
            elif Nivel == 4:

                if tipoNodo == "Dep" or tipoNodo == "Prov" or tipoNodo == "Dis":
                    if node1 not in visited:
                        queue.append(node1)
                elif tipoNodo =="Calle":
                    listDatos.append(node1)

        visited.append(item)
    
    return listDatos