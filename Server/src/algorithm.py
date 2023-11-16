import src.tools as tools

startingNode = "Pais.Peru"


def getProvincia(Grafo, Departamento):
    # Departamento = addDepartamentoString(Departamento)
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
                    listDatos.append(
                        Grafo.nodes[node1]["provincia"]
                        + "."
                        + Grafo.nodes[node1]["Label"]
                    )
            elif Nivel == 4:
                if tipoNodo == "Dep" or tipoNodo == "Prov" or tipoNodo == "Dis":
                    if node1 not in visited:
                        queue.append(node1)
                elif tipoNodo == "Calle":
                    listDatos.append(node1)

        visited.append(item)

    return listDatos


def getDistritoD(Grafo, departamento):
    visited = []

    visited.append(startingNode)
    queue = getAll(Grafo, 1)

    distritoDep = []

    while queue:
        item = queue.pop()

        if item not in visited:
            if item == departamento:
                for nodo0, nodo1 in Grafo.edges(item):
                    if tools.getTipoNodo(nodo1) == "Prov":
                        queue.append(nodo1)

            for nodo0, nodo1 in Grafo.edges(item):
                if tools.getTipoNodo(nodo1) == "Dis":
                    distritoDep.append(
                        Grafo.nodes[nodo1]["provincia"]
                        + "."
                        + Grafo.nodes[nodo1]["Label"]
                    )

            visited.append(item)

    print(distritoDep)
    return distritoDep


def getCallesD(Grafo, Departamento):
    listCalles = []
    visited = []

    queue = getAll(Grafo, 1)

    while queue:
        item = queue.pop()

        if item not in visited:
            if item == Departamento:
                for nodo0, nodo1 in Grafo.edges(item):
                    if tools.getTipoNodo(nodo1) == "Prov":
                        queue.append(nodo1)

            for nodo0, nodo1 in Grafo.edges(item):
                if tools.getTipoNodo(nodo1) == "Dis":
                    queue.append(nodo1)
                if tools.getTipoNodo(nodo1) == "Calle":
                    dictTMP = {
                        "Calle": Grafo.nodes[nodo1]["direccion"],
                        "Departamento": Grafo.nodes[nodo1]["departamento"],
                        "Provincia": Grafo.nodes[nodo1]["provincia"],
                        "Distrito": Grafo.nodes[nodo1]["distrito"],
                        "Tipo de Vivienda": Grafo.nodes[nodo1]["tipoVivienda"],
                        "Cantidad Cuartos": Grafo.nodes[nodo1]["cuartos"],
                        "Material pared": Grafo.nodes[nodo1]["material_paredes"],
                        "Material techo": Grafo.nodes[nodo1]["material_techo"],
                    }
                    # print(dictTMP)
                    listCalles.append(dictTMP)
            visited.append(item)

    return listCalles


def getDistritoP(Grafo, provincia):
    # Departamento = addDepartamentoString(Departamento)

    visited = []

    visited.append(startingNode)
    queue = getAll(Grafo, 1)

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
            if item == provincia:
                print(item)
                for nodo0, nodo1 in Grafo.edges(item):
                    if tools.getTipoNodo(nodo1) == "Dis":
                        distritoDep.append(
                            Grafo.nodes[nodo1]["provincia"]
                            + "."
                            + Grafo.nodes[nodo1]["Label"]
                        )

            for nodo0, nodo1 in Grafo.edges(item):
                if (
                    tools.getTipoNodo(nodo1) == "Dep"
                    or tools.getTipoNodo(nodo1) == "Prov"
                ):
                    queue.append(nodo1)

            visited.append(item)

    return distritoDep


def getDistritoDP(Grafo, departamento, provincia):
    # Departamento = addDepartamentoString(Departamento)

    visited = []

    visited.append(startingNode)
    queue = getAll(Grafo, 1)

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
                        distritoDep.append(
                            Grafo.nodes[nodo1]["provincia"]
                            + "."
                            + Grafo.nodes[nodo1]["Label"]
                        )

            visited.append(item)

    return distritoDep


def getCalles(Grafo):
    listCalles = []
    visited = []

    queue = getAll(Grafo, 1)

    while queue:
        item = queue.pop()

        if item not in visited:
            for nodo0, nodo1 in Grafo.edges(item):
                if tools.getTipoNodo(nodo1) != "Calle":
                    queue.append(nodo1)
                else:
                    dictTMP = {
                        "Calle": Grafo.nodes[nodo1]["direccion"],
                        "Departamento": Grafo.nodes[nodo1]["departamento"],
                        "Provincia": Grafo.nodes[nodo1]["provincia"],
                        "Distrito": Grafo.nodes[nodo1]["distrito"],
                        "Tipo de Vivienda": Grafo.nodes[nodo1]["tipoVivienda"],
                        "Cantidad Cuartos": Grafo.nodes[nodo1]["cuartos"],
                        "Material pared": Grafo.nodes[nodo1]["material_paredes"],
                        "Material techo": Grafo.nodes[nodo1]["material_techo"],
                    }
                    # print(dictTMP)
                    listCalles.append(dictTMP)
            visited.append(item)

    return listCalles
