#sql도 종종 짜보긴 해야할듯
SELECT t1.CART_ID FROM CART_PRODUCTS as t1, CART_PRODUCTS as t2
WHERE t1.CART_ID = t2.CART_ID AND
t1.Name = 'Milk' and t2.Name = 'Yogurt';