-- a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student
-- Procedure ComputeAverageScoreForUser is taking 1 input:
-- user_id, a users.id value (you can assume user_id is linked to an existing users)
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN
	DECLARE weighted_avg_score FLOAT;
	SET weighted_avg_score = (SELECT SUM(score * weight) / SUM(weight) 
				  FROM users AS u
				  JOIN corrections AS c ON u.id=c.user_id
				  JOIN projects AS p ON c.project_id=p.id
				  WHERE u.id=user_id);
	UPDATE users SET average_score = weighted_avg_score WHERE id=user_id;
END $$
DELIMITER ;
