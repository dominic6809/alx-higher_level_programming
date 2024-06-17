-- Task 15: List all Comedy shows from hbtn_0d_tvshows
-- Select the titles of Comedy shows
-- Use INNER JOINs to link genres, show genres, and shows
-- Filter the results to only include shows with the genre "Comedy"
-- Order the results by the show title in ascending order
SELECT
    tv_shows.title
    FROM
    tv_shows
    INNER JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
    INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
    WHERE tv_genres.name = "Comedy"
    ORDER BY tv_shows.title;
