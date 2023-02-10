-- a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	UPDATE users as u,
	(SELECT u.id, SUM(score * weight) / SUM(weight) AS w_avg
	FROM users AS u JOIN corrections AS c ON u.id=c.user_id
	JOIN projects AS p ON c.project_id=p.id GROUP BY u.id) AS wavg
	SET u.average_score = wavg.w_avg
	WHERE u.id=wavg.id;
END $$
DELIMITER ;
