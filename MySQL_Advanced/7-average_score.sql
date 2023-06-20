-- 7-average_score.sql
-- This updates the average score for a specific user.

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    UPDATE users AS u
    SET u.average_score = (
        SELECT AVG(c.score)
        FROM corrections AS c
        WHERE c.user_id = user_id
    )
    WHERE u.id = user_id;
END //
DELIMITER ;
