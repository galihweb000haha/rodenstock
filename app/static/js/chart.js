//======================HASIL PREDIKSI=========================//
el = document.querySelector(".chart_hasil_prediksi_relevansi")
var options = {
    series: [{
    name: 'Relevan',
    data: JSON.parse(el.dataset.data_hasil_prediksi)[0]
  }, {
    name: 'Tidak Relevan',
    data: JSON.parse(el.dataset.data_hasil_prediksi)[1]
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
    categories: ['2023',
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

  var chart = new ApexCharts(el, options);
  chart.render();
//======================PRESTASI THD PREDIKSI=========================//
var el = document.querySelector(".chart_korelasi_prestasi_terhadap_prediksi")
var options = {
    series: [
    {
      type: 'boxPlot',
      data: [
        {
          x: 'Relevan',
          y: JSON.parse(el.dataset.prestasi_relevan),
        },
        {
          x: 'Tidak Relevan',
          y: JSON.parse(el.dataset.prestasi_tidak_relevan),
        },
      ]
    }
  ],
    chart: {
    type: 'boxPlot',
    height: 350
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

  var chart = new ApexCharts(el, options);
  chart.render();
//======================PRESTASI THD ORGANISASI=========================//
var el = document.querySelector(".chart_korelasi_organisasi_terhadap_prediksi")
var options = {
    series: [
    {
      type: 'boxPlot',
      data: [
        {
          x: 'Relevan',
          y: JSON.parse(el.dataset.organisasi_relevan),
        },
        {
          x: 'Tidak Relevan',
          y: JSON.parse(el.dataset.organisasi_tidak_relevan),
        },
      ]
    }
  ],
    chart: {
    type: 'boxPlot',
    height: 350
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

  var chart = new ApexCharts(el, options);
  chart.render();
//======================PRESTASI THD SERTIFIKAT=========================//
el = document.querySelector(".chart_korelasi_sertifikat_terhadap_prediksi")
var options = {
    series: [
    {
      type: 'boxPlot',
      data: [
        {
          x: 'Relevan',
          y: JSON.parse(el.dataset.sertifikat_relevan),
        },
        {
          x: 'Tidak Relevan',
          y: JSON.parse(el.dataset.sertifikat_tidak_relevan),
        },
      ]
    }
  ],
    chart: {
    type: 'boxPlot',
    height: 350
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

  var chart = new ApexCharts(el, options);
  chart.render();

//======================JENIS KELAMIN=========================//
el = document.querySelector(".chart_distribusi_jenis_kelamin")
var options = {
    series: JSON.parse(el.dataset.ammount_gender),
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

var chart = new ApexCharts(el, options);
chart.render();

//======================PEKERJAAN ORTU=========================//
el = document.querySelector(".chart_distribusi_pekerjaan")
var options = {
    series: JSON.parse(el.dataset.pekerjaan_ortu),
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

var chart = new ApexCharts(el, options);
chart.render();


//======================PENGHASILAN ORTU=========================//
el = document.querySelector(".chart_distribusi_penghasilan_ortu")
var options = {
  series: [{
  name: 'Jml',
  data: JSON.parse(el.dataset.penghasilan_ortu)
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
    return val;
  },
  offsetY: -20,
  style: {
    fontSize: '12px',
    colors: ["#304758"]
  }
},

xaxis: {
  categories: [
      "< 1 JT",
      "1-2JT",
      "2-3JT",
      "3-4JT",
      "4-5JT",
      ">5JT",
  ],
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
};

var chart = new ApexCharts(el, options);
chart.render();
//======================// SCATTER PRESTASI=========================//

el = document.querySelector(".chart_sactter_prestasi")
var options = {
  series: [{
  name: "Relevan",
  data: JSON.parse(el.dataset.scatter_prestasi_relevan)
},{
  name: "Tidak Relevan",
  data: JSON.parse(el.dataset.scatter_prestasi_tidak_relevan)
}],
  chart: {
  height: 350,
  type: 'scatter',
  zoom: {
    enabled: true,
    type: 'xy'
  }
},
xaxis: {
  tickAmount: 10,
  labels: {
    formatter: function(val) {
      return parseFloat(val).toFixed(1) 
    }
  }
},
yaxis: {
  show: false,
  tickAmount: 7, 
  labels: {
    formatter: function(val) {
      return parseFloat(val).toFixed(1) + "%"
    }
  },

}

};

var chart = new ApexCharts(el, options);
chart.render();
// SCATTER ORGANISASI
el = document.querySelector(".chart_sactter_organisasi")
var options = {
  series: [{
  name: "Relevan",
  data: JSON.parse(el.dataset.scatter_organisasi_relevan)
},{
  name: "Tidak Relevan",
  data: JSON.parse(el.dataset.scatter_organisasi_tidak_relevan)
}],
  chart: {
  height: 350,
  type: 'scatter',
  zoom: {
    enabled: true,
    type: 'xy'
  }
},
xaxis: {
  tickAmount: 10,
  labels: {
    formatter: function(val) {
      return parseFloat(val).toFixed(1) 
    }
  }
},
yaxis: {
  show: false,
  tickAmount: 7, 
  labels: {
    formatter: function(val) {
      return parseFloat(val).toFixed(1) + "%"
    }
  },

}

};

var chart = new ApexCharts(el, options);
chart.render();
// SCATTER SERTIFIKAT
el = document.querySelector(".chart_sactter_sertifikat")
var options = {
  series: [{
  name: "Relevan",
  data: JSON.parse(el.dataset.scatter_sertifikat_relevan)
},{
  name: "Tidak Relevan",
  data: JSON.parse(el.dataset.scatter_sertifikat_tidak_relevan)
}],
  chart: {
  height: 350,
  type: 'scatter',
  zoom: {
    enabled: true,
    type: 'xy'
  }
},
xaxis: {
  tickAmount: 10,
  labels: {
    formatter: function(val) {
      return parseFloat(val).toFixed(1) 
    }
  }
},
yaxis: {
  show: false,
  tickAmount: 7, 
  labels: {
    formatter: function(val) {
      return parseFloat(val).toFixed(1) + "%"
    }
  },

}

};

var chart = new ApexCharts(el, options);
chart.render();