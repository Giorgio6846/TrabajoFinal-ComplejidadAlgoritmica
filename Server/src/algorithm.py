import src.loadGraph as lG

startingNode = "Pais.Peru"

def getDepartamentos(Grafo):
    listDepartamentos = []
    
    for departamentos in Grafo.edges(startingNode):
        listDepartamentos.append(departamentos[1])
        
    return listDepartamentos