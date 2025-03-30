import * as Vue from "https://cdn.jsdelivr.net/npm/vue@3.2/dist/vue.esm-browser.js"

const { createApp } = Vue

export const gmoIndex = createApp({
    mounted() {
        this.getForexStatus()
        this.getTicker()
        this.getKLine()

        setInterval(() => {
            this.getForexStatus()
            this.getTicker()
        }, 30000)
    },
    computed: {
        statusClass() {
            return {
                "text-red": this.status === "CLOSE",
                "text-green": this.status === "OPEN"
            }
        }
    },
    methods: {
        getForexStatus() {
            fetch('/gmo/api/forex-status')
                .then(response => {
                    if (!response.ok) {
                        throw new Error("Network Error in fetching forex status: " + response.statusText);
                    }
                    return response.json()
                })
                .then(data => {
                    console.log(data)
                    this.status = data.data.status
                    this.responsetime = data.responsetime
                })
        },
        getTicker() {
            this.ticker = []
            fetch('/gmo/api/ticker')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network Error in fetching Ticker: ' + response.statusText);
                    }
                    return response.json()
                })
                .then(data => {
                    for (const d of data.data) {
                        this.ticker.push({
                            symbol: d.symbol,
                            ask: d.ask,
                            bid: d.bid,
                            }
                        )
                    }
                })
        },
        getKLine() {
            fetch(`/gmo/api/klines/?symbol=${this.symbol}&priceType=${this.priceType}&interval=${this.interval}&date=${this.date}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network Error in fetching KLine: ' + response.statusText);
                    }
                    return response.json()
                })
                .then(data => {
                    console.log(data)
                })

        }

    },
    data() {
        return {
            status: null,
            responsetime: null,
            ticker: [],
            kline: [],
            symbol: "USD_JPY",
            priceType: "ASK",
            interval: "1hour",
            date: "20250328",
        }
    },
    delimiters: ['[[', ']]']
})

gmoIndex.mount("#gmo")