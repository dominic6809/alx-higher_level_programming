-- Task 17: Convert hbtn_0c_0 database, first_table table, and name field to UTF8

USE `hbtn_0c_0`
-- Convert hbtn_0c_0 database
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Convert first_table table
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
