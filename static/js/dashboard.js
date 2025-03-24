import * as Vue from "https://cdn.jsdelivr.net/npm/vue@3.2/dist/vue.esm-browser.js"
// dashboard

const { createApp } = Vue

export const dashboard = createApp({
    // chart.js
    mounted() {
      const ctx1 = document.getElementById('lineChart').getContext('2d');
      this.chart1 = new Chart(ctx1, {
          type: 'line',
          data: {
              labels: ['2024年1月', '2024年2月', '2024年3月'],
              datasets: [
                  {
                      label: '我が家の資産の推移',
                      data: this.values1,
                  },
              ],

          }
      });
      const ctx2 = document.getElementById('pieChart').getContext('2d');
      this.chart2 = new Chart(ctx2, {
          type: 'pie',
          data: {
              labels: ['2024年1月', '2024年2月', '2024年3月'],
              datasets: [
                  {
                      label: '我が家の資産の推移',
                      data: this.values2,
                      backgroundColor: [
                          'yellow',
                          'pink',
                          'skyblue',
                          // 'rgb(255, 99, 132)',
                          // 'rgb(54, 162, 235)',
                          // 'rgb(255, 205, 86)'
                      ],
                  }
              ],

          }
      })
    },

    methods: {
        // write methods here.
    },
    data() {
        return {
            message: 'Django +++ Vue.js!',
            values1: [130, 200, 140],
            values2: [100, 200, 140],
            chart1: null,
            chart2: null,
        }
    },

    delimiters: ['[[', ']]'],
})

dashboard.mount('#dashboard')
