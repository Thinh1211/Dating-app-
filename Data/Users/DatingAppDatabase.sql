DROP database IF EXISTS DatingApp;
CREATE database IF NOT EXISTS DatingApp;
USE DatingApp;

CREATE TABLE User_information (
User_name TEXT DEFAULT NULL,
User_dob TEXT DEFAULT NULL,
User_gender TEXT DEFAULT NULL,
User_location TEXT DEFAULT NULL,
User_bio TEXT DEFAULT NULL
);

CREATE TABLE User_account (
Account_username TEXT DEFAULT NULL,
Account_password TEXT DEFAULT NULL
);

CREATE TABLE User_basics (
Basics_height TEXT DEFAULT NULL,
Basics_weight TEXT DEFAULT NULL,
Basics_zodiac TEXT DEFAULT NULL,
Basics_education TEXT DEFAULT NULL,
Basics_workout TEXT DEFAULT NULL,
Basics_smoke TEXT DEFAULT NULL,
Basics_drink TEXT DEFAULT NULL
);

CREATE TABLE User_interests (
Interests_sports TEXT DEFAULT NULL,
Interests_creativity TEXT DEFAULT NULL,
Interests_goingout TEXT DEFAULT NULL,
Interests_stayingin TEXT DEFAULT NULL,
Interests_film_tv TEXT DEFAULT NULL,
Interests_reading TEXT DEFAULT NULL,
Interests_music TEXT DEFAULT NULL,
Interests_food TEXT DEFAULT NULL,
Interests_travelling TEXT DEFAULT NULL,
Interests_pet TEXT DEFAULT NULL
);

DELIMITER $$
CREATE PROCEDURE New_User
(IN User_name VARCHAR(100), IN User_dob TEXT, IN User_gender VARCHAR(100), IN User_location VARCHAR(100),
IN User_bio VARCHAR(100), IN Account_username VARCHAR(100), IN Account_password VARCHAR(100),
IN Basics_height VARCHAR(100), IN Basics_weight VARCHAR(100), IN Basics_zodiac VARCHAR(100),
IN Basics_education VARCHAR(100), IN Basics_workout VARCHAR(100), IN Basics_smoke VARCHAR(100),
IN Basics_drink VARCHAR(100), IN Interests_sports VARCHAR(100), IN Interests_creativity VARCHAR(100),
IN Interests_goingout VARCHAR(100), IN Interests_stayingin VARCHAR(100), IN Interests_film_tv VARCHAR(100),
IN Interests_reading VARCHAR(100), IN Interests_music VARCHAR(100), IN Interests_food VARCHAR(100),
IN Interests_travelling VARCHAR(100), IN Interests_pet VARCHAR(100))
BEGIN
INSERT INTO User_information (User_name, User_dob, User_gender, User_location, User_bio)
VALUES (User_name, User_dob, User_gender, User_location, User_bio);
INSERT INTO User_account (Account_username, Account_password)
VALUES (Account_username, Account_password);
INSERT INTO User_basics (Basics_height, Basics_weight, Basics_zodiac, Basics_education,
Basics_workout, Basics_smoke, Basics_drink)
VALUES (Basics_height, Basics_weight, Basics_zodiac, Basics_education,
Basics_workout, Basics_smoke, Basics_drink);
INSERT INTO User_interests (Interests_sports, Interests_creativity, Interests_goingout, 
Interests_stayingin, Interests_film_tv, Interests_reading, Interests_music, Interests_food,
Interests_travelling, Interests_pet)
VALUES (Interests_sports, Interests_creativity, Interests_goingout, 
Interests_stayingin, Interests_film_tv, Interests_reading, Interests_music, Interests_food,
Interests_travelling, Interests_pet);
END $$

CALL New_user ('Nguyen Duy Anh Tung', '2003-07-20', 'Male', 'Hanoi', 'thisisbio', 'anhtung207', 'pass123', '1m77', '62kg', 'Cancer', 'College',
 'Gym', 'Sometimes', 'Coffee', 'Basketball', 'Drawing', 'Usually', 'Sometimes', 'Action', 'Manga', 'RnB', 'Pho', 'Beach', 'Dogs & Cats');
<<<<<<< HEAD
 
 SELECT * FROM User_information;
 SELECT * FROM User_account;
 SELECT * FROM User_basics;
 SELECT * FROM User_interests;
 
=======

 SELECT * FROM User_information;
 SELECT * FROM User_account;
 SELECT * FROM User_basics;
 SELECT * FROM User_interests;
>>>>>>> 3efd7594bf85f60c1e86246a812e3abcdb19bd09