-- Create a table `users` with specific attributes
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL
);

-- Insert sample data
INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");
INSERT INTO users (email, name) VALUES ("sylvie@dylan.com", "Sylvie");
INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Jean");
