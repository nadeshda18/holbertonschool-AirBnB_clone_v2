-- Create database if not exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create user if not exists
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';

-- Set password for user
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';

-- grant usage
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';

-- Grant privileges to the user for the specified database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
