-- a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.
-- Procedure AddBonus is taking 3 inputs (in this order):
-- user_id, a users.id value (you can assume user_id is linked to an existing users)
-- project_name, a new or already exists projects - if no projects.name found in the table, you should create it
-- score, the score value for the correction

DELIMITER $$

CREATE PROCEDURE AddBonus(user_id INTEGER, project_name VARCHAR(255), score INTEGER)
BEGIN

	INSERT INTO projects(name)
	SELECT * FROM (SELECT project_name) As tmp 
	WHERE NOT EXISTS (
		SELECT name FROM projects WHERE name = project_name
	) LIMIT 1;
	 SET @projectID = (SELECT id FROM projects WHERE name=project_name);
	INSERT INTO corrections VALUES(user_id, @projectID, score);
END$$
DELIMITER ;

