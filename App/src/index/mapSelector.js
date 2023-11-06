var a = document.getElementById("peruSvg")

//Lectura del archivo json
import data from '../../Assets/Lugares.json' assert {type: 'json'}

//Arreglo con lugares
var dataLugares = []

//Clase Lugar
class Lugar {
    constructor(nombre, id) {
        this.nombre = nombre;
        this.id = id;
    }

    setElement(elementId) {
        this.elementId = elementId
    }
}

//Ingreso de datos del arreglo
for(var i in data.Lugares){
    const LugarTMP = new Lugar(data.Lugares[i].Nombre, data.Lugares[i].id)
    dataLugares.push(LugarTMP)
}

//console.log(dataLugares)

//var lugares = [];
//for (var i in data) {
//    lugares.push(data[i]);
//    console.log(data)
//}
//console.log(lugares)

a.addEventListener("load", function () {

    var svgDoc = a.contentDocument;

    function elementByid(lugarObject) {

        if (typeof(lugarObject.id) == "string")
        {
            //console.log(lugarObject.id)

            var elementId = svgDoc.getElementById(lugarObject.id);
            lugarObject.setElement(elementId);
        }
        else
        {
            var arrElementByid = [];
            for(let i = 0; i < 2; i++)
            {
                //console.log(lugarObject.id[i]);
                var elementId = svgDoc.getElementById(lugarObject.id[i])
                arrElementByid.push(elementId)
            }
            lugarObject.setElement(arrElementByid)
            //for(var i in lugarObject.id.length){
            //    console.log("Object!")
            //}
        }
        //    console.log(lugarObject.id.at(i))
        
        //console.log(lugarObject.elementId)
        //var elementId = svgDoc.getElementById(lugarObject.id);
        //return elementId
    }

    function eventListener(lugarObject) {

        if (typeof (lugarObject.id) == "string") {
            lugarObject.elementId.addEventListener("mousedown", function () {
                console.log(lugarObject.nombre)
                localStorage.setItem('DepartamentoSelecionado', lugarObject.nombre)

                window.location.href = "src/search/search.html"
            })
            }
        else {
            for (let i = 0; i < 2; i++) {
                (lugarObject.elementId[i]).addEventListener("mousedown", function () {
                    alert(lugarObject.nombre)
                })
            }
            //for(var i in lugarObject.id.length){
            //    console.log("Object!")
            //}
        }
        //var elementId = lugarObject.getElementById()
        //lugarObject.getElementById().addEventListener("mousedown", function () {
        //    alert(lugarObject.getNombre());
        //}, false)
    }

    for(var i in dataLugares){
        console.log(dataLugares.at(i).nombre);
        elementByid(dataLugares.at(i));
        eventListener(dataLugares.at(i));
    }
    
    console.log(dataLugares)

    /*
    for(var indexTMP in dataLugares){
        for(var indexID in dataLugares[indexTMP]){
    
            dataLugares[indexTMP][indexID].addEventListener("mouesdown", function(){
                alert(dataLugares[indexTMP][indexID])
            })

        //for(var indexID in dataLugares[indexTMP]){
            //svgDoc.getElementById(dataLugares[indexTMP][indexID])
        //}
        }
    }
    */

    //var path7 = svgDoc.getElementById("path7");

    //path7.addEventListener("mousedown", function () {
    //    alert("Hello World");
    //}, false)

}, false)