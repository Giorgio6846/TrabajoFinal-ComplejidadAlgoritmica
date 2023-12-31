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

def getCalles(Grafo, messageJSON):
    listCalles = []
    visited = []

    queue = getAll(Grafo, 1)

    while queue:
        item = queue.pop()

        if item not in visited:
            if tools.getTipoNodo(item) == "Dep":
                if messageJSON["Departamento"] == None:
                    for nodo0, nodo1 in Grafo.edges(item):
                        if item not in visited:
                            queue.append(nodo1)

                elif tools.addDepartamentoString(messageJSON["Departamento"]) == item:
                    for nodo0, nodo1 in Grafo.edges(item):
                        if item not in visited:
                            queue.append(nodo1)

            elif tools.getTipoNodo(item) == "Prov":
                if messageJSON["Provincia"] == None:
                    for nodo0, nodo1 in Grafo.edges(item):
                        if item not in visited:
                            queue.append(nodo1)

                elif tools.addProvinciaString(messageJSON["Provincia"]) == item:
                    for nodo0, nodo1 in Grafo.edges(item):
                        if item not in visited:
                            queue.append(nodo1)

            elif tools.getTipoNodo(item) == "Dis":
                if messageJSON["Distrito"] == None:
                    for nodo0, nodo1 in Grafo.edges(item):
                        if item not in visited:
                            queue.append(nodo1)

                elif tools.addDistritoString(messageJSON["Distrito"]) == item:
                    for nodo0, nodo1 in Grafo.edges(item):
                        if item not in visited:
                            queue.append(nodo1)

            elif tools.getTipoNodo(item) == "Calle":
                dictTMP = {
                    "Calle": Grafo.nodes[item]["direccion"],
                    "Departamento": Grafo.nodes[item]["departamento"],
                    "Provincia": Grafo.nodes[item]["provincia"],
                    "Distrito": Grafo.nodes[item]["distrito"],
                    "Tipo de Vivienda": Grafo.nodes[item]["tipoVivienda"],
                    "Cantidad Cuartos": Grafo.nodes[item]["cuartos"],
                    "Material pared": Grafo.nodes[item]["material_paredes"],
                    "Material techo": Grafo.nodes[item]["material_techo"],
                    "Material piso": Grafo.nodes[item]["material_piso"],
                }

                listCalles.append(dictTMP)

            visited.append(item)

    return listCalles

def getDistrito(Grafo, messageJSON):
    visited = []

    visited.append(startingNode)
    queue = getAll(Grafo, 1)

    distritoList = []

    while queue:
        item = queue.pop()

        if item not in visited:
            if tools.getTipoNodo(item) == "Dep":
                if messageJSON["Departamento"] == None:
                    for nodo0, nodo1 in Grafo.edges(item):
                        if item not in visited:
                            queue.append(nodo1)

                elif tools.addDepartamentoString(messageJSON["Departamento"]) == item:
                    for nodo0, nodo1 in Grafo.edges(item):
                        if item not in visited:
                            queue.append(nodo1)

            elif tools.getTipoNodo(item) == "Prov":
                if messageJSON["Provincia"] == None:
                    for nodo0, nodo1 in Grafo.edges(item):
                        if item not in visited:
                            queue.append(nodo1)

                elif tools.addProvinciaString(messageJSON["Provincia"]) == item:
                    for nodo0, nodo1 in Grafo.edges(item):
                        if item not in visited:
                            queue.append(nodo1)

            elif tools.getTipoNodo(item) == "Dis":
                distritoList.append(
                    Grafo.nodes[item]["provincia"] + "." + Grafo.nodes[item]["Label"]
                )

        visited.append(item)

    return distritoList

def getAllCalles(Grafo):
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
                        "Material piso": Grafo.nodes[nodo1]["material_piso"],
                    }
                    # print(dictTMP)
                    listCalles.append(dictTMP)
            visited.append(item)

    return listCalles


def getStats(list):
    dictVivienda = {}
    dictParedes = {}
    dictTecho = {}
    dictPiso = {}

    for index in list:
        if index["Tipo de Vivienda"] in dictVivienda:
            dictVivienda[index["Tipo de Vivienda"]] += 1
        else:
            dictVivienda[index["Tipo de Vivienda"]] = 1

        if index["Material pared"] in dictParedes:
            dictParedes[index["Material pared"]] += 1
        else:
            dictParedes[index["Material pared"]] = 1

        if index["Material techo"] in dictTecho:
            dictTecho[index["Material techo"]] += 1
        else:
            dictTecho[index["Material techo"]] = 1

        if index["Material piso"] in dictPiso:
            dictPiso[index["Material piso"]] += 1
        else:
            dictPiso[index["Material piso"]] = 1

    return dictVivienda, dictParedes, dictTecho, dictPiso
