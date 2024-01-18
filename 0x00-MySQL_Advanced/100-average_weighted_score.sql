-- Creating a stored procedure ComputeAverageWeightedScoreForUser
-- This script is intended for MySQL

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id_param INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_weight INT;
    DECLARE average_score FLOAT;

    SELECT SUM(corrections.score * projects.weight) INTO total_score, SUM(projects.weight) INTO total_weight
    FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id_param;

    IF total_weight > 0 THEN
        SET average_score = total_score / total_weight;
    ELSE
        SET average_score = 0;
    END IF;

    UPDATE users SET average_score = average_score WHERE id = user_id_param;
END //

DELIMITER ;
