-- Task 4: Create the table id_not_null with specified description if it doesn't already exist

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256) NOT NULL
);
