var slider = document.getElementById("myRange");
var output = document.getElementById("demo");

list = [(10),(15),(20),(25),(45)];

output.innerHTML = "Speed: " + slider.value; // Display the default slider value
slider.oninput = function() {
    output.innerHTML = "Speed: " +  this.value;
    var actualspeed = list[this.value - 1];
    client.send("buttons", String(actualspeed));
  }

//does this work?