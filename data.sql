CREATE DATABASE cashier_app;

USE cashier_app;

CREATE TABLE product {
    id int NOT NULL AUTO_INCREMENT,
    name varchar(50),
    stock int,
    price bigint
    PRIMARY KEY (id)
}

INSERT INTO product VALUES (1, 'Nasi Ayam Sambal Matah', 3, 20000)
INSERT INTO product VALUES (1, 'Nasi Ayam Crispy Lada Hitam', 5, 25000)
INSERT INTO product VALUES (1, 'Strawberry Milkshake', 8, 8000)
INSERT INTO product VALUES (1, 'Nasi Kangkung', 7, 20000)
