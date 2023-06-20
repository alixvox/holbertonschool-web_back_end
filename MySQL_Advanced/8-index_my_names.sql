-- 8-index_my_names.sql
-- Indexes names starting with the first letter.

CREATE INDEX idx_name_first ON names (name(1));
