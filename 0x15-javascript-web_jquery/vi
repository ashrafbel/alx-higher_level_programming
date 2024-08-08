let u = 'https://swapi-api.hbtn.io/api/films/?format=json'
$.get(u , function (data) {
  console.log(data);
  data.results.forEach(m => {
    $('UL#list_movies').append(m.title);
  });
});
