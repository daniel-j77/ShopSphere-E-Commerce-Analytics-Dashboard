SELECT Region,
SUM(Sales) Revenue
FROM ecommerce
GROUP BY Region;

SELECT Category,
SUM(Profit) Profit
FROM ecommerce
GROUP BY Category;

SELECT CustomerSegment,
SUM(Sales) Revenue
FROM ecommerce
GROUP BY CustomerSegment;

SELECT Returned,
COUNT(*) Orders
FROM ecommerce
GROUP BY Returned;