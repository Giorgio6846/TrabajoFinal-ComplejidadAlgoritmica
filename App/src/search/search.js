var listaDepartamentos = []
var listaProvincias = []
var listaDistritos = []

async function requestDataServer(requestData){
   requestJSON = JSON.stringify(requestData)
   receivedJSON = await run(requestJSON)
   receivedJSON = JSON.parse(receivedJSON)

   return receivedJSON
}

function removeOptions(selectElement) {
   console.log(selectElement.options.length)

   //var i, L = selectElement.options.length - 1;
   //for (i = L; i >= 0; i--) {
   //   selectElement.remove(i);
   //}
}

function addItemsToSelect(selectItem, listSelect, JSONData){
   for (var i = 0; i < JSONData.length; i++)
   {
      var optionTMP = document.createElement("option");
      optionTMP.text = JSONData[i]
      //console.log(JSONData[i])
      selectItem.add(optionTMP)
      listSelect.push(optionTMP)
   }
}

async function requestDatos(){
   //removeOptions(document.getElementById("selectDepartamento"))
   //removeOptions(document.getElementById("selectProvincia"))
   //removeOptions(document.getElementById("selectDistrito"))

   var departamentoBuscar = localStorage.getItem('DepartamentoSelecionado')
   var provinciaBuscar = localStorage.getItem('ProvinciaSelecionado')
   var distritoBuscar = localStorage.getItem('DistritoSelecionado')

   requestJSONData = {
      "Departamento": departamentoBuscar,
      "Provincia": provinciaBuscar,
      "Distrito": distritoBuscar,
   };

   console.log(requestJSONData)

   JSONdata = await requestDataServer(requestJSONData)

   addItemsToSelect(selectDepartamento, listaDepartamentos, JSONdata["listaDepartamentos"])
   addItemsToSelect(selectProvincia, listaProvincias, JSONdata["listaProvincias"])
   addItemsToSelect(selectDistrito, listaDistritos, JSONdata["listaDistritos"])

   let table = document.querySelector("table")
   clearTable(table)
   generateTable(table, JSONdata["listCalles"])
}

function generateTable(table, data){
   for (let element of data) {
      let row = table.insertRow();
      for (key in element) {
         let cell = row.insertCell();
         let text = document.createTextNode(element[key]);
         cell.appendChild(text);
      }
   }
}

function clearTable(table){
   for(var i = 1; i < table.rows.length;){
      table.deleteRow(i)
   }
}

requestDatos()
