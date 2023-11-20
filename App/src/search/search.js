var listaDepartamentos = []
var listaProvincias = []
var listaDistritos = []

async function requestDataServer(requestData){
   requestJSON = JSON.stringify(requestData)
   receivedJSON = await run(requestJSON)
   receivedJSON = JSON.parse(receivedJSON)

   return receivedJSON
}

async function addItemsToSelect(selectItem, listSelect, JSONData){
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

   graficoVivienda = updateChart(JSONdata["listStats"]["statsViviendas"], 'chartViviendas', 'Estadisticas de Viviendas', graficoVivienda);
   graficoParedes = updateChart(JSONdata["listStats"]["statsParedes"], 'chartParedes', 'Estadisticas de Paredes', graficoParedes);
   graficoTechos = updateChart(JSONdata["listStats"]["statsTecho"], 'chartTecho', 'Estadisticas de Techo', graficoTechos);
   graficoPisos = updateChart(JSONdata["listStats"]["statsPiso"], 'chartPiso', 'Estadisticas de Piso', graficoPisos);
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


function calcularPorcentajes(stats) {
    const total = Object.values(stats).reduce((acc, val) => acc + val, 0);
    const porcentajes = {};
    for (const key in stats) {
        porcentajes[key] = ((stats[key] / total) * 100).toFixed(2);
    }
    return porcentajes;
}

function updateChart(stats, chartId, chartLabel, myChart) {
   const porcentajes = calcularPorcentajes(stats);

   const ctx = document.getElementById(chartId).getContext('2d');

   if (myChart) {
       myChart.destroy();
   }

   return new Chart(ctx, {
       type: 'bar',
       data: {
           labels: Object.keys(porcentajes),
           datasets: [{
               label: chartLabel,
               data: Object.values(porcentajes),
               backgroundColor: [
                   'rgba(255, 99, 132, 0.2)',
                   'rgba(54, 162, 235, 0.2)',
                   'rgba(255, 206, 86, 0.2)',
               ],
               borderColor: [
                   'rgba(255, 99, 132, 1)',
                   'rgba(54, 162, 235, 1)',
                   'rgba(255, 206, 86, 1)',
               ],
               borderWidth: 1
           }]
       },
       options: {
           scales: {
               y: {
                   beginAtZero: true
               }
           }
       }
   });
} 


let graficoVivienda;
let graficoTechos;
let graficoParedes;
let graficoPisos;

requestDatos()
