-- Task 9: List all cities in the database hbtn_0d_usa with cities.id,
-- cities.name, and states.name, sorted by cities.id

SELECT 
    cities.id, 
    cities.name, 
    (SELECT states.name FROM states WHERE states.id = cities.state_id) AS state_name
FROM 
    cities
ORDER BY 
    cities.id ASC;
