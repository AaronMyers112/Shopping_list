
/* Creating the database */
CREATE DATABASE IF NOT EXISTS Shopping_List;

USE Shopping_List;


/* Creating the fundementals table */
DROP TABLE IF EXISTS Fundementals;

CREATE TABLE Fundementals( 
amount INT DEFAULT 0,
name VARCHAR(20) NOT NULL,
cost DOUBLE NOT NULL,
required VARCHAR(10) DEFAULT 'Yes');


/* Creating the luxuries table */
DROP TABLE IF EXISTS Luxeries;

CREATE TABLE Luxeries(
amount INT DEFAULT 0,
name VARCHAR(20) NOT NULL,
cost DOUBLE NOT NULL);
