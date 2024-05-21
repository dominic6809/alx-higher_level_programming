-- Task 16: List all records of the table second_table excluding rows
-- without a name value, ordered by descending score
-- The database name will be passed as an argument to the mysql command

SELECT score, name FROM second_table
WHERE name IS NOT NULL ORDER BY score DESC;
