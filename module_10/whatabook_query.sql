/*
    Title: whatabook_query.sql
    Author: Rebecca Robinson
    Date: 02.17.2023
    Description: WhatABook Query
*/

-- View user wishlist
SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author
FROM wishlist
    INNER JOIN user ON wishlist.user_id = user.user_id
    INNER JOIN book ON wishlist.book_id = book.book_id
WHERE user.user_id = 1;

-- View location
SELECT store_id, locale from store;

-- View book list
SELECT book_id, book_name, author, details from book;
