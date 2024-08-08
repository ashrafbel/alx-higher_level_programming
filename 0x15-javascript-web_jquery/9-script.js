$(document).ready(function() {
    let u = 'https://hellosalut.stefanbohacek.dev/?lang=fr'
    $.get(u, function(data) {
      $('#hello').text(data.hello);
    });
  });
