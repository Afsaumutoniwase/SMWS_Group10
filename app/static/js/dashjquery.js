document.addEventListener('DOMContentLoaded', (event) => {
    const ctx = document.getElementById('collectionsAvoidedChart').getContext('2d');
  
    const data = {
      labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
      datasets: [{
        label: 'Collections Avoided',
        data: [5, 8, 10, 15, 12, 9, 11],
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1
      }]
    };
  
    const config = {
      type: 'bar',
      data: data,
      options: {
        scales: {
          x: {
            beginAtZero: true,
            grid: {
              display: false // This removes the vertical lines
            }
          },
          y: {
            beginAtZero: true,
            grid: {
              display: true // This keeps the horizontal lines
            }
          }
        },
        plugins: {
            tooltip: {
              backgroundColor: 'rgba(87, 186, 152, 1)', // Background color of the tooltip
              borderColor: 'rgba(0, 0, 0, 0.2)', // Border color of the tooltip
              borderWidth: 1, // Border width of the tooltip
              borderRadius: 4, // Border radius of the tooltip
              padding: 10, // Padding of the tooltip content
              displayColors: false, // Whether to display color boxes in the tooltip
              shadowOffsetX: 2, // Horizontal shadow offset
              shadowOffsetY: 2, // Vertical shadow offset
              shadowBlur: 5, // Shadow blur radius
              shadowColor: 'rgba(0, 0, 0, 0.3)', // Shadow color
              bodyFont: {
                size: 14, // Font size of the tooltip body
                weight: 'normal', // Font weight of the tooltip body
                color: '#fff' // Font color of the tooltip body
              }
            }
          }
        }
      };
    const collectionsAvoidedChart = new Chart(ctx, config);
});
