-- Stored Procedure ComputeAverageWeightedScoreForUsers
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_id_param INT;
    
    -- Declare cursor for all users
    DECLARE user_cursor CURSOR FOR SELECT id FROM users;
    
    -- Declare variables
    DECLARE done INT DEFAULT FALSE;
    DECLARE weighted_score FLOAT;
    DECLARE total_weight FLOAT;

    -- Declare handlers
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Open cursor
    OPEN user_cursor;

    -- Start looping through users
    user_loop: LOOP
        -- Fetch user_id from cursor
        FETCH user_cursor INTO user_id_param;

        -- Check if done fetching
        IF done THEN
            LEAVE user_loop;
        END IF;

        -- Initialize variables
        SET weighted_score = 0;
        SET total_weight = 0;

        -- Calculate weighted score for each project
        SELECT SUM(corrections.score * projects.weight) INTO weighted_score,
               SUM(projects.weight) INTO total_weight
        FROM corrections
        JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id_param;

        -- Update average_score in the users table
        UPDATE users
        SET average_score = IFNULL(weighted_score / NULLIF(total_weight, 0), 0)
        WHERE id = user_id_param;
    END LOOP;

    -- Close cursor
    CLOSE user_cursor;
END //

DELIMITER ;
