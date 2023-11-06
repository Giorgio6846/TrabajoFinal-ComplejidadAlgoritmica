import dis
from functools import update_wrapper
from math import dist
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
    distrito = distrito.split(".")
    distrito[0] = distrito[0].capitalize()
    distrito[1] = distrito[1].capitalize()
    distrito = '.'.join(distrito)
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
    elif re.search("Distrito.", string):
        return "Dis"
    elif re.search("Pais.", string):
        return "Pais"
    else:
        return "Calle"
    
def saveDepartamentosJSON(listDepartamentos):
    listDepartamentosTMP = []
    for item in listDepartamentos:
        departamento = removeDepartamentoString(item)
        listDepartamentosTMP.append(departamento)
        listDepartamentosTMP = sorted(listDepartamentosTMP)  
    return listDepartamentosTMP

def saveProvinciasJSON(listProvincias):
    listProvinciasTMP = []
    for item in listProvincias:
        provincia = removeProvinciaString(item)
        listProvinciasTMP.append(provincia)
        listProvinciasTMP = sorted(listProvinciasTMP)
    return listProvinciasTMP

def saveDistritosJSON(listDistritos):
    listDistrtosTMP = []
    for item in listDistritos:
        distrito = removeDistritoString(item)
        listDistrtosTMP.append(distrito)
        listDistrtosTMP = sorted(listDistrtosTMP)
    return listDistrtosTMP