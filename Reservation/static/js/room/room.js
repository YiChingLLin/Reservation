$(document).ready(function() {
  $(".datepicker").datepicker({
    defaultDate: new Date(),
    format: "yyyy/mm/dd"    
  });
});

function processData() {
  var roomdateElement = document.getElementById("roomdate");
  var roomdate = roomdateElement.value;
}