/**
 * Created by mikedanylov on 9/9/15.
 */

function plot_selected(elem_id){

    var json_data = JSON.parse(document.getElementById("div_" + elem_id).innerHTML);
    var raw_measurements = json_data['mea_value'];
    var raw_datetime = json_data['mea_datetime'];
    var dataPoints = [];

    for (var i = 0; i < raw_datetime.length; i++){
        dataPoints.push({
            x : new Date(parseFloat(raw_datetime[i]) * 1000),
            y : parseFloat(raw_measurements[i])
        });
    }

    var chart_id = 'chart' + elem_id;
    //console.log('chart id is ' + chart_id);
    var chart = new CanvasJS.Chart(chart_id, {
        title : {
            text : "Sensor " + elem_id + " data"
        },
        axisX:{
            title: "Time"
        },
        axisY: {
            title: "Temperature"
        },
        data : [{
            type : "splineArea",
            xValueType: "dateTime",
            dataPoints : dataPoints
        }],
        zoomEnabled: true
     });
    chart.render();
}

function plot_realtime(elem_id, time_frame){

    // 1. Send request to server to get data
    // for chosen sensor within time frame

    $.ajax({
        type: 'post',
        url: '/realtime/',
        data: {
            sensor_id: elem_id,
            time_frame: time_frame
        },
        dataType: 'json',
        success: function (data){
            var new_data = JSON.stringify(data);
            var div_post = 'div_' + elem_id;
            document.getElementById(div_post).innerHTML = new_data;
            plot_selected(elem_id);
        },
        error: function (err) {
            console.log(data);
        }
    });

    //var yVal = 15, updateCount = 0;
    //var updateChart = function () {
    //
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