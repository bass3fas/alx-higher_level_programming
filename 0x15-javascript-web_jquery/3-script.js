$(document).ready(function() {
  // Add click event listener to the div with id "red_header"
  $('div#red_header').click(function() {
    // Add class "red" to the <header> element
    $('header').addClass('red');
  });
});
