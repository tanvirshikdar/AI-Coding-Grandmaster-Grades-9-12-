CREATE TABLE IF NOT EXISTS Employees (
    Emp_ID TEXT PRIMARY KEY,
    Emp_Name TEXT,
    Department TEXT,
    Salary INTEGER,
    City TEXT
);

INSERT INTO Employees (Emp_ID, Emp_Name, Department, Salary, City) VALUES
('E001', 'John Doe', 'Finance', 50000, 'New York'),
('E002', 'Jane Smith', 'IT', 60000, 'London'),
('E003', 'Tarun Sethi', 'Management', 75000, 'Delhi'),
('E004', 'Richard Roe', 'Sales', 45000, 'Paris'),
('E005', 'Sara Wilson', 'Finance', 52000, 'London');

SELECT * FROM Employees;

SELECT * FROM Employees 
WHERE Department = 'Finance';

SELECT Emp_Name, Department 
FROM Employees 
WHERE City = 'London';