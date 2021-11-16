-- Deletes the database hbtn_0c_0
IF EXISTS (SELECT name FROM master.dbo.sysdatabases WHERE name = ’hbtn_0c_0’)
BEGIN
DROP DATABASE `hbtn_0c_0`
END
