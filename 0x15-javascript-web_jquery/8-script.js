$.get('https://swapi.co/api/films?format=json', function (data, textStatus) {
  let length = data.results.length;
  for (let x of data.results) {
    $('ul#list_movies').append(x.title);
    $('ul#list_movies').append("\n");
  }
});
