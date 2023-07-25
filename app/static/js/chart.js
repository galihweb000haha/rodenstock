//======================HASIL PREDIKSI=========================//
var options = {
    series: [{
    name: 'PRODUCT A',
    data: [44, 55, 41, 67, 22, 43, 21, 49]
  }, {
    name: 'PRODUCT B',
    data: [13, 23, 20, 8, 13, 27, 33, 12]
  }, {
    name: 'PRODUCT C',
    data: [11, 17, 15, 15, 21, 14, 15, 13]
  }],
    chart: {
    type: 'bar',
    height: 350,
    stacked: true,
    stackType: '100%'
  },
  responsive: [{
    breakpoint: 480,
    options: {
      legend: {
        position: 'bottom',
        offsetX: -10,
        offsetY: 0
      }
    }
  }],
  xaxis: {
    categories: ['2011 Q1', '2011 Q2', '2011 Q3', '2011 Q4', '2012 Q1', '2012 Q2',
      '2012 Q3', '2012 Q4'
    ],
  },
  fill: {
    opacity: 1
  },
  legend: {
    position: 'right',
    offsetX: 0,
    offsetY: 50
  },
  };

  var chart = new ApexCharts(document.querySelector(".chart_hasil_prediksi_relevansi"), options);
  chart.render();
//======================PRESTASI THD PREDIKSI=========================//
var options = {
    series: [
    {
      type: 'boxPlot',
      data: [
        {
          x: 'Jan 2015',
          y: [54, 66, 69, 75, 88]
        },
        {
          x: 'Jan 2016',
          y: [43, 65, 69, 76, 81]
        },
      ]
    }
  ],
    chart: {
    type: 'boxPlot',
    height: 350
  },
  title: {
    text: 'Basic BoxPlot Chart',
    align: 'left'
  },
  plotOptions: {
    boxPlot: {
      colors: {
        upper: '#5C4742',
        lower: '#A5978B'
      }
    }
  }
  };

  var chart = new ApexCharts(document.querySelector(".chart_korelasi_prestasi_terhadap_prediksi"), options);
  chart.render();
//======================PRESTASI THD ORGANISASI=========================//
var options = {
    series: [
    {
      type: 'boxPlot',
      data: [
        {
          x: 'Jan 2015',
          y: [54, 66, 69, 75, 88]
        },
        {
          x: 'Jan 2016',
          y: [43, 65, 69, 76, 81]
        },
      ]
    }
  ],
    chart: {
    type: 'boxPlot',
    height: 350
  },
  title: {
    text: 'Basic BoxPlot Chart',
    align: 'left'
  },
  plotOptions: {
    boxPlot: {
      colors: {
        upper: '#5C4742',
        lower: '#A5978B'
      }
    }
  }
  };

  var chart = new ApexCharts(document.querySelector(".chart_korelasi_organisasi_terhadap_prediksi"), options);
  chart.render();
//======================PRESTASI THD SERTIFIKAT=========================//
var options = {
    series: [
    {
      type: 'boxPlot',
      data: [
        {
          x: 'Jan 2015',
          y: [54, 66, 69, 75, 88]
        },
        {
          x: 'Jan 2016',
          y: [43, 65, 69, 76, 81]
        },
      ]
    }
  ],
    chart: {
    type: 'boxPlot',
    height: 350
  },
  title: {
    text: 'Basic BoxPlot Chart',
    align: 'left'
  },
  plotOptions: {
    boxPlot: {
      colors: {
        upper: '#5C4742',
        lower: '#A5978B'
      }
    }
  }
  };

  var chart = new ApexCharts(document.querySelector(".chart_korelasi_sertifikat_terhadap_prediksi"), options);
  chart.render();

//======================JENIS KELAMIN=========================//
var options = {
    series: [45, 55],
    chart: {
    width: 380,
    type: 'pie',
},
labels: ['Laki-laki', 'Perempuan'],
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

var chart = new ApexCharts(document.querySelector(".chart_distribusi_jenis_kelamin"), options);
chart.render();

//======================PEKERJAAN ORTU=========================//
var options = {
    series: [44, 55, 13, 43, 22],
    chart: {
    width: 380,
    type: 'pie',
},
labels: ['Buruh', 'Swasta', 'Wiraswasta', 'Pekerja Lepas', 'PNS'],
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

var chart = new ApexCharts(document.querySelector(".chart_distribusi_pekerjaan"), options);
chart.render();


//======================PENGHASILAN ORTU=========================//
var options = {
    series: [{
    name: 'Inflation',
    data: [2.3, 3.1, 4.0, 10.1, 4.0, 3.6, 3.2, 2.3, 1.4, 0.8, 0.5, 0.2]
  }],
    chart: {
    height: 350,
    type: 'bar',
  },
  plotOptions: {
    bar: {
      borderRadius: 10,
      dataLabels: {
        position: 'top', // top, center, bottom
      },
    }
  },
  dataLabels: {
    enabled: true,
    formatter: function (val) {
      return val + "%";
    },
    offsetY: -20,
    style: {
      fontSize: '12px',
      colors: ["#304758"]
    }
  },
  
  xaxis: {
    categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    position: 'top',
    axisBorder: {
      show: false
    },
    axisTicks: {
      show: false
    },
    crosshairs: {
      fill: {
        type: 'gradient',
        gradient: {
          colorFrom: '#D8E3F0',
          colorTo: '#BED1E6',
          stops: [0, 100],
          opacityFrom: 0.4,
          opacityTo: 0.5,
        }
      }
    },
    tooltip: {
      enabled: true,
    }
  },
  yaxis: {
    axisBorder: {
      show: false
    },
    axisTicks: {
      show: false,
    },
    labels: {
      show: false,
      formatter: function (val) {
        return val + "%";
      }
    }
  
  },
  title: {
    text: 'Monthly Inflation in Argentina, 2002',
    floating: true,
    offsetY: 330,
    align: 'center',
    style: {
      color: '#444'
    }
  }
  };

  var chart = new ApexCharts(document.querySelector(".chart_distribusi_penghasilan_ortu"), options);
  chart.render();

//======================ANALISIS DESKRIPTIF=========================//

