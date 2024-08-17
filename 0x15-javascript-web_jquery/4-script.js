$(document).ready(function () {
  // Add a click event handler to the div with the id 'toggle_header'
  $("#toggle_header").click(function () {
    $("header").toggleClass("red green");
  });
});
