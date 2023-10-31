var listaDepartamentos = []
var listaProvincias = []
var listaDistritos = []

async function requestDataServer(requestData){
   requestJSON = JSON.stringify(requestData)
   receivedJSON = await run(requestJSON)
   receivedJSON = JSON.parse(receivedJSON)

   return receivedJSON
}

async function requestDepartamentos(){
   requestJSONData = {
      "type": "listDepartamento",
      "Departamento": "NULL",
      "Provincia": "NULL",
      "Distrito": "NULL",
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

function requestProvincia() {
   //Se cambia el departamento que depende del seleccionado
   requestJSONData = {
      "type": "listProvincia",
      "Departamento": "NULL",
      "Provincia": "NULL",
      "Distrito": "NULL",
   };

   var selectProvincia = document.getElementById("selectProvincia")

}

function requestDistrito() {
   //Se cambia el departamento y provincia que depende del seleccionado


   var selectDistrito = document.getElementById("selectDistrito")

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

var provinciaId = document.getElementById("seccionProvincia");
var distritoId = document.getElementById("seccionDistrito");

requestDepartamentos()

resetDepartamento()