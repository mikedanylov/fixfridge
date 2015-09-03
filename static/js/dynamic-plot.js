window.onload = function () {

    var now_date = new Date();
    var date_str = now_date.toString();
    // var dataPoints = [/*{y : 10}, {y : 13}, {y : 18}, {y : 20}, {y : 17}*/];
    var dataPoints = [];
    var chart = new CanvasJS.Chart("chartContainer", {
        title : {
            text : "Dynamic Data"
        },
        axisX:{
            title: "Time",
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

    var yVal = 15, updateCount = 0;
    var updateChart = function () {

        // get sensor data from database
        yVal = yVal + Math.round(5 + Math.random() * (-5 - 5));
        updateCount++;

        dataPoints.push({
            x : new Date(),
            y : yVal
        });

        chart.options.title.text = "Values displayed " + updateCount;
        chart.render();
    };

    // update chart every second
    setInterval(function(){updateChart()}, 1000);
}
