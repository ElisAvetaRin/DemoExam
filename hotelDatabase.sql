create database HotelDatabase;
use HotelDatabase;
create table users(
	id int auto_increment primary key,
    name varchar(100),
    password varchar(100)
);