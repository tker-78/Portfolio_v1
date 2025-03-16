

import * as Vue from "https://cdn.jsdelivr.net/npm/vue@3.2/dist/vue.esm-browser.js"
// dashboard

const { createApp } = Vue

export const dashboard = createApp({
    data() {
        return {
            message: "Django + Vue.js!",
        }
    },
    delimiters: ['[[', ']]']
});
dashboard.mount('#dashboard')





//shortcuts
const shortcuts = createApp({
    data() {
        return {
            message: "Django + Vue.js!"
        }
    },
    delimiters: ['[[', ']]']
})

shortcuts.mount('#shortcuts')


// Overview
const overview = createApp({
    data() {
        return {
            message: "Django + Vue.js!"
        }
    },
    delimiters: ['[[', ']]']
})

overview.mount('#overview')


//Events
const events = createApp({
    data() {
        return {
            message: "Django + Vue.js!"
        }
    },
    delimiters: ['[[', ']]']
})

events.mount('#events')



//Profile
const profile = createApp({
    data() {
        return {
            message: "Django + Vue.js!"
        }
    },
    delimiters: ['[[', ']]']
})

profile.mount('#profile')


//Status
const status = createApp({
    data() {
        return {
            message: "Django + Vue.js!"
        }
    },
    delimiters: ['[[', ']]']
})

status.mount('#status')


