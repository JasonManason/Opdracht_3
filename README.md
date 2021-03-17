This project is for educational purposes only.

# Recommendation engine:
The goal of this project is to create two seperate recommendation algoritms that create different tables with data.


## Content filtering:
A filter based on sub_sub_category and if the product has a promo.
Every sub_sub_category gets its own recommendation table named 'rec_<sub_sub_category name>'
Each of these tables contains 4 records (if there are as many) based on their sub_sub_category and IF they have a promo.
So there may be some cases in which there are less records.


## Collaborative filtering:
A filter based on similar people.
