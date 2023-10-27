import pandas as pd
import networkx as nx

nombrePais = "Pais.Peru"

df = pd.read_csv("../Generador/Dataframe.csv", index_col = False)
df = df.drop(columns=["Unnamed: 0"])
df

def loadGraph(Grafo):
    Grafo.add_node(nombrePais)    

    accessDepartamento(Grafo)
    nx.write_graphml_lxml(Grafo,"test1.graphml")
    
def accessDepartamento(Grafo):
    
    Departamentos = list(df["departamento"].unique())
    
    for departamento in Departamentos:
        dfDepartamento = df.iloc[list(df["departamento"] == departamento)]
        nombreDepartamento = "Departamento." + str(departamento)
        
        Grafo.add_node(nombreDepartamento)
        Grafo.add_edge(nombrePais, nombreDepartamento)
        
        accessProvincia(dfDepartamento, Grafo, departamento)

def accessProvincia(dfDepartamento, Grafo, departamento):
    Provincias = list(dfDepartamento["provincia"].unique())
    
    for provincia in Provincias: 
        dfProvincia = dfDepartamento.iloc[list(dfDepartamento["provincia"] == provincia)]
        
        nombreDepartamento = "Departamento." + str(departamento)
        nombreProvincia = "Provincia." + str(provincia)
        
        Grafo.add_node(nombreProvincia)
        Grafo.add_edge(nombreDepartamento, nombreProvincia)
        
        accessDistrito(dfProvincia, Grafo, provincia)

def accessDistrito(dfProvincia, Grafo, provincia):
    
    #dataFrameDistrito = dataFrameProvincia.iloc[list(dataFrameProvincia["provincia"] == provincia)]
    Distritos = list(dfProvincia["distrito"].unique())
    
    for distrito in Distritos: 
        dfDistrito = dfProvincia.iloc[list(dfProvincia["distrito"] == distrito)]
                
        nombreProvincia = "Provincia." + str(provincia)
        nombreDistrito = "Distrito." + str(distrito)
        
        Grafo.add_node(nombreDistrito)
        Grafo.add_edge(nombreProvincia, nombreDistrito)
        accessDireccion(dfDistrito, Grafo, distrito)

def accessDireccion(dataframeDistrito, Grafo, distrito):
    for index, row in dataframeDistrito.iterrows():
            nombreDistrito = "Distrito." + str(distrito)
        
            direccion = row["direccion"]
            Grafo.add_node(direccion)
            Grafo.add_edge(nombreDistrito, direccion)