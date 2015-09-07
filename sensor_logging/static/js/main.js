/**
 * Created by mikedanylov on 9/5/15.
 */

//window.onload = function(){
//    ajax_request("measurements_div", "static/measurements.txt");
//    ajax_request("datetime_div", "static/datetime.txt");
//}

function plot_selected(){

    var dataPoints = [];

    var raw_measurements = document.getElementById("measurements_div").innerHTML.split(' ');
    raw_measurements.pop();
    var raw_datetime = document.getElementById("datetime_div").innerHTML.split(' ');
    raw_datetime.pop();

    for (var i = 0; i < raw_datetime.length; i++){
        dataPoints.push({
            x : new Date(parseFloat(raw_datetime[i]) * 1000),
            y : parseFloat(raw_measurements[i])
        });
    }

    var chart = new CanvasJS.Chart("chartContainer", {
        title : {
            text : "Sensor logs"
        },
        axisX:{
            title: "Time"
        },
        axisY: {
            title: "Temperature"
        },
        data : [{
            type : "spline",
            xValueType: "dateTime",
            dataPoints : dataPoints
        }]
     });

    chart.render();

    //var yVal = 15, updateCount = 0;
    //var updateChart = function () {
    //
    //    // get sensor data from database
    //    yVal = yVal + Math.round(5 + Math.random() * (-5 - 5));
    //    updateCount++;
    //
    //    dataPoints.push({
    //        x : new Date(),
    //        y : yVal
    //    });
    //
    //    chart.options.title.text = "Values displayed " + updateCount;
    //    chart.render();
    //};
    //
    // //update chart every second
    //setInterval(function(){updateChart()}, 1000);
}

function ajax_request(div, file){
    var xmlhttp;
    if (window.XMLHttpRequest){
        xmlhttp = new XMLHttpRequest();
    }
    else{
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange=function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
          document.getElementById(div).innerHTML = xmlhttp.responseText;
        }
    }
    xmlhttp.open("POST",file,true);
    xmlhttp.send();
}
