--  a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the
-- average score for a student. 
-- An average score can be a decimal
-- The Procedure ComputeAverageScoreForUser takes 1 input:
    -- user_id, a users.id value (you can assume user_id is linked to an existing users)

DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INTEGER)
BEGIN
	DECLARE averageScore FLOAT;
	SET averageScore = (SELECT AVG(score) FROM corrections where corrections.user_id = user_id);
	UPDATE users
	SET average_score = averageScore
	WHERE id = user_id;
END$$
DELIMITER ;
