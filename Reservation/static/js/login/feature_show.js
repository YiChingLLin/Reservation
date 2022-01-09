const slider = document.querySelector('.slider-wrapper');    
const beforeImg = document.querySelector('.slider-before-img'); 
const handler = document.querySelector('.handler'); 
var marginX; 

handler.onmousedown = function(e) {
    marginX = e.pageX - handler.offsetLeft;
    slider.addEventListener('mousemove', moveHandler);
}
handler.onmouseup = function(e) {
    slider.removeEventListener('mousemove', moveHandler);
}


function moveHandler(e) {
    handler.style.left = e.pageX - marginX + 'px';
    beforeImg.style.width = e.pageX - marginX + 'px';
}