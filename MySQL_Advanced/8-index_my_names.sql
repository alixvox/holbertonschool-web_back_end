-- 8-index_my_names.sql
-- Indexes names starting with the first letter.

ALTER TABLE names
ADD COLUMN name_first_letter CHAR(1) GENERATED ALWAYS AS (LEFT(name, 1)) STORED;

CREATE INDEX idx_name_first_score ON names (name_first_letter, score);
