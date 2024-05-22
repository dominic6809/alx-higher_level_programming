-- Task 19: List all shows from hbtn_0d_tvshows_rate by their rating

SELECT 
    tv_shows.title, 
    SUM(tv_show_ratings.rating) AS rating
FROM 
    tv_shows
JOIN 
    tv_show_ratings ON tv_shows.id = tv_show_ratings.tv_show_id
GROUP BY 
    tv_shows.title
ORDER BY 
    rating DESC;
