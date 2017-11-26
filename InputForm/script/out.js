'use strict';

google.charts.load('current', {'packages':['gauge']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {

        // Maximum Values of different Scores
        var max_Assistance = 1000;
        var max_Reliability = 100;
        var max_Popularity = 100;

        // Feeding data for each gauge
        var data1 = google.visualization.arrayToDataTable([
          ['Label', 'Value'],
          ['Assistance', max_Assistance]
        ]);

        var data2 = google.visualization.arrayToDataTable([
          ['Label', 'Value'],
          ['Reliability', max_Reliability]
        ]);

        var data3 = google.visualization.arrayToDataTable([
          ['Label', 'Value'],
          ['Popularity', max_Popularity]
        ]);

        // Feeding styling options for each gauge
        var options1 = {
          width: $("#AssistScore").width(), height: $("#AssistScore").height(),
          redFrom: 0, redTo: 400,
          greenFrom: 600, greenTo: 1000,
          yellowFrom:400, yellowTo: 600,
          animation:{
            duration: 3000,
            easing: 'out',
          },
          minorTicks: 5,
          max: max_Assistance
        };

        var options2 = {
          width: $("#RelyScore").width(), height: $("#RelyScore").height(),
          redFrom: 0, redTo: 15,
          greenFrom: 75, greenTo: 100,
          yellowFrom:50, yellowTo: 75,
          animation:{
            duration: 3000,
            easing: 'out',
          },
          minorTicks: 5,
          max: max_Reliability
        };

        var options3 = {
          width: $("#PopScore").width(), height: $("#PopScore").height(),
          redFrom: 0, redTo: 15,
          greenFrom: 75, greenTo: 100,
          yellowFrom:50, yellowTo: 75,
          animation:{
            duration: 3000,
            easing: 'out',
          },
          minorTicks: 5,
          max: max_Popularity
        };

        // Binding gauges to their corresponding divs
        var chart1 = new google.visualization.Gauge(document.getElementById('AssistScore'));
        var chart2 = new google.visualization.Gauge(document.getElementById('RelyScore'));
        var chart3 = new google.visualization.Gauge(document.getElementById('PopScore'));

        // Creating an illusion of animation
        data1.setValue(0, 1, 0);
        data2.setValue(0, 1, 0);
        data3.setValue(0, 1, 0);

        chart1.draw(data1, options1);
        chart2.draw(data2, options2);
        chart3.draw(data3, options3);

        // Setting Actual Values
        data1.setValue(0, 1, 40 + Math.round(600 * Math.random()));
        data2.setValue(0, 1, 40 + Math.round(60 * Math.random()));
        data3.setValue(0, 1, 40 + Math.round(60 * Math.random()));

        chart1.draw(data1, options1);
        chart2.draw(data2, options2);
        chart3.draw(data3, options3);

}
