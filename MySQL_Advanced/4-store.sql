-- 4-store.sql
-- This computes an item's quantity after an order is placed.

DELIMITER $$
CREATE TRIGGER after_order_insert
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
   UPDATE items
   SET quantity = quantity - NEW.number
   WHERE name = NEW.item_name;
END $$
DELIMITER ;
