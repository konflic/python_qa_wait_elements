var hidden = document.getElementsByClassName("hide")[0];

hidden.addEventListener("mouseover", function(e) {
    e.target.classList.remove("hide");
    e.target.className = "btn btn-success"
});

function loadXMLDoc() {
  var xhttp = new XMLHttpRequest();

  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      let obj = JSON.parse(this.responseText);
      let element = document.createElement(obj.tag);
      element.className = obj.classes;
      element.innerText = obj.text;
      element.style.display = obj.display;
      element.addEventListener("click", function(e) {
        setTimeout(function() {
          e.target.parentElement.firstElementChild.remove();
        }, 1000);
      });
      setTimeout(function() {
        document.getElementById("demo").appendChild(element);
      }, 2000);
    }
  };

  xhttp.open("GET", "data.json", true);
  xhttp.send();
}

let table = document.getElementsByClassName("table")[0];

table.addEventListener("click", function(e) {
    colors = Array("red", "green", "blue", "yello", "gray", "ivory", "lightgreen", "lightblue");
    e.target.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];;
});

var modal = document.getElementById("myModal");
// Get the button that opens the modal
var btn = document.getElementById("myBtn");
// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];
// When the user clicks the button, open the modal
btn.onclick = function() {
console.log("here!");
  modal.style.display = "block";
}
// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}