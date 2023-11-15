var listaDepartamentos = []
var listaProvincias = []
var listaDistritos = []

var departamentoBuscar = localStorage.getItem('DepartamentoSelecionado')
var provinciaBuscar = document.getElementById('selectProvincia')
var distritoBuscar = document.getElementById('selectDistrito')

async function requestDataServer(requestData){
   requestJSON = JSON.stringify(requestData)
   receivedJSON = await run(requestJSON)
   receivedJSON = JSON.parse(receivedJSON)

   return receivedJSON
}

async function requestDepartamentos(){
   requestJSONData = {
      "type": "listDepartamento",
      "Departamento": departamentoBuscar,
      "Provincia": "null",
      "Distrito": "null",
   };

   JSONdata = await requestDataServer(requestJSONData)

   console.log(JSONdata["departamentos"])

   var selectDepartamento = document.getElementById("selectDepartamento")

   /*
   for (i = 0; i < JSONdata["departamentos"].length; i++) {
      var departamentoTMP = document.createElement("option");
      departamentoTMP.text = JSONdata["departamentos"][i]
      console.log(JSONdata["departamentos"][i])
      selectDepartamento.add(departamentoTMP)
      listaDepartamentos.push(departamentoTMP)
   }
   */
   addItemsToSelect(selectDepartamento, listaDepartamentos, JSONdata["departamentos"])
}

function resetDepartamento(){
   for(var items in listaDepartamentos)
   {
      listaDepartamentos.remove()
      console.log(items)
   }
}

async function requestProvincia() {
   //Se cambia el departamento que depende del seleccionado
   requestJSONData = {
      "Departamento": departamentoBuscar,
      "Provincia": "NULL",
      "Distrito": "NULL",
   };

   JSONData = await requestDataServer(requestJSONData)

   console.log(JSONData["provincias"])

   var selectProvincia = document.getElementById("selectProvincia")

   addItemsToSelect(selectProvincia, listaProvincias, JSONData["provincias"])
}

async function requestDistrito() {
   //Se cambia el departamento que depende del seleccionado
   requestJSONData = {
      "type": "listDistrito",
      "Departamento": departamentoBuscar,
      "Provincia": "NULL",
      "Distrito": "NULL",
   };

   JSONData = await requestDataServer(requestJSONData)

   console.log(JSONData["distritos"])

   var selectDistrito = document.getElementById("selectDistrito")

   addItemsToSelect(selectDistrito, listaDistritos, JSONData["distritos"])
}

function addItemsToSelect(selectItem, listSelect, JSONData){
   for (var i = 0; i < JSONData.length; i++)
   {
      var optionTMP = document.createElement("option");
      optionTMP.text = JSONData[i]
      console.log(JSONData[i])
      selectItem.add(optionTMP)
      listSelect.push(optionTMP)
   }
}


//if (localStorage.getItem('DepartamentoSelecionado') == "null") {
//   requestDepartamentos()
//}

//requestProvincia()
//requestDistrito()

async function requestDatos(){
   requestJSONData = {
      "Departamento": departamentoBuscar,
      "Provincia": provinciaBuscar,
      "Distrito": distritoBuscar,
   };

   JSONdata = await requestDataServer(requestJSONData)

   addItemsToSelect(selectDepartamento, listaDepartamentos, JSONdata["listaDepartamentos"])
   addItemsToSelect(selectProvincia, listaProvincias, JSONdata["listaProvincias"])
   addItemsToSelect(selectDistrito, listaDistritos, JSONdata["listaDistritos"])

}

requestDatos()