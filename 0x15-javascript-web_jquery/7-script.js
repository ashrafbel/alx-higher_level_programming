// Fetches API data and replaces the character name in the <div id="character">

let u = 'https://swapi-api.hbtn.io/api/people/5/?format=json'
$.get(u, function (data) {
  $('#character').append(data.name);
});
