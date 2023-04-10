-- Creating a table user that has 3 columns
-- email unique and not null, name

-- Drop the table if it exists
DROP TABLE IF EXISTS `users`;

-- Create the table
CREATE TABLE IF NOT EXISTS `users` (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
