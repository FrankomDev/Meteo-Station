const ctx = document.getElementById('temp1h');
const ctx2 = document.getElementById('press1h');
const ctx3 = document.getElementById('hum1h');

fetch('/api/get1h')
      .then(response => response.json())
      .then(data => {
	  createChart(data)
	  console.log(data)
      })

function createChart(data){

new Chart(ctx, {
   type: 'line',
    data: {
      	labels: [data[3][1], data[2][1], data[1][1], data[0][1]],
      	datasets: [{
           label: 'Temperatura °C',
           data: [data[3][2], data[2][2], data[1][2], data[0][2]],
           borderWidth: 1,
	   backgroundColor: '#466EFD',
	   borderColor: '#466EFD'
     	}]
    	},
    	options: {
      	  scales: {
           y: {
	    beginAtZero: true
        }
     }
    }
  });
new Chart(ctx2, {
   type: 'line',
    data: {
      	labels: [data[3][1], data[2][1], data[1][1], data[0][1]],
      	datasets: [{
           label: 'Ciśnienie hPa',
           data: [data[3][3], data[2][3], data[1][3], data[0][3]],
           borderWidth: 1,
	   backgroundColor: '#F6C109',
	   borderColor: '#F6C109'
     	}]
    	},
    	options: {
      	  scales: {
           y: {
	    beginAtZero: false
        }
     }
    }
  }); 
new Chart(ctx3, {
   type: 'line',
    data: {
      	labels: [data[3][1], data[2][1], data[1][1], data[0][1]],
      	datasets: [{
           label: 'Wilgotność %',
           data: [data[3][4], data[2][4], data[1][4], data[0][4]],
           borderWidth: 1,
	   backgroundColor: '#248754',
	   borderColor: '#248754'
     	}]
    	},
    	options: {
      	  scales: {
           y: {
	    beginAtZero: false
        }
     }
    }
  });
}
