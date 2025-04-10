create database DataAnalytics;

use DataAnalytics;

create table person(
person_id int,
firstname varchar(20),
lastname varchar(20),
address varchar(20),
city varchar(20)
);

insert into person values(1,"Gowthami","chillimuntha","hostel","chennai");

insert into person values(2,"Gayathri","chillimuntha","hostel","vjvd"),(3,"sweety","ch","hostel","hyd");


select * from person;


delete from person where person_id=3;


update person set firstname="ch" where person_id=1;






create table users(
userId int auto_increment primary key, 
username varchar(50) unique not null,
email varchar(200) unique not null,
passwordhash varchar(200)not null,
firstname varchar(50),
lastname varchar(50),
dateofbirth date,
createdAt Datetime default current_timestamp,
lastlogin datetime,
status enum ('active','inactive','suspended') default 'active',
index(email)
);


insert into users values(1, "Gowthami", "gowthami@gmil.com", "gowthami@123", "ch", "gowthami", "2002-04-08", "2024-08-07", "2024-08-07", "active");


select * from users;


create table students(
student_id int primary key,
name varchar(100),
age int,
check(age>18)
);




create table enrollements(
enrollment_id int primary key,
student_id int,
course_id int,
foreign key (student_id) references students(student_id)
);

insert into enrollements values(1,1,1);

select * from enrollements;

insert into students values(1,"gowthami",19);

insert into students values(2,"gayathri",19);

select * from students;


create table OrderDetails(
order_id int,
product_id int,
quantity int,
primary key(order_id,product_id)
);


insert into OrderDetails values(1,1,10);

select * from OrderDetails;

Drop table person;

truncate table person;



create table products(productid int,productname varchar(20),price int);



insert into products values(1,"mobile",300000),(2,"mobile2",40000);

insert into products values(1,"mobile",500000),(2,"mobile2",40000);


select * from products;

select max(price)
from products;

select min(price)
from products;

select min(price) as small_price
from products
group by productid;

select max(price) as small_price,productid
from products
group by productid;



select avg(price) as small_price,productid
from products
group by productid;


select count(*) as numberOfColumns
from products;


select count(productid)
from products
where price>2000;


select count(distinct price)
from products;



select sum(price)
from products;


create table customers(customerid int primary key,
name varchar(100)
);

create table orders(
order_id int primary key,
customerid int,
product varchar(100),
foreign key(customerid) references customers(customerid)
on delete cascade
);

insert into customers values(1,"Gowthami"),(2,"gayathri"),(3,"sweety");

insert into orders values(101,1,"laptop");


insert into orders values(102,2,"mobile"),(103,3,"cycle");

select * from customers;

select * from orders;

select * from students;

select * from orders
order by product desc;

select * from orders
order by product asc,order_id desc;  



select * from orders
order by product ;
delete from customers where customerid=1;



CREATE TABLE Customerstable (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    ContactName VARCHAR(100),
    Country VARCHAR(50)
);
 
CREATE TABLE Orderstable (
    OrderID INT PRIMARY KEY,
    OrderDate DATE,
    CustomerID INT,
    Amount DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES Customerstable(CustomerID)
);
 
INSERT INTO Customerstable (CustomerID, CustomerName, ContactName, Country) VALUES
(1, 'John Doe', 'John D.', 'USA'),
(2, 'Jane Smith', 'Jane S.', 'UK'),
(3, 'Alice Brown', 'Alice B.', 'Canada'),
(4, 'Bob Johnson', 'Bob J.', 'Australia');
 
INSERT INTO Orderstable (OrderID, OrderDate, CustomerID, Amount) VALUES
(101, '2024-09-01', 1, 250.00),
(102, '2024-09-05', 2, 300.00),
(103, '2024-09-07', 1, 150.00),
(104, '2024-09-10', 3, 450.00);


select * from Customerstable;

select * from Orderstable;


select 
	Customerstable.CustomerID,
    Customerstable.CustomerName,
    Orderstable.OrderID,
    Orderstable.OrderDate,
    Orderstable.Amount
from
	Customerstable
Inner join
	Orderstable on Customerstable.CustomerID=Orderstable.CustomerID;


select 
	Customerstable.CustomerID,
    Customerstable.CustomerName,
    Orderstable.OrderID,
    Orderstable.OrderDate,
    Orderstable.Amount
from
	Customerstable
left join
	Orderstable on Customerstable.CustomerID=Orderstable.CustomerID;



select 
	Customerstable.CustomerID,
    Customerstable.CustomerName,
    Orderstable.OrderID,
    Orderstable.OrderDate,
    Orderstable.Amount
from
	Customerstable
right join
	Orderstable on Customerstable.CustomerID=Orderstable.CustomerID;



select 
	Customerstable.CustomerID,
    Customerstable.CustomerName,
    Orderstable.OrderID,
    Orderstable.OrderDate,
    Orderstable.Amount
from
	Customerstable
join
	Orderstable on Customerstable.CustomerID=Orderstable.CustomerID;



create table drink(id int,name varchar(20));

create table snacks(id int,name varchar(20));

insert into drink values(1,"tea"),(2,"coffee");
insert into snacks values(1,"biscuits"),(2,"cake");


select drink.name,snacks.name
from drink
cross join 
snacks on drink.id=snacks.id;
