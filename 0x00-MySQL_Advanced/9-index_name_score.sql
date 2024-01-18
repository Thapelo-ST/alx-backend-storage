-- Creating an index idx_name_first_score on the first letter of the name column and the score column
-- This script is intended for MySQL

CREATE INDEX idx_name_first_score ON names (LEFT(name, 1), score);
