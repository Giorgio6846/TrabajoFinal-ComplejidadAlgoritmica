import src.tools as tools

startingNode = "Pais.Peru"

def getDepartamentos(Grafo):
    listDepartamentos = []
    
    for departamentos in Grafo.edges(startingNode):
        listDepartamentos.append(departamentos[1])
        
    return listDepartamentos

def getAllProvincias1(Grafo):
    visited = []
    
    visited.append(startingNode)
    queue = getDepartamentos(Grafo)
    
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
    queue = getDepartamentos(Grafo)
        
    provinciasDep = []
    
    for departamento in queue:
        if departamento == Departamento:
            for nodosConectados0, nodosConectados1 in Grafo.edges(departamento):
                if nodosConectados1 not in visited:
                    provinciasDep.append(nodosConectados1)
                    
    return provinciasDep

def getDistrito(Grafo, departamento, provincia):
    #Departamento = addDepartamentoString(Departamento)

    visited = []
    
    visited.append(startingNode)
    queue = getDepartamentos(Grafo)
        
    distritoDep = []
    
    """
    for departamento in queue:
        if departamento == Departamento:
            for nodosConectados in Grafo.edges(departamento):
                if nodosConectados[1] not in visited:
                    provinciasDep.append(nodosConectados[1])
    """  
                    
    while queue:
        item = queue.pop()
        
        if item not in visited:
        
            if item == departamento:
                for nodo0, nodo1 in Grafo.edges(item):
                    if tools.getTipoNodo(nodo1) == "Prov":
                        queue.append(nodo1)
            
            if item == provincia:
                print(item)
                for nodo0, nodo1 in Grafo.edges(item):
                    if tools.getTipoNodo(nodo1) == "Dis":
                        distritoDep.append(Grafo.nodes[nodo1]["Label"])            
            
            visited.append(item)
    
    return distritoDep