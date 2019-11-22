/* global mapboxgl */


let places = [{
        'name': "EnviroD Space @ PLQ",
        'position': [103.8937, 1.3180],
        'link': 'https://goo.gl/maps/sdzDJvGw77TWBk5X8',
        'description': "10 Paya Lebar Rd, #05-01/02, Singapore 409057"
    },
    {
        'name': "EnviroD Space @ 313",
        'position': [103.8384, 1.3009],
        'link': 'https://goo.gl/maps/5KUbvCQT1ZBjRLwFA',
        'description': "313 Orchard Rd, #06-11/12/13, Singapore 238895"
    },
    {
        'name': 'EnviroD Space @ Junction 8',
        'position': [103.8486, 1.3505],
        'link': 'https://goo.gl/maps/An9c9qNZkw1P91dq8',
        'description': "9 Bishan Pl, #05-23/24, Singapore 579837"
    }
]

mapboxgl.accessToken = "pk.eyJ1IjoiZGl5YW5haDA4IiwiYSI6ImNrMHlwam9pNzBoc2QzYnA4ZXgydXFvY2cifQ.5Ou3JPEXHCQOJ-0H4Blltw";

let mapOptions = {
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11', 
    center: [103.8198, 1.3521], 
    zoom: 11, 
};
let map = new mapboxgl.Map(mapOptions);

// Create a Marker
for (let each_place of places) {
    let m = new mapboxgl.Marker();
    let p = new mapboxgl.Popup({
        offset: 25
    });
    m.setLngLat(each_place.position);
    p.setHTML(`<h5>${each_place.name}</h5>
                <p>${each_place.description}</p>
                <a href = "${each_place.link}" target="_blank" class = "direction">Directions</a>`);
    m.setPopup(p);
    m.addTo(map);
}