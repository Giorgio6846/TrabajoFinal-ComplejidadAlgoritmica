async function requestDataServer(requestData){
   requestJSON = JSON.stringify(requestData)
   receivedJSON = await run(requestJSON)
   receivedJSON = JSON.parse(receivedJSON)

   console.log(receivedJSON["departamentos"])

   listaDepartamentos = []

   var selectDepartamento = document.getElementById("selectDepartamento")

   for (i = 0; i < receivedJSON["departamentos"].length; i++)
   {
      var departamentoTMP = document.createElement("option");
      departamentoTMP.text = receivedJSON["departamentos"][i]
      console.log(receivedJSON["departamentos"][i])
      selectDepartamento.add(departamentoTMP)
      listaDepartamentos.push(departamentoTMP)
   }

   return receivedJSON
}

function requestDepartamentos(){
   requestDepartamentoData = {
      "type": "listDepartamento",
      "Departamento": "NULL",
      "Provincia": "NULL",
      "Distrito": "NULL",
   };

   requestDataServer(requestDepartamentoData)
}

function requestProvincia() {

}

function requestDistrito() {

}

var provinciaId = document.getElementById("seccionProvincia");
var distritoId = document.getElementById("seccionDistrito");

requestDepartamentos()