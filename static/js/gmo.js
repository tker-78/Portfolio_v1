
import * as Vue from "https://cdn.jsdelivr.net/npm/vue@3.2/dist/vue.esm-browser.js"


const { createApp } = Vue

export const gmo = createApp({
   mounted() {
       window.google.charts.load('current', { packages: ['corechart'] });
       window.google.charts.setOnLoadCallback(this.drawChart);
   },
   methods: {
       drawChart() {
           console.log(this.values)
           const candleData = window.google.visualization.arrayToDataTable(this.values, true)
           const ctx1 = document.getElementById('candleChart')
           const chart = new window.google.visualization.CandlestickChart(ctx1)
           this.chart = chart
           this.chart.draw(candleData, this.options)
       }
   },
   data() {
       return {
           chart: null,
           values: [
              ['Mon', 20, 28, 38, 45],
              ['Tue', 31, 38, 55, 66],
              ['Wed', 50, 55, 77, 80],
              ['Thu', 77, 77, 66, 50],
              ['Fri', 68, 66, 22, 15],
           ],
           options: {
               legend: 'none',
           },
       }
   },
})

gmo.mount("#gmo")