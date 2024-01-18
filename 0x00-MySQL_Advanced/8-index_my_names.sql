-- Creating an index idx_name_first on the first letter of the name column
-- This script is intended for MySQL

CREATE INDEX idx_name_first ON names (LEFT(name, 1);
