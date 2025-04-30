USE pratice;

CREATE TABLE Employee(

EmployeeId  INT  primary key,
EmployeeName VARCHAR(20),
EmployeeSalary INT,
JoiningDate DATE

);
drop table  Employee;
INSERT INTO Employee (EmployeeId, EmployeeName, EmployeeSalary, JoiningDate) VALUES (1, 'sujon', 2000, '2024-04-01');
INSERT INTO Employee(EmployeeId,EmployeeName,EmployeeSalary,JoiningDate) VALUES(2,'ahemd',50000,'2024-3-02');
DELETE FROM Employee WHERE EmployeeId=1;
SET SQL_SAFE_UPDATES=0;
UPDATE Employee
SET EmployeeName="sujon ahmed"
WHERE EmployeeId=2;
 select * from Employee;