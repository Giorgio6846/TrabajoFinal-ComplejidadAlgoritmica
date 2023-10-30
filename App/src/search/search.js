function requestDataServer(requestData){
   requestJSON = JSON.stringify(requestData)
   receivedJSON = run(requestJSON)

   console.log(receivedJSON)

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

var departamentoId = document.getElementById("seccionDistrito");
var provinciaId = document.getElementById("seccionProvincia");
var distritoId = document.getElementById("seccionDistrito");

requestDepartamentos()