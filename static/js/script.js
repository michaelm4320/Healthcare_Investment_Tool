// PROFILE DROPDOWN
const profile = document.querySelector('nav .profile');
const imgProfile = profile.querySelector('img');
const dropdownProfile = profile.querySelector('.profile-link');

imgProfile.addEventListener('click', function () {
	dropdownProfile.classList.toggle('show');
})

// APEXCHART
var options = {
  series: [{
  name: test[4],
  data: [31, 40, 28, 51, 42, 109, 100]
}, {
  name: 'series2',
  data: [11, 32, 45, 32, 34, 52, 41]
}],
  chart: {
  height: 350,
  type: 'area'
},
dataLabels: {
  enabled: false
},
stroke: {
  curve: 'smooth'
},
xaxis: {
  type: 'datetime',
  categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z", "2018-09-19T04:30:00.000Z", "2018-09-19T05:30:00.000Z", "2018-09-19T06:30:00.000Z"]
},
tooltip: {
  x: {
    format: 'dd/MM/yy HH:mm'
  },
},
};

console.log(test)

var chart = new ApexCharts(document.querySelector("#chart"), options);
chart.render();

var AGEoptions = {
          series: [{
          name: 'Ages',
          data: [12, 10, 30, 35, 20]
        }],
          chart: {
          type: 'bar',
          height: 600
        },
        plotOptions: {
          bar: {
            horizontal: false,
            columnWidth: '55%',
            endingShape: 'rounded'
          },
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          show: true,
          width: 2,
          colors: ['transparent']
        },
        xaxis: {
          categories: ['0-20', '20-40', '40-60', '60-80', '80-100'],
           title: {
                text: 'Age Group'
            }
        },
        yaxis: {
          title: {
            text: 'Hearing Infections'
          }
        },
        fill: {
          opacity: 1
        },
        tooltip: {
          y: {
            formatter: function (val) {
              return "# " + val + " hearing infections"
            }
          }
        }
        };

        var ageChart = new ApexCharts(document.querySelector("#age-chart"), AGEoptions);
        ageChart.render();

        var INSURANCEoptions = {
          series: [44, 55, 13, 43, 22, 30, 50, 21, 41],
          chart: {
          width: 700,
          type: 'pie',
        },
        labels: ['Medicare', 'Medicaid', 'Dual Eligible', 'Humana', 'Blue Cross Blue Shield', 'United Healthcare', 'Aetna', 'Cigna Health', 'Anthem'],
        responsive: [{
          breakpoint: 480,
          options: {
            chart: {
              width: 200
            },
            legend: {
              position: 'bottom'
            }
          }
        }]
        };

        var INSURANCEchart = new ApexCharts(document.querySelector("#insurance-chart"), INSURANCEoptions);
        INSURANCEchart.render();