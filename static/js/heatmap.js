import * as Vue from "https://cdn.jsdelivr.net/npm/vue@3.2/dist/vue.esm-browser.js"

const { createApp } = Vue

export const calheatmap = createApp({
    mounted() {
        const cal = new CalHeatmap();
        cal.paint(this.options);
    },
    data() {
        return {
            options: {
                range: 5,
                domain: {type: 'month', sort: 'asc'},
                subDomain: {type: 'day'},
                scale: {
                    color: {
                        type: 'linear',
                        range: ['#e6e6e6', '#4dd05a'],
                        domain: [0, 1],
                    },
                },
            },
        }
    }
})

calheatmap.mount('#cal-heatmap')



