CREATE database CarDealer;
use CarDealer;


create table user_(
	username varchar(20) not null,
    nameAndSurname varchar(35),
    address varchar(20),
    email varchar(25),
    password_ varchar(20),
    phone varchar(15),
    constraint user_pk primary key (username)
    );
    

create table car (
	vehicleID varchar(200) not null,
    make varchar(30),
	model varchar(30),
    description_ varchar(50),
    fuel varchar(15),
    image varchar(200),
    price int,
    power_ varchar(15),
    mileage int,
    date_ datetime,
    username varchar(20),
    constraint car_pk primary key (vehicleID),
    constraint car_to_user foreign key(username) references user_(username)
    );
    
    create table favorite(
		username varchar(20),
        vehicleID varchar(200),
        constraint favorite_pk primary key (username, vehicleID),
		constraint fav_to_user foreign key(username) references user_(username),
		constraint fav_to_car foreign key(vehicleID) references car(vehicleID)

	);
	
        
alter table car modify description_ varchar(200);

delete from car where price=0;

select * from car;

SELECT COUNT(*) 
FROM car;


insert into user_ (username,nameAndSurname,address,email,password_,phone) values ('abdullabakija','Abdulla Bakija','Recica','a.bakija98@gmail.com','dullo123','070222333');
insert into user_ (username,nameAndSurname,address,email,password_,phone) values ('agniramadani','Agni Ramadani','Cellopek','aramadani@gmail.com','agni123','070332333');


use CarDealer;