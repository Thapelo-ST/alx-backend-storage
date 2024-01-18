-- Creating a trigger to decrease the quantity of an item after adding a new order
-- This script is intended for MySQL

DELIMITER //
CREATE TRIGGER decrease_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    DECLARE new_quantity INT;

    -- Calculate the new quantity
    SET new_quantity = (
        SELECT quantity - NEW.number
        FROM items
        WHERE name = NEW.item_name
    );

    -- Update the quantity in the items table
    UPDATE items
    SET quantity = new_quantity
    WHERE name = NEW.item_name;
END //
DELIMITER ;

