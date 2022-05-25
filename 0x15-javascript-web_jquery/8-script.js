$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
var res = data.results;
for(i = 0; i < res.length; i++)
$('#list_movies').append('<li>'+res[i].title+'</li>');
});
