var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
output.innerHTML = slider.value; // Display the default slider value
slider.oninput = function() {
    output.innerHTML = this.value;
    client.send("buttons",this.value);
  }