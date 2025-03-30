import * as Vue from "https://cdn.jsdelivr.net/npm/vue@3.2/dist/vue.esm-browser.js"

const { createApp } = Vue

export const gmoIndex = createApp({
    mounted() {
        this.getForexStatus()
    },
    methods: {
        getForexStatus() {
            fetch('/gmo/api/forex-status')
                .then(response => {
                    if (!response.ok) {
                        throw new Error("Network Error: " + response.statusText);
                    }
                    return response.json()
                })
                .then(data => {
                    console.log(data)
                    this.status = data.data.status
                    this.responsetime = data.responsetime
                })
        }

    },
    data() {
        return {
            status: null,
            responsetime: null,
        }
    },
    delimiters: ['[[', ']]']
})

gmoIndex.mount("#forex-status")