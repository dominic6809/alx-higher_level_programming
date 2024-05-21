-- Task 17: Convert hbtn_0c_0 database, first_table table, and name field to UTF8

-- Convert hbtn_0c_0 database
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Convert first_table table
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- convert name field to UTF8
ALTER TABLE first_table MODIFY COLUMN name VARCHAR(256)
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
