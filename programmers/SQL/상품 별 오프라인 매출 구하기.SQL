-- 코드를 입력하세요
SELECT P.PRODUCT_CODE,  (P.PRICE * SUM(OFF.SALES_AMOUNT)) AS  SALES
FROM PRODUCT P JOIN OFFLINE_SALE OFF ON P.PRODUCT_ID = OFF.PRODUCT_ID
group by p.product_code
having SALES is not null
order by SALES desc, p.product_code
