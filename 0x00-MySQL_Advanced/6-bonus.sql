-- a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.
-- Procedure AddBonus is taking 3 inputs (in this order):
-- user_id, a users.id value (you can assume user_id is linked to an existing users)
-- project_name, a new or already exists projects - if no projects.name found in the table, you should create it
-- score, the score value for the correction

DELIMITER $$

CREATE PROCEDURE AddBonus(user_id INTEGER, project_name VARCHAR(255), score INTEGER)
BEGIN

	INSERT INTO projects(name)VALUES(project_name);
	SET @latest_project = LAST_INSERT_ID();
	INSERT INTO corrections VALUES(user_id, @latest_project, score);
END$$
DELIMITER ;
