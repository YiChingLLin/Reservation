$(document).ready(function() {
  $(".datepicker").datepicker({
    defaultDate: new Date(),
    format: "yyyy/mm/dd"    
  });
});

function processData() {
  var restaurantdateElement = document.getElementById("restaurantdate");
  var restaurantdate = restaurantdatedateElement.value;
}