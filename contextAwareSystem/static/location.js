if (navigator.geolocation) {
    var location_timeout = setTimeout("geolocFail()", 20000);

    navigator.geolocation.getCurrentPosition(function(position) {
        clearTimeout(location_timeout);

        var lat = position.coords.latitude;
        var lng = position.coords.longitude;

        console.log(lat, lng);
    }, function(error) {
        clearTimeout(location_timeout);
        geolocFail();
    });
} else {
    // Fallback for no geolocation
    geolocFail();
}

function geolocFail() {
	console.log("failed");
}