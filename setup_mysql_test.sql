-- creates a database hbnb_test_db
-- creates a new user hbnb_test in localhost
-- password for hbnb_test set to hbnb_test_pwd
-- hbnb_test should have all privileges on db hbnb_test_db
-- grants hbnb_test SELECT privileges on database performance schema

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER
       IF NOT EXISTS 'hbnb_test'@'localhost'
       IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES
      ON `hbnb_test_db`.*
      TO 'hbnb_test'@'localhost'
      IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT
      ON `performance_schema`.*
      TO 'hbnb_test'@'localhost'
      IDENTIFIED BY 'hbnb_test_pwd';
FLUSH PRIVILEGES;
