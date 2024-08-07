$(document).ready(function() {
  // Fetch movie data from the API
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    const movies = data.results;

    // Select the UL#list_movies element
    const listMovies = $('#list_movies');

    // Iterate through each movie and append a new LI element to the list
    movies.forEach(function(movie) {
      const movieTitle = movie.title;
      listMovies.append($('<li>').text(movieTitle));
    });
  });
});
