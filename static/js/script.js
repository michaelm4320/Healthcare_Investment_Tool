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
          data: city
        }],
          chart: {
          type: 'bar',
          height: 500
        },
        plotOptions: {
          bar: {
            borderRadius: 4,
            horizontal: true,
          }
        },
        dataLabels: {
          enabled: false
        },
       xaxis: {
    categories: ['Fort Myers', 'Jacksonville', 'Miami', 'Orlando', 'Tampa'],
    labels: {
      style: {
        fontSize: '15px',
      }
    },
    title: {
      text: 'Number of Ear Infections',
      style: {
        fontSize: '19px',
      }
    }
  },
  yaxis: {
    labels: {
      style: {
        fontSize: '15px',
      }
    },
    title: {
      text: 'Cities',
      style: {
        fontSize: '19px',
      }
    }
  }
};

        var chart = new ApexCharts(document.querySelector("#chart"), options);
        chart.render();

var AGEoptions = {
          series: [{
          name: 'Ages',
          data: [ages[0], ages[1], ages[2], ages[3], ages[4], ages[5], ages[6]]
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
          categories: ['0-15', '16-30', '31-45', '46-60', '61-75', '76-90', '91-110'],
          labels: {
      style: {
        fontSize: '15px',
      }
    },
           title: {
                text: 'Age Group',
                style: {
        fontSize: '19px',
      }
            }
        },
        yaxis: {
        labels: {
      style: {
        fontSize: '15px',
      }
    },
          title: {
            text: 'Number of Ear Infections',
style: {
        fontSize: '19px',
      }
          }
        },
        fill: {
          opacity: 1
        },
        tooltip: {
          y: {
            formatter: function (val) {
              return "# " + val + " ear infections"
            }
          }
        }
        };

        var ageChart = new ApexCharts(document.querySelector("#age-chart"), AGEoptions);
        ageChart.render();

        var INSURANCEoptions = {
          series: insurance,
          chart: {
          width: 700,
          type: 'pie',
        },
        labels: ['Aetna', 'Anthem', 'Blue Cross Blue Shield', 'Cigna Health', 'Humana', 'Medicaid', 'NO_INSURANCE', 'UnitedHealthcare'],
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