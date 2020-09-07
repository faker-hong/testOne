给表添加外键
ALTER TABLE orders add CONSTRAINT `fk_item_id` FOREIGN KEY (`item_id`) REFERENCES items(`item_id`)

ALTER TABLE orders add CONSTRAINT `fk_buyer_id` FOREIGN KEY (`buyer_id`) REFERENCES users(`user_id`)

需求：找出用户出售的第二个产品是否是他们最爱的（可以保证每天最多只售卖一个产品）
出售产品小于2的都为no


1.统计卖出产品的个数
SELECT seller_id, COUNT(1) sell_num
FROM orders
GROUP BY seller_id

2.给每个人售卖次数排序标号
SELECT
	order_date,
	item_id,
	seller_id,
	@row_num:=(CASE WHEN seller_id=@seller_id THEN @row_num:=@row_num+1 ELSE 1 END) row_num,
	@seller_id:=seller_id
FROM
	(SELECT order_date, item_id, seller_id from orders ORDER BY seller_id, order_date) sell_order,
	(SELECT @seller_id:=0, @row_num:=0) variable

3.判断第二售卖产品是否为最爱品牌
SELECT 
	u.user_id
FROM
users u 
	LEFT JOIN items i 
		ON u.favorite_brand = i.item_brand
	LEFT JOIN (SELECT
							order_date,
							item_id,
							seller_id,
							@row_num:=(CASE WHEN seller_id=@seller_id THEN @row_num:=@row_num+1 ELSE 1 END) row_num,
							@seller_id:=seller_id
						FROM
							(SELECT order_date, item_id, seller_id from orders ORDER BY seller_id, order_date) sell_order,
							(SELECT @seller_id:=0, @row_num:=0) variable
						) sells_order
		ON u.user_id = sells_order.seller_id
WHERE i.item_id=sells_order.item_id and row_num=2


3.判断第二售卖产品是否为最爱品牌
SELECT
	sells_order.seller_id,
	(CASE WHEN u.favorite_brand=i.item_brand THEN 'yes' ELSE 'no' END) 2nd_item_fav_brand
FROM 
	users u LEFT JOIN	(SELECT
											order_date,
											item_id,
											seller_id,
											@row_num:=(CASE WHEN seller_id=@seller_id THEN @row_num:=@row_num+1 ELSE 1 END) row_num,
											@seller_id:=seller_id
										FROM
											(SELECT order_date, item_id, seller_id from orders ORDER BY seller_id, order_date) sell_order,
											(SELECT @seller_id:=0, @row_num:=0) variable
											) sells_order
ON sells_order.seller_id = u.user_id
JOIN items i ON i.item_id = sells_order.item_id
JOIN (SELECT seller_id, COUNT(1) sell_num
			FROM orders
			GROUP BY seller_id) item_count ON item_count.seller_id = sells_order.seller_id
WHERE sells_order.row_num=2
ORDER BY seller_id, order_date


最终结果1:
SELECT
	u.user_id seller_id,
	IF(result.2nd_item_fav_brand='yes', 'yes', 'no') 2nd_item_fav_brand
FROM users u
LEFT JOIN (SELECT
-- 						sells_order.order_date,
-- 						u.favorite_brand,
-- 						sells_order.row_num,
						sells_order.seller_id,
-- 						item_count.sell_num,
-- 						i.item_brand,
						(CASE WHEN u.favorite_brand=i.item_brand THEN 'yes' ELSE 'no' END) 2nd_item_fav_brand
					FROM 
						users u LEFT JOIN	(SELECT
																order_date,
																item_id,
																seller_id,
																@row_num:=(CASE WHEN seller_id=@seller_id THEN @row_num:=@row_num+1 ELSE 1 END) row_num,
																@seller_id:=seller_id
															FROM
																(SELECT order_date, item_id, seller_id from orders ORDER BY seller_id, order_date) sell_order,
																(SELECT @seller_id:=0, @row_num:=0) variable
																) sells_order
					ON sells_order.seller_id = u.user_id
					JOIN items i ON i.item_id = sells_order.item_id
					JOIN (SELECT seller_id, COUNT(1) sell_num
								FROM orders
								GROUP BY seller_id) item_count ON item_count.seller_id = sells_order.seller_id
					WHERE sells_order.row_num=2
					ORDER BY seller_id, order_date) result
ON u.user_id = result.seller_id


最终结果2:
SELECT
	u.user_id seller_id,
	(CASE WHEN u.user_id=2nd_favorite_users.user_id THEN 'yes' ELSE 'no' END) 2nd_item_fav_brand
FROM
	users u
		LEFT JOIN
	(SELECT 
			u.user_id
		FROM
		users u 
			LEFT JOIN items i 
				ON u.favorite_brand = i.item_brand
			LEFT JOIN (SELECT
									order_date,
									item_id,
									seller_id,
									@row_num:=(CASE WHEN seller_id=@seller_id THEN @row_num:=@row_num+1 ELSE 1 END) row_num,
									@seller_id:=seller_id
								FROM
									(SELECT order_date, item_id, seller_id from orders ORDER BY seller_id, order_date) sell_order,
									(SELECT @seller_id:=0, @row_num:=0) variable
								) sells_order
				ON u.user_id = sells_order.seller_id
		WHERE i.item_id=sells_order.item_id and row_num=2) 2nd_favorite_users
ON u.user_id=2nd_favorite_users.user_id