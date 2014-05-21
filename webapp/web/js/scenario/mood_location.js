google.load("visualization", "1.1", {packages:["corechart"]});

google.setOnLoadCallback(chartsOnLoad);     



function chartsOnLoad(){
	getTypesCount();
}

var map = null;
var boundsRec = null;

function addSelectionRectangle(){
	var bounds = new google.maps.LatLngBounds(
      new google.maps.LatLng(-38.2607,144.3945),
      new google.maps.LatLng(-37.4598,145.7647)
  );

  // Define the rectangle and set its editable property to true.
  boundsRec = new google.maps.Rectangle({
    bounds: bounds,
    editable: true,
    draggable: true,
    fillOpacity: 0.08
  });

  boundsRec.setMap(map);
  google.maps.event.addListener(boundsRec, 'bounds_changed', updateBounds);
}

function updateBounds(){
 	getTypesCount();
}

function getTypesCount(){
	var ne = boundsRec.getBounds().getNorthEast();
 	var sw = boundsRec.getBounds().getSouthWest();
 	var bounds =sw.lng()+','+sw.lat()+','+ne.lng()+','+ne.lat();
	$.getJSON(requestUrl+'/_design/geo/_spatial/happy?bbox='+bounds+'&count=true', 
	function(dataHappy) {
		$.getJSON(requestUrl+'/_design/geo/_spatial/sad?bbox='+bounds+'&count=true', 
		function(dataSad) {
			drawTable(dataHappy,dataSad);
		});
		
	});
}

function drawTable(dataHappy,dataSad){
	var table = new google.visualization.DataTable();
    
    table.addColumn('string', 'Mood');
    table.addColumn('number', 'Tweets');

    // for(var i=0;i<data.rows.length; i++){
        table.addRow();
        table.setValue(0,0, 'positive');
        table.setValue(0,1, dataHappy.count);

        table.addRow();
        table.setValue(1,0, 'negative');
        table.setValue(1,1, dataSad.count);

        // table.addRow();
        // table.setValue(2,0, 'relation');
        // table.setValue(2,1, (dataHappy.count/dataSad.count)*1000);
    // }
  
    var options = {
      title: '',
      hAxis: {title: 'Mood'},
      width: '90%', 
      height: 500,
      vAxis: {maxValue: 2}
     
    };


  	// var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
  	var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
  	
  	chart.draw(table,options);
} 

$(document).ready(function(){

	var mapOptions = {
		zoom: 9,
	    center: new google.maps.LatLng(-37.793472,144.995804),
	    mapTypeId: google.maps.MapTypeId.ROADMAP
	};

	map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

	addSelectionRectangle();

});