// Script that updates the <header> text to 'New Header!!!'
//when clicking on <div id="update_header">

$('DIV#update_header').click(function () {
    $('HEADER').text('New Header!!!');
  });
