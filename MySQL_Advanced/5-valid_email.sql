-- 5-valid_email.sql
-- This resets the valid_email boolean when a user's email is updated.

DELIMITER //
CREATE TRIGGER email_change
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
   IF NEW.email <> OLD.email THEN
      SET NEW.valid_email = 0;
   END IF;
END;//
DELIMITER ;
