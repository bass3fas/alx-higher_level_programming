$(document).ready(function() {
  // Add click event listener to the div with id "red_header"
  $('div#red_header').click(function() {
    // Update the text color of the <header> element to red
    $('header').css('color', '#FF0000');
  });
});
