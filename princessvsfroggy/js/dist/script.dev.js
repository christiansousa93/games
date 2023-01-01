"use strict";

var princess = document.querySelector('.princess');
var froggy = document.querySelector('.froggy');

var jump = function jump() {
  princess.classList.add('jump');
  setTimeout(function () {
    princess.classList.remove('jump');
  }, 500);
};

var loop = setInterval(function () {
  var froggyPosition = froggy.offsetLeft;
  var princessPosition = +window.getComputedStyle(princess).bottom.replace('px', '');

  if (froggyPosition >= 1000 && froggyPosition > 0 && princessPosition < 60) {
    froggy.style.animation = 'none';
    froggy.style.left = "".concat(froggyPosition, "px");
    princess.style.animation = 'none';
    princess.style.bottom = "".concat(princessPosition, "px");
    princess.src = './images/princessdead.gif';
    clearInterval(loop);
  }
}, 10);
document.addEventListener('keydown', jump);