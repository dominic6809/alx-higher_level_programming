-- Task 3: Create the table force_name with specified description if it doesn't already exist

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
