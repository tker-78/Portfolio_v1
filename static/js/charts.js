// LineChart
let ctx = document.getElementById("lineChart").getContext("2d");
let lineChart = new Chart(ctx, {
    type: "line",
    data: {
        labels: [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ],
        datasets: [
            {
                label: "work load",
                data: [2, 9, 3, 17, 6, 3, 7],
                backgroundColor: "rgba(153,205,1,0.6)",
            },
            {
                label: "free hours",
                data: [2, 2, 5, 5, 2, 1, 10],
                backgroundColor: "rgba(155,153,10,0.6)",
            },
        ],
    },
});
