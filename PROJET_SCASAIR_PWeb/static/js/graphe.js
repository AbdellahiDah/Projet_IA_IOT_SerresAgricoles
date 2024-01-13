new WOW().init();
	window.chartColors = {
		red: 'rgb(255, 99, 132)',
		orange: 'rgb(255, 159, 64)',
		yellow: 'rgb(255, 205, 86)',
		green: 'rgb(75, 192, 192)',
		blue: 'rgb(54, 162, 235)',
		purple: 'rgb(153, 102, 255)',
		grey: 'rgb(201, 203, 207)'
    };
	var config1 = {
			type: 'line',
			data: {
				labels: Array(10).fill(0).map((x, y) => x + y),
				datasets: [{
					label: 'DHT TEMPERATURE SENSOR 1',
					fill: false,
					backgroundColor: window.chartColors.blue,
					borderColor: window.chartColors.blue,
					data: []
				}]
			},
			options: {
				responsive: true,
				aspectRatio: 1,
				title: {
					display: true,
					//text: "Node 1 Temperature's Chart"
				},
				legend: {
					position: 'top',
					labels: {
						fontColor: '#000'
					}
				},
				tooltips: {
					mode: 'index',
					intersect: false,
				},
				hover: {
					mode: 'nearest',
					intersect: true
				},
				scales: {
					xAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							//labelString: 'Seconds'
						}
					}],
					yAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							//labelString: 'Value in C'
						}
					}]
				}
			}
	};
	var config2 = {
			type: 'line',
			data: {
				labels: Array(10).fill(0).map((x, y) => x + y),
				datasets: [{
					label: 'DHT TEMPERATURE SENSOR 2',
					fill: false,
					backgroundColor: window.chartColors.yellow,
					borderColor: window.chartColors.yellow,
					data: []
				}]
			},
			options: {
				responsive: true,
				aspectRatio: 1,
				title: {
					display: true,
					//text: "Node 2 Temperature's Chart"
				},
				legend: {
					position: 'top',
					labels: {
						fontColor: '#000'
					}
				},
				tooltips: {
					mode: 'index',
					intersect: false,
				},
				hover: {
					mode: 'nearest',
					intersect: true
				},
				scales: {
					xAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							//labelString: 'Seconds'
						}
					}],
					yAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							//labelString: 'Value in C'
						}
					}]
				}
			}
	};
	var config3 = {
			type: 'line',
			data: {
				labels: Array(10).fill(0).map((x, y) => x + y),
				datasets: [{
					label: 'DHT TEMPERATURE SENSOR 3',
					fill: false,
					backgroundColor: window.chartColors.purple,
					borderColor: window.chartColors.purple,
					data: []
				}]
			},
			options: {
				responsive: true,
				aspectRatio: 1,
				title: {
					display: true,
					//text: "Node 3 Temperature's Chart"
				},
				legend: {
					position: 'top',
					labels: {
						fontColor: '#000'
					}
				},
				tooltips: {
					mode: 'index',
					intersect: false,
				},
				hover: {
					mode: 'nearest',
					intersect: true
				},
				scales: {
					xAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							//labelString: 'Seconds'
						}
					}],
					yAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							//labelString: 'Value in C'
						}
					}]
				}
			}
	};
	var config4 = {
			type: 'line',
			data: {
				labels: Array(10).fill(0).map((x, y) => x + y),
				datasets: [{
					label: 'DHT TEMPERATURE SENSOR 4',
					fill: false,
					backgroundColor: window.chartColors.red,
					borderColor: window.chartColors.red,
					data: []
				}]
			},
			options: {
				responsive: true,
				aspectRatio: 1,
				title: {
					display: true,
					//text: "Node 4 Temperature's Chart"
				},
				legend: {
					position: 'top',
					labels: {
						fontColor: '#000'
					}
				},
				tooltips: {
					mode: 'index',
					intersect: false,
				},
				hover: {
					mode: 'nearest',
					intersect: true
				},
				scales: {
					xAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							//labelString: 'Seconds'
						}
					}],
					yAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							//labelString: 'Value in C'
						}
					}]
				}
			}
	};
	var config5 = {
			type: 'line',
			data: {
				labels: Array(10).fill(0).map((x, y) => x + y),
				datasets: [{
					label: 'DHT TEMPERATURE SENSOR 5',
					fill: false,
					backgroundColor: window.chartColors.green,
					borderColor: window.chartColors.green,
					data: []
				}]
			},
			options: {
				responsive: true,
				aspectRatio: 1,
				title: {
					display: true,
					//text: "Node 5 Temperature's Chart"
				},
				legend: {
					position: 'top',
					labels: {
						fontColor: '#000'
					}
				},
				tooltips: {
					mode: 'index',
					intersect: false,
				},
				hover: {
					mode: 'nearest',
					intersect: true
				},
				scales: {
					xAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							//labelString: 'Seconds'
						}
					}],
					yAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							//labelString: 'Value in C'
						}
					}]
				}
			}
	};
	var t;

	function loadData() {
		var xhttp;
		var moyen
		var url="/data"
		xhttp=new XMLHttpRequest()
		xhttp.onreadystatechange = function() {
			if (this.readyState == 4 && this.status == 200) {
				var myData = xhttp.responseText
				var parsedData = JSON.parse(myData)
				var tempData1 = parsedData.temperature1
				var tempData2 = parsedData.temperature2
				var tempData3 = parsedData.temperature3
				var tempData4 = parsedData.temperature4
				var tempData5 = parsedData.temperature5
				var moyen1=parsedData.moyen1
				var moyen2=parsedData.moyen2
				var moyen3=parsedData.moyen3
				var moyen4=parsedData.moyen4
				var moyen5=parsedData.moyen5
				var moyenG=parsedData.moyenG

                //Hum
                var hum1 = parsedData.hum1
				var hum2 = parsedData.hum2
				var hum3 = parsedData.hum3
				var hum4 = parsedData.hum4
				var hum5 = parsedData.hum5
				var moyhum1=parsedData.moyhum1
				var moyhum2=parsedData.moyhum2
				var moyhum3=parsedData.moyhum3
				var moyhum4=parsedData.moyhum4
				var moyhum5=parsedData.moyhum5
				var moyhumG=parsedData.moyhumG

                //CO2
                var CO21 = parsedData.CO21
				var CO22 = parsedData.CO22
				var CO23 = parsedData.CO23
				var CO24 = parsedData.CO24
				var CO25 = parsedData.CO25
				var moyco21=parsedData.moyco21
				var moyco22=parsedData.moyco22
				var moyco23=parsedData.moyco23
				var moyco24=parsedData.moyco24
				var moyco25=parsedData.moyco25
				var moyco2G=parsedData.moyco2G

                //PH
                var PH1 = parsedData.PH1
				var PH2 = parsedData.PH2
				var PH3 = parsedData.PH3
				var PH4 = parsedData.PH4
				var PH5 = parsedData.PH5
				var moyph1=parsedData.moyph1
				var moyph2=parsedData.moyph2
				var moyph3=parsedData.moyph3
				var moyph4=parsedData.moyph4
				var moyph5=parsedData.moyph5
				var moyphG=parsedData.moyphG

				var ledData=parsedData.leds

				// myData=myData.replace(/\s|\[|\]|\n/g, "").split(',').map(Number);
				config1["data"]["datasets"][0]["data"]=tempData1.reverse();
				config2["data"]["datasets"][0]["data"]=tempData2.reverse();
				config3["data"]["datasets"][0]["data"]=tempData3.reverse();
				config4["data"]["datasets"][0]["data"]=tempData4.reverse();
				config5["data"]["datasets"][0]["data"]=tempData5.reverse();
				chart1.update();
				chart2.update();
				chart3.update(); 
				chart4.update();
				chart5.update();

                // myData=myData.replace(/\s|\[|\]|\n/g, "").split(',').map(Number);
				config1["data"]["datasets"][0]["data"]=hum1.reverse();
				config2["data"]["datasets"][0]["data"]=hum2.reverse();
				config3["data"]["datasets"][0]["data"]=hum3.reverse();
				config4["data"]["datasets"][0]["data"]=hum4.reverse();
				config5["data"]["datasets"][0]["data"]=hum5.reverse();
				chart6.update();
				chart7.update();
				chart8.update();
				chart9.update();
				chart10.update();

                // myData=myData.replace(/\s|\[|\]|\n/g, "").split(',').map(Number);
				config1["data"]["datasets"][0]["data"]=CO21.reverse();
				config2["data"]["datasets"][0]["data"]=CO22.reverse();
				config3["data"]["datasets"][0]["data"]=CO23.reverse();
				config4["data"]["datasets"][0]["data"]=CO24.reverse();
				config5["data"]["datasets"][0]["data"]=CO25.reverse();
				chart11.update();
				chart12.update();
				chart13.update();
				chart14.update();
				chart15.update();

                config1["data"]["datasets"][0]["data"]=PH1.reverse();
				config2["data"]["datasets"][0]["data"]=PH2.reverse();
				config3["data"]["datasets"][0]["data"]=PH3.reverse();
				config4["data"]["datasets"][0]["data"]=PH4.reverse();
				config5["data"]["datasets"][0]["data"]=PH5.reverse();
				chart16.update();
				chart17.update();
				chart18.update();
				chart19.update();
				chart20.update();
				var tmp;
				
                // Temp
				tmp=document.getElementById("tmp1")
				tmp.textContent=moyen1

				tmp=document.getElementById("tmp2")
				tmp.textContent=moyen2

				tmp=document.getElementById("tmp3")
				tmp.textContent=moyen3

				tmp=document.getElementById("tmp4")
				tmp.textContent=moyen4

				tmp=document.getElementById("tmp5")
				tmp.textContent=moyen5

				tmp=document.getElementById("tmpG")
				moyenG=parseFloat(moyenG).toFixed(1)
				tmp.textContent=moyenG


                // Hum
                tmp=document.getElementById("hum1")
				tmp.textContent=moyhum1

				tmp=document.getElementById("hum2")
				tmp.textContent=moyhum2

				tmp=document.getElementById("hum3")
				tmp.textContent=moyhum3

				tmp=document.getElementById("hum4")
				tmp.textContent=moyhum4

				tmp=document.getElementById("hum5")
				tmp.textContent=moyhum5

				tmp=document.getElementById("humG")
				moyenG=parseFloat(moyhumG).toFixed(1)
				tmp.textContent=moyhumG


                // CO2 Level
                tmp=document.getElementById("co21")
				tmp.textContent=moyco21

				tmp=document.getElementById("co22")
				tmp.textContent=moyco22

				tmp=document.getElementById("co23")
				tmp.textContent=moyco23

				tmp=document.getElementById("co24")
				tmp.textContent=moyco24

				tmp=document.getElementById("co25")
				tmp.textContent=moyco25

				tmp=document.getElementById("co2G")
				moyenG=parseFloat(moyco2G).toFixed(1)
				tmp.textContent=moyco2G

                // PH Level
                tmp=document.getElementById("ph1")
				tmp.textContent=moyph1

				tmp=document.getElementById("ph2")
				tmp.textContent=moyph2

				tmp=document.getElementById("ph3")
				tmp.textContent=moyph3

				tmp=document.getElementById("ph4")
				tmp.textContent=moyph4

				tmp=document.getElementById("ph5")
				tmp.textContent=moyph5

				tmp=document.getElementById("phG")
				moyenG=parseFloat(moyphG).toFixed(1)
				tmp.textContent=moyphG


                // Temp
				var greenLED = document.getElementById("led-green")
				var orangeLED = document.getElementById("led-orange")
				var redLED = document.getElementById("led-red")

				if(ledData[0]==1){
					greenLED.classList.add("led-green-active")
					greenLED.classList.remove("led-green-inactive")
					orangeLED.classList.remove("led-orange-active")
					orangeLED.classList.add("led-orange-inactive")
					redLED.classList.remove("led-red-active")
					redLED.classList.add("led-red-inactive")
				}
				else if(ledData[1]==1){
					greenLED.classList.remove("led-green-active")
					greenLED.classList.add("led-green-inactive")
					orangeLED.classList.add("led-orange-active")
					orangeLED.classList.remove("led-orange-inactive")
					redLED.classList.remove("led-red-active")
					redLED.classList.add("led-red-inactive")
				}
				else if(ledData[2]==1){
					greenLED.classList.remove("led-green-active")
					greenLED.classList.add("led-green-inactive")
					orangeLED.classList.remove("led-orange-active")
					orangeLED.classList.add("led-orange-inactive")
					redLED.classList.add("led-red-active")
					redLED.classList.remove("led-red-inactive")
				}
				else if(ledData[3]==1){
					greenLED.classList.remove("led-green-active")
					greenLED.classList.add("led-green-inactive")
					orangeLED.classList.remove("led-orange-active")
					orangeLED.classList.add("led-orange-inactive")
					redLED.classList.add("led-red-active")
					redLED.classList.remove("led-red-inactive")
				}
				else if(ledData[4]==1){
					greenLED.classList.remove("led-green-active")
					greenLED.classList.add("led-green-inactive")
					orangeLED.classList.remove("led-orange-active")
					orangeLED.classList.add("led-orange-inactive")
					redLED.classList.add("led-red-active")
					redLED.classList.remove("led-red-inactive")
				}
			}
		}
		xhttp.open("GET", url, true)
		xhttp.send()
	}
	
	window.onload = function() {
        // Temp
		var ctx1 = document.getElementById('canvas1').getContext('2d');
		var ctx2 = document.getElementById('canvas2').getContext('2d');
		var ctx3 = document.getElementById('canvas3').getContext('2d');
		var ctx4 = document.getElementById('canvas4').getContext('2d');
		var ctx5 = document.getElementById('canvas5').getContext('2d');

        //Hum
        var ctx6 = document.getElementById('canvas6').getContext('2d');
		var ctx7 = document.getElementById('canvas7').getContext('2d');
		var ctx8 = document.getElementById('canvas8').getContext('2d');
		var ctx9 = document.getElementById('canvas9').getContext('2d');
		var ctx10 = document.getElementById('canvas10').getContext('2d');

        //CO2
        var ctx11 = document.getElementById('canvas11').getContext('2d');
		var ctx12 = document.getElementById('canvas12').getContext('2d');
		var ctx13 = document.getElementById('canvas13').getContext('2d');
		var ctx14 = document.getElementById('canvas14').getContext('2d');
		var ctx15 = document.getElementById('canvas15').getContext('2d');

        //PH
        var ctx16 = document.getElementById('canvas16').getContext('2d');
		var ctx17 = document.getElementById('canvas17').getContext('2d');
		var ctx18 = document.getElementById('canvas18').getContext('2d');
		var ctx19 = document.getElementById('canvas19').getContext('2d');
		var ctx20 = document.getElementById('canvas20').getContext('2d');

        chart1 = new Chart(ctx1, config1);
		chart2 = new Chart(ctx2, config2);
		chart3 = new Chart(ctx3, config3);
		chart4 = new Chart(ctx4, config4);
		chart5 = new Chart(ctx5, config5);

        chart6 = new Chart(ctx6, config1);
		chart7 = new Chart(ctx7, config2);
		chart8 = new Chart(ctx8, config3);
		chart9 = new Chart(ctx9, config4);
		chart10 = new Chart(ctx10, config5);

        chart11 = new Chart(ctx11, config1);
		chart12= new Chart(ctx12, config2);
		chart13 = new Chart(ctx13, config3);
		chart14 = new Chart(ctx14, config4);
		chart15 = new Chart(ctx15, config5);

        chart16 = new Chart(ctx16, config1);
		chart17= new Chart(ctx17, config2);
		chart18 = new Chart(ctx18, config3);
		chart19 = new Chart(ctx19, config4);
		chart20 = new Chart(ctx20, config5);


		window.setInterval(function(){
			loadData()
		},1000);
	};


    loadData();