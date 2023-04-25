/*CREATE DATABASE new_phonebook;
USE new_phonebook;
CREATE TABLE new_phonebook
(
Id INT PRIMARY KEY NOT NULL,
ProductName VARCHAR(30) NOT NULL,
Manufacturer VARCHAR(40),
ProductCount VARCHAR(40) NOT NULL,
Price  VARCHAR(30)
);
*/

INSERT new_phonebook
(
Id, ProductName, Manufacturer, ProductCount, Price
)
VALUES 
(1, "IPhone X", "Apple", "3", "76000"),
(2, "IPhone 8", "Apple", "2", "51000"),
(3, "Galaxy S9", "Samsung", "2", "56000"),
(4, "Galaxy S8", "Samsung", "1", "41000"),
(5, "P20 Pro", "Huawei", "5", "36000");

/*Выведите название, производителя и цену для товаров, количество которых превышает 2*/
SELECT ProductName, Manufacturer, Price FROM new_phonebook WHERE ProductCount > 2;

/* Выведите весь ассортимент товаров марки “Samsung”*/

SELECT * FROM new_phonebook WHERE Manufacturer = "Samsung";
