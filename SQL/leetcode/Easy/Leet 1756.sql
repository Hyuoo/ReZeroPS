/*
Solving Date    : 2024.03.16
Title           : 1757. Recyclable and Low Fat Products
tags            : select
url             : https://leetcode.com/problems/recyclable-and-low-fat-products/
*/

select product_id from Products
where low_fats = "Y" and recyclable = "Y"
;