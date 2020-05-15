$(document).ready(function () {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  $.get(url, function (data) {
    const result = data.results;
    $.each(result, function (data2, movie) {
      $('ul#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
