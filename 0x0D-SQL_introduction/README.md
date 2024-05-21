# 0x0D. SQL - Introduction

## Table of Contents
1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Getting Started](#getting-started)
4. [Basic SQL Concepts](#basic-sql-concepts)
    - [Database](#database)
    - [Table](#table)
    - [Schema](#schema)
5. [Common SQL Commands](#common-sql-commands)
    - [SELECT](#select)
    - [INSERT](#insert)
    - [UPDATE](#update)
    - [DELETE](#delete)
6. [Examples](#examples)
7. [Resources](#resources)
8. [Requirements](#requirements)
9. [Tasks](#tasks)

## Overview

Structured Query Language (SQL) is a standard language for managing and manipulating relational databases. SQL is used to perform various operations on the data within a database, such as querying, updating, and managing the database schema.

## Prerequisites

Before starting with SQL, it is helpful to have a basic understanding of:
- Database concepts
- Basic programming principles

## Getting Started

To begin working with SQL, you need a database management system (DBMS). Popular DBMSs include:
- MySQL
- PostgreSQL
- SQLite
- Microsoft SQL Server
- Oracle Database

You can install any of these systems and use their respective tools to execute SQL commands.

## Basic SQL Concepts

### Database
A database is an organized collection of data, generally stored and accessed electronically from a computer system.

### Table
A table is a collection of related data entries and it consists of columns and rows.

### Schema
A schema is a blueprint or architecture of how a database is constructed. It defines how the data is organized and how the relationships among them are associated.

## Common SQL Commands

### SELECT
The `SELECT` statement is used to query the database and retrieve data.

```sql
-- Select all columns from the table
SELECT column1, column2 FROM table_name;
```
### INSERT
The INSERT statement is used to add new rows of data to a table.
```
-- Insert values into specific columns of the table
INSERT INTO table_name (column1, column2) VALUES (value1, value2);
```
### UPDATE
The UPDATE statement is used to modify existing data in a table.
```
-- Update specific columns of the table based on a condition
UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;
```
### DELETE
The DELETE statement is used to remove existing rows from a table.
```
-- Delete rows from the table based on a condition
DELETE FROM table_name WHERE condition;
```
## Examples
### Creating a Table
```
-- Create a table named Employees with specified columns
CREATE TABLE Employees (
    EmployeeID int,
    FirstName varchar(255),
    LastName varchar(255),
    BirthDate date
);
```
### Inserting Data into a Table
```
-- Insert a row into the Employees table
INSERT INTO Employees (EmployeeID, FirstName, LastName, BirthDate) VALUES (1, 'John', 'Doe', '1980-01-01');
```
### Querying Data from a Table
```
-- Select all rows from the Employees table where the last name is 'Doe'
SELECT * FROM Employees WHERE LastName = 'Doe';
```
### Updating Data in a Table
```
-- Update the first name of the employee with EmployeeID 1 to 'Jane'
UPDATE Employees SET FirstName = 'Jane' WHERE EmployeeID = 1;
```
### Deleting Data from a Table
```
-- Delete the employee with EmployeeID 1
DELETE FROM Employees WHERE EmployeeID = 1;
```
## Resources
For further learning, check out the following resources:

W3Schools SQL Tutorial
SQLBolt - Learn SQL
Khan Academy SQL Course
PostgreSQL Documentation
MySQL Documentation
