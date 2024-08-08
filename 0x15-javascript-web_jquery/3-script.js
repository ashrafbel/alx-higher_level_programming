// Uses jQuery to add the red class to the <header> tag
// and turn it red when <div id="red_header"> is clicked

$('DIV#red_header').click(function () {
    $('HEADER').addClass('red');
  });
