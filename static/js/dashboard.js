import * as Vue from "https://cdn.jsdelivr.net/npm/vue@3.2/dist/vue.esm-browser.js"
// dashboard

const { createApp } = Vue

export const dashboard = createApp({
    mounted() {
      const ctx = document.getElementById('lineChart').getContext('2d');
      this.chart = new Chart(ctx, {
          type: 'line',
          data: {
              labels: ['2024年1月', '2024年2月', '2024年3月'],
              datasets: [
                  {
                      label: '我が家の資産の推移',
                      data: this.values,
                  }
              ]
          }
      })
    },
    methods: {
        plus1() {
            this.values[0] = this.values[0] + 10
            this.chart.update()
        },
        plus2() {
            this.values[1] = this.values[1] + 10
            this.chart.update();
        },
        plus3() {
            this.values[2] = this.values[2] + 10
            this.chart.update();
        },
        minus1() {
            this.values[0] = this.values[0] - 10
            this.chart.update()
        },
        minus2() {
            this.values[1] = this.values[1] - 10
            this.chart.update()
        },
        minus3() {
            this.values[2] = this.values[2] - 10
            this.chart.update()
        },
    },
    data() {
        return {
            message: 'Django +++ Vue.js!',
            values: [130, 200, 140],
            chart: null,
        }
    },

    delimiters: ['[[', ']]'],
})

dashboard.mount('#dashboard')
