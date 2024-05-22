-- Task 5:  script that Create the table unique_id
-- with specified description if it doesn't already exist

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
