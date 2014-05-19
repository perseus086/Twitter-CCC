google.load("visualization", "1.1", {packages:["corechart"]});
 
google.setOnLoadCallback(getData);     



function getData(){
    $.getJSON(requestUrl+'/_design/time/_view/hours?group_level=1', 
        function(data) {
            drawTable(data);
        });
}

function drawTable(data){
    console.log(data)
	var table = new google.visualization.DataTable();
    
    table.addColumn('string', 'Hour');
    table.addColumn('number', 'Tweets');

    for(var i=0;i<data.rows.length; i++){
        table.addRow();
        table.setValue(i,0, data.rows[i].key);
        table.setValue(i,1, data.rows[i].value);
    }
  
    var options = {
          title: 'Tweets by hour',
          hAxis: {title: 'Hours'},
          width: '90%', 
          height: 500,
          vAxis: {maxValue: 2}
         
        };


  	var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
  	chart.draw(table,options);
} 