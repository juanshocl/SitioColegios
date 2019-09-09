var chile = {
    "regiones": [{
        "region": "Región Metropolitana de Santiago",
        "comunas": ["Cerrillos", "Cerro Navia", "Conchalí", "El Bosque", "Estación Central", "Huechuraba", "Independencia", "La Cisterna", "La Florida", "La Granja", "La Pintana", "La Reina", "Las Condes", "Lo Barnechea", "Lo Espejo", "Lo Prado", "Macul", "Maipú", "Ñuñoa", "Pedro Aguirre Cerda", "Peñalolén", "Providencia", "Pudahuel", "Quilicura", "Quinta Normal", "Recoleta", "Renca", "San Joaquín", "San Miguel", "San Ramón", "Vitacura", "Puente Alto", "Pirque", "San José de Maipo", "Colina", "Lampa", "Tiltil", "San Bernardo", "Buin", "Calera de Tango", "Paine", "Melipilla", "Alhué", "Curacaví", "María Pinto", "San Pedro", "Talagante", "El Monte", "Isla de Maipo", "Padre Hurtado", "Peñaflor"]
        }]
    }

var txtRegion = document.getElementById("txtRegion")
var txtCity = document.getElementById("txtCity")

for(let i in chile.regiones) {
    let option = document.createElement("option")
    option.innerHTML = chile.regiones[i].region;
    txtRegion.appendChild(option)
}

function selectCity() {
    console.log("chilito")
    let cities = []
    txtCity.innerHTML = ""
    cities = chile.regiones.filter( function( region ) {
        return region.region == txtRegion.value
    } )
    for(let i in cities[0].comunas) {
        let option = document.createElement("option")
        option.innerHTML = cities[0].comunas[i];       
        txtCity.appendChild(option)
    }
}