-- 9-index_name_score.sql
-- Add column for first letter of name

ALTER TABLE names
ADD COLUMN name_first_letter CHAR(1) GENERATED ALWAYS AS (LEFT(name, 1)) STORED;
CREATE INDEX idx_name_first_score ON names (name_first_letter, score);
