var header = document.querySelector('#header1');
header.style.color = 'red';

function randomColor() {
var letters =  "0123456789ABCDEF";
var color = '#';
for (var i = 0; i < 6; i++) {
  color += letters[Math.floor(Math.random()*16)];
}
return color;
}


function changeHeaderColor() {
  colorIn = randomColor();
  header.style.color = colorIn;
}

setInterval("changeHeaderColor()",500);
