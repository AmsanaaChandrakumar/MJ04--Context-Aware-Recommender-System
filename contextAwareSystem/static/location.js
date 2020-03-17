var geocoder;

initialize()
if (navigator.geolocation) {
	navigator.geolocation.getCurrentPosition(successFunction, errorFunction);
} 
//Get the latitude and the longitude;
function successFunction(position) {
    var lat = position.coords.latitude;
    var lng = position.coords.longitude;
    codeLatLng(lat, lng)
}

function errorFunction(){
	alert("Geocoder failed");
}

function initialize() {
	geocoder = new google.maps.Geocoder();
	console.log("in tuna2")
}

function codeLatLng(lat, lng) {

var latlng = new google.maps.LatLng(lat, lng);
  geocoder.geocode({'latLng': latlng}, function(results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
    console.log(results)
      if (results[1]) {
      //formatted address
      // alert(results[0].formatted_address)
      //find country name
      for (var i=0; i<results[0].address_components.length; i++) {
        for (var b=0;b<results[0].address_components[i].types.length;b++) {
          if (results[0].address_components[i].types[b] == "locality") {
            city= results[0].address_components[i];
            break;
          }
        }
      }
      //city name
      document.getElementById("location").innerHTML = "Trending in " + city.long_name;

      fetch('/cityWeather', {
        method: 'POST',
        body: JSON.stringify({
          "city": city.long_name
        })
      }).then(function (response) {
        return response.text();
      }).then(function (text) {
        var weatherData = JSON.parse(text)
        document.getElementById("temperature").innerHTML = weatherData.main.temp;
        console.log('Temperature: ');
        console.log(weatherData.main.temp);
        console.log('Wind Speed: ');
        console.log(weatherData.wind.speed);
        console.log('Description: ');
        console.log(weatherData.weather[0].description);
        console.log('Icon: ');
        console.log(weatherData.weather[0].icon);
      });

      } else {
        alert("No results found");
      }
    } else {
      alert("Geocoder failed due to: " + status);
    }
  });
}

