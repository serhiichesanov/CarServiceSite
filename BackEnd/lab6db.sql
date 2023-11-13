use mydb;

CREATE TABLE `User` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`username` varchar(255) NOT NULL,
	`firstname` varchar(255) NOT NULL,
	`lastname` varchar(255) NOT NULL,
	`email` varchar(255) NOT NULL,
	`password` varchar(255) NOT NULL,
	`phone` varchar(255) NOT NULL,
	`userStatus`  NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Admin` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`adminRigths` varchar(255) NOT NULL,
	`password` varchar(255) NOT NULL,
	`user_id` INT NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Car` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`model` varchar(255) NOT NULL,
	`colot` varchar(255) NOT NULL,
	`seatnum` INT NOT NULL,
	`tankvolume` FLOAT NOT NULL,
	`maxspeed` FLOAT NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Rent` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`audience` INT,
	`user_id` INT NOT NULL,
	`amountofHours` INT NOT NULL,
	`dateTimeOfReservation` TIMESTAMP NOT NULL,
	`dateTimeOfEndReservation` TIMESTAMP NOT NULL,
	`status` VARCHAR(255) NOT NULL,
	PRIMARY KEY (`id`)
);

ALTER TABLE `Admin` ADD CONSTRAINT `Admin_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User`(`id`);

ALTER TABLE `Rent` ADD CONSTRAINT `Rent_ibfk_2` FOREIGN KEY (`audience`) REFERENCES `Car`(`id`);

ALTER TABLE `Rent` ADD CONSTRAINT `Rent_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `User`(`id`);





