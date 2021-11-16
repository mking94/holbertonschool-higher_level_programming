-- Deletes the database hbtn_0c_0
IF EXISTS (SELECT name FROM master.dbo.sysdatabases WHERE name = N’hbtn_0c_0’) THEN
DROP DATABASE `hbtn_0c_0`;
