import re

def removeDepartamentoString(departamento):
    departamento = departamento.replace("Departamento.","")
    departamento = str.capitalize(departamento)
    return departamento

def removeProvinciaString(provincia):
    provincia = provincia.replace("Provincia.","")
    provincia = str.capitalize(provincia)
    return provincia

def removeDistritoString(distrito):
    distrito = distrito.replace("Distrito.","")
    distrito = str.capitalize(distrito)
    return distrito

def addDepartamentoString(departamento):
    departamentoTMP = "Departamento." + str.upper(departamento)
    return departamentoTMP

def addProvinciaString(provincia):
    provinciaTMP = "Provincia." + str.upper(provincia)
    return provinciaTMP

def addDistritoString(distrito):
    distritoTMP = "Distrito." + str.upper(distrito)
    return distritoTMP

def getTipoNodo(string):
    if re.search("Departamento.", string):
        return "Dep"
    elif re.search("Provincia.", string):
        return "Prov"
    elif re.search("Distrito..", string):
        return "Dis"
    
def saveDepartamentosJSON(listDepartamentos):
    listDepartamentosTMP = []
    for departamento in listDepartamentos:
        departamento = removeDepartamentoString(departamento)
        listDepartamentosTMP.append(departamento)
        listDepartamentosTMP = sorted(listDepartamentosTMP)  
    return listDepartamentosTMP

def saveProvinciasJSON(listProvincias):
    listProvinciasTMP = []
    for provincia in listProvincias:
        provincia = removeProvinciaString(provincia)
        listProvinciasTMP.append(provincia)
        listProvinciasTMP = sorted(listProvinciasTMP)
    return listProvinciasTMP

def saveDistritosJSON(listDistritos):
    listDistrtosTMP = []
    for distrito in listDistritos:
        distrito = removeDistritoString(distrito)
        listDistrtosTMP.append(distrito)
        listDistrtosTMP = sorted(listDistrtosTMP)
    return listDistrtosTMP