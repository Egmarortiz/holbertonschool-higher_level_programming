-- create_hbtn_0d_usa.sql

-- 1) Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- 2) Switch into that database
USE hbtn_0d_usa;

-- 3) Create the states table if it doesn't already exist
CREATE TABLE IF NOT EXISTS states (
  id   INT              NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(256)     NOT NULL
);
