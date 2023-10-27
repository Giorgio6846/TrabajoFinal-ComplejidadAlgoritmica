function requestDataServer(){
   requestData = {
    "tipo": "Status",
    "Departamento": "NULL",
    "Provincia": "NULL",
    "Distrito": "NULL",
   };

   requestJSON = JSON.stringify(requestData)

   console.log(requestJSON);

   console.log(serverCOMS(requestJSON))
}