$.get('https://swapi.co/api/people/5/?format=json', function (results) {
  let theName = results['name']
  $('div#character').text(theName);
});
