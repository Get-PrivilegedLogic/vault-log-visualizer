document.addEventListener("DOMContentLoaded", () => {
  const ctx = document.getElementById("checkoutsChart").getContext("2d");
  new Chart(ctx, {
    type: "bar",
    data: {
      labels: ["Windows", "Linux", "DB", "AWS"],
      datasets: [{
        label: "CheckOuts",
        data: [12, 19, 3, 5],
        backgroundColor: "rgba(54, 162, 235, 0.5)"
      }]
    },
    options: {
      responsive: true,
      scales: {
        y: { beginAtZero: true }
      }
    }
  });
});
