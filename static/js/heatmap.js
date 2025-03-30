import * as Vue from "https://cdn.jsdelivr.net/npm/vue@3.2/dist/vue.esm-browser.js"

const { createApp } = Vue

export const heatmap = createApp({
    mounted() {
        const ctx1 = document.getElementById("heatmap-chart")
        ctx1.width = ctx1.clientWidth * window.devicePixelRatio
        ctx1.height = ctx1.clientHeight * window.devicePixelRatio
        this.chart = echarts.init(ctx1)
        this.getVirtualData('2025')
        // this.chart.setOption(this.options)
    },
    methods: {
        getVirtualData(year) {
              const date = +echarts.time.parse(year + '-01-01');
              const end = +echarts.time.parse(+year + 1 + '-01-01');
              const dayTime = 3600 * 24 * 1000;
              const data = [];
              // for (let time = date; time < end; time += dayTime) {
              //   data.push([
              //     echarts.time.format(time, '{yyyy}-{MM}-{dd}', false),
              //     Math.floor(Math.random() * 10000)
              //   ]);
              // }
              // this.options.series.data = data

            fetch('api/calendar-data')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok: ' + response.statusText);
                    }
                    return response.json()
                })
                .then(data => {
                    const array_data = Object.entries(data).map(([date, value]) => {
                        return [date, value]
                    })
                    this.options.series.data = array_data
                    this.chart.setOption(this.options)
                })




            // this.options.series.data = [
            //     ['2025-01-01', 1],
            //     ['2025-01-02', 2],
            //     ['2025-01-03', 3],
            // ]
        }
    },
    data() {
        return {
            data: null,
            chart: null,
            options: {
                title: {
                top: 30,
                left: 'center',
                text: '日記投稿数'
              },
              tooltip: {},
              visualMap: {
                min: 0,
                max: 10,
                type: 'piecewise',
                orient: 'horizontal',
                left: 'center',
                top: 65,
                inRange: {
                  // 緑系のグラデーション
                  color: ['#e6f3e6', '#c6e6c6', '#a6d9a6', '#86cc86', '#66bf66', '#46b246', '#26a526', '#069906']
                },
              },
              calendar: {
                top: 120,
                left: 30,
                right: 30,
                cellSize: ['auto', 18],
                range: '2025',
                itemStyle: {
                  borderWidth: 0.5,
                },
                yearLabel: { show: false }
              },
              series: {
                type: 'heatmap',
                coordinateSystem: 'calendar',
                data: null
              }
            }
        }
    }

})

heatmap.mount('#heatmap')



