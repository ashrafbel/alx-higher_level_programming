// Fetches API data and replaces the character name in the <div id="character">

let u = 'https://swapi.co/api/people/5/?format=json';
$.get(u, function (data) {
  $('div#character').text(data.name);
});
