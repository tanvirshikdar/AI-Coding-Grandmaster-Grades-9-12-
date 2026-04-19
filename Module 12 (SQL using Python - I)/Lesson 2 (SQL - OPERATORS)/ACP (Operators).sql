CREATE TABLE IF NOT EXISTS CUSTOMER (
    customer_id TEXT PRIMARY KEY,
    cust_name TEXT,
    city TEXT,
    grade INTEGER,
    salesman_id TEXT
);

INSERT INTO CUSTOMER (customer_id, cust_name, city, grade, salesman_id) VALUES
('3002', 'Nick Rimando', 'New York', 100, '5001'),
('3007', 'Brad Davis', 'New York', 200, '5001'),
('3005', 'Graham Zusi', 'California', 200, '5002'),
('3008', 'Julian Green', 'London', 300, '5002'),
('3004', 'Fabian Johns', 'Paris', 300, '5006'),
('3009', 'Geoff Cameron', 'Berlin', 100, '5003'),
('3003', 'Jozy Altidor', 'Moscow', 200, '5007'),
('3001', 'Brad Guzan', 'London', NULL, '5005');

SELECT * FROM CUSTOMER WHERE city = 'New York' OR grade > 100;

SELECT * FROM CUSTOMER WHERE city = 'New York' AND grade > 100;