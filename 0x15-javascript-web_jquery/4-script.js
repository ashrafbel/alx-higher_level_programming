// Script that toggles the <header> class when the user
// clicks on <div id="toggle_header">

$('DIV#toggle_header').click(function () {
    $('HEADER').toggleClass('green red');
  });
