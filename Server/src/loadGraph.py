import pandas as pd
import platform

nombrePais = "Pais.Peru"

if platform.system() == "Windows":
    filePath = "./Server/Assets/Dataframe.csv"
elif platform.system() == "Darwin":
    filePath = "/Assets/Dataframe.csv"
else:
    filePath = "/Assets/Dataframe.csv"

df = pd.read_csv(filePath, index_col=False)
df = df.drop(columns=["Unnamed: 0"])


# df = pd.read_csv("/Assets/Dataframe.csv", index_col= False)


def accessDireccion(dataframeDistrito, Grafo, idDistrito):
    for index, row in dataframeDistrito.iterrows():
        direccion = row["direccion"]

        Grafo.add_node(direccion, **row.to_dict())
        # Grafo.nodes[direccion].update(row.to_dict())

        Grafo.add_edge(idDistrito, direccion)


def accessDistrito(dfProvincia, Grafo, provincia):
    Distritos = list(dfProvincia["distrito"].unique())

    for distrito in Distritos:
        dfDistrito = dfProvincia.iloc[list(dfProvincia["distrito"] == distrito)]

        nombreProvincia = "Provincia." + str(provincia)
        nombreDistrito = "Distrito." + str(distrito)
        idDistrito = "Distrito." + str(provincia) + "." + str(distrito)

        Grafo.add_node(idDistrito, **{"Label": nombreDistrito, "provincia": provincia})
        # Grafo.nodes[nombreDistrito]['provincia'].update(provincia)

        Grafo.add_edge(nombreProvincia, idDistrito)
        accessDireccion(dfDistrito, Grafo, idDistrito)


def accessProvincia(dfDepartamento, Grafo, departamento):
    Provincias = list(dfDepartamento["provincia"].unique())

    for provincia in Provincias:
        dfProvincia = dfDepartamento.iloc[
            list(dfDepartamento["provincia"] == provincia)
        ]

        nombreDepartamento = "Departamento." + str(departamento)
        nombreProvincia = "Provincia." + str(provincia)

        Grafo.add_node(
            nombreProvincia, **{"Label": nombreProvincia, "departamento": departamento}
        )

        Grafo.add_edge(nombreDepartamento, nombreProvincia)

        accessDistrito(dfProvincia, Grafo, provincia)


def accessDepartamento(Grafo):
    Departamentos = list(df["departamento"].unique())

    for departamento in Departamentos:
        dfDepartamento = df.iloc[list(df["departamento"] == departamento)]
        nombreDepartamento = "Departamento." + str(departamento)

        Grafo.add_node(nombreDepartamento)

        Grafo.add_edge(nombrePais, nombreDepartamento)

        accessProvincia(dfDepartamento, Grafo, departamento)


def loadGraph(Grafo):
    Grafo.add_node(nombrePais)

    accessDepartamento(Grafo)
