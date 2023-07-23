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

var chart = new ApexCharts(document.querySelector("#chart_jenis_kelamin"), options);
chart.render();

//======================PEKERJAAN ORTU=========================//
var options = {
    series: [44, 55, 13, 43, 22],
    chart: {
    width: 380,
    type: 'pie',
},
labels: ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
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

var chart = new ApexCharts(document.querySelector("#chart_pekerjaan_ortu"), options);
chart.render();

