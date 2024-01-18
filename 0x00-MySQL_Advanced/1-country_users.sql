-- Creating users table and inserting attributes
-- all will be tested using MySq

CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(225) NOT NULL UNIQUE,
        name VARCHAR(225),
	country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
