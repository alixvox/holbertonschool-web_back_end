-- 0.uniq_users.sql
-- Creates a users table if it does not exist.

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL,
  name VARCHAR(255),
  PRIMARY KEY(id),
  UNIQUE(email)
);
