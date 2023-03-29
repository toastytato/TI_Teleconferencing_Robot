var clientId = Math.floor(Math.random() * 10000).toString();
client = new Paho.MQTT.Client("f88526ba972442818f936ee5c29a35e8.s2.eu.hivemq.cloud", 8884,clientId);
var text = document.getElementById("display")

// //set callback handlers
// client.onConnectionLost = function (responseObject) {
//     console.log("Connection Lost: "+responseObject.errorMessage);
// }


// // Called when the connection is made
function onConnect(){
	text.innerHTML = "test";
  //client.subscribe("#");

}

try {
  client.connect({
  
    onSuccess: onConnect,
    userName: 'karen',
    password: "seniordesignteami13",
    useSSL:true
  });
  
}
catch(err) {
  document.getElementById("demo").innerHTML = err.message;
}

// // Connect the client, providing an onConnect callback

document.onkeydown = checkKey; 
document.onkeyup = checkKeyup;
function checkKey(e) {
  
    e = e || window.event;

    if (e.keyCode == '38') {
      text.innerHTML = "move forward";
      client.send("control","forward");
      
    }
    else if (e.keyCode == '40') {
      text.innerHTML = "backwards";
     // client.send("control","backwards");
      
    }
    else if (e.keyCode == '37') {
      text.innerHTML = "turn left";
     // client.send("control","left");
      
    }
    else if (e.keyCode == '39') {
      //client.send("control","right");
      text.innerHTML = "turn right";
    }
    else if (e.keyCode == '87') {
      //client.send("control","up");
      text.innerHTML = "actuator up";
    }
    else if (e.keyCode == '83') {
      //client.send("control","down");
      text.innerHTML = "actuator down";
    }

    else{
      //client.send("control","stop");
      text.innerHTML = "stopped";
    }
  
}


function checkKeyup(e) {
  var text = document.getElementById("display")
    e = e || window.event;
    //client.send("control","stop");
    text.innerHTML = "stop";
    
}