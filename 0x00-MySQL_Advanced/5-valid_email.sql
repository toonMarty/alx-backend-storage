-- a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.
DELIMITER $$

CREATE TRIGGER validate_email_update BEFORE UPDATE
ON users FOR EACH ROW
BEGIN
	IF NOT (SELECT NEW.email REGEXP '^[a-zA-Z0-9][a-zA-Z0-9._-]*[a-zA-Z0-9._-]@[a-zA-Z0-9][a-zA-Z0-9._-]*[a-zA-Z0-9]\\.[a-zA-Z]{2,63}$') THEN
		SET NEW.valid_email = !NEW.valid_email;
	END IF;
END$$
DELIMITER ; 
