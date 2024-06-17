-- Task 8: List all the cities of California from the database hbtn_0d_usa, sorted by cities.id
-- First, ensure you're using the correct database
-- Then, select cities where the state_id corresponds to the id of California
SELECT id, name 
FROM cities
WHERE state_id = (
    SELECT id 
    FROM states 
    WHERE name = 'California'
)
ORDER BY id ASC;
