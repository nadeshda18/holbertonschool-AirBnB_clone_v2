-- Create database if not exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create user if not exists
<<<<<<< HEAD
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
=======
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';

-- Set password for user
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';

-- grant usage
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';
>>>>>>> master

-- Grant privileges to the user for the specified database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on performance_schema database
<<<<<<< HEAD
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
=======
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
>>>>>>> master
