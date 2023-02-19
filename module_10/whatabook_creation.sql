/*
    Title: whatabook.creation.sql
    Author: Rebecca Robinson
    Date: 02.19.2023
    Description: Creating the WhatABook user and tables.
*/

-- Drop for duplicate protection
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- Create user
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- Apply privileges to user for database
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- Drop for duplicate protection
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- Drop for duplicate protection
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

-- Store table creation
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

-- Book table creation
CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

-- User table creation
CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

-- Wishlist table creation
CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

-- Insert a store location
INSERT INTO store(locale)
    VALUES('2701 Monroe St, Madison, WI 53711');

-- Insert books
INSERT INTO book(book_name, author, details)
    VALUES('The Eye of the World', 'Robert Jordan', 'First Book of the Wheel of Time');

INSERT INTO book(book_name, author, details)
    VALUES('The Great Hunt', 'Robert Jordan', 'Second Book of the Wheel of Time');

INSERT INTO book(book_name, author, details)
    VALUES('The Dragon Reborn', 'Robert Jordan', 'Third Book of the Wheel of Time');

INSERT INTO book(book_name, author, details)
    VALUES('The Shadow Rising', 'Robert Jordan', 'Fourth Book of the Wheel of Time');

INSERT INTO book(book_name, author, details)
    VALUES('The Fires of Heaven', 'Robert Jordan', 'Fifth Book of the Wheel of Time');

INSERT INTO book(book_name, author, details)
    VALUES("Lord of Chaos", 'Robert Jordan', 'Sixth Book of the Wheel of Time');

INSERT INTO book(book_name, author, details)
    VALUES('A Crown of Swords', 'Robert Jordan', 'Seventh Book of the Wheel of Time');

INSERT INTO book(book_name, author, details)
    VALUES('The Path of Daggers', 'Robert Jordan', 'Eighth Book of the Wheel of Time');

INSERT INTO book(book_name, author, details)
    VALUES("Winter's Heart", 'Robert Jordan', 'Ninth Book of the Wheel of Time');

-- Insert user
INSERT INTO user(first_name, last_name) 
    VALUES('Rand', "al'Thor");

INSERT INTO user(first_name, last_name)
    VALUES('Mat', 'Cauthon');

INSERT INTO user(first_name, last_name)
    VALUES('Perrin', 'Aybara');

-- Insert into wishlist
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Rand'), 
        (SELECT book_id FROM book WHERE book_name = 'The Eye of the World')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Mat'),
        (SELECT book_id FROM book WHERE book_name = 'The Path of Daggers')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Perrin'),
        (SELECT book_id FROM book WHERE book_name = 'The Great Hunt')
    );
