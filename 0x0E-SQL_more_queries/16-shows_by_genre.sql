-- Task 16: List all shows and their linked genres from hbtn_0d_tvshows

SELECT 
    tv_shows.title, 
    tv_genres.name
FROM 
    tv_shows
LEFT JOIN 
    tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
LEFT JOIN 
    tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY 
    tv_shows.title, tv_genres.name;
