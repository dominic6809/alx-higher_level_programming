-- Task 13: List all genres from hbtn_0d_tvshows with the number of shows linked to each

SELECT 
    tv_show_genres.genre_id AS genre,
    COUNT(tv_show_genres.tv_show_id) AS number_of_shows
FROM 
    tv_show_genres
GROUP BY 
    tv_show_genres.genre_id
ORDER BY 
    number_of_shows DESC;
