/* 
this file holds the maps and mapm views for the accountability sector
*/

// THE MAP SCRIPT FOR CREATING THE 2D MAP

require(["esri/Map", "esri/views/MapView"], function (Map, MapView) {
  var map = new Map({
    basemap: "topo-vector",
  });

  var view = new MapView({
    container: "viewDiv", // Reference to the DOM node that will contain the view
    map: map, // References the map object created in step 3
  });
});
