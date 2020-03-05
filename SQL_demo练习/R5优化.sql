从日期下手
1.获得日期大一些的订单，这样每个用户的第一单就是第二笔出售
SELECT
	o2.order_id,
 	o2.item_id,
 	o2.seller_id,
 	MAX(o2.order_date),
	i.item_brand
FROM 
	orders o1 JOIN
	orders o2
ON o1.seller_id=o2.seller_id and o1.order_date<o2.order_date
JOIN items i ON i.item_id=o2.item_id
GROUP BY o2.seller_id


最终结果
SELECT
	u.user_id seller_id,
	(CASE WHEN u.favorite_brand=second_item.item_brand THEN 'yes' ELSE 'no' END) 2nd_item_fav_brand
FROM
	users u 
	LEFT JOIN 
		(SELECT
 			o2.seller_id,
			i.item_brand
		FROM 
			orders o1 JOIN
			orders o2
		ON o1.seller_id=o2.seller_id and o1.order_date<o2.order_date
		JOIN items i ON i.item_id=o2.item_id
		GROUP BY o2.seller_id
		) second_item
	ON u.user_id=second_item.seller_id



---------------------------------------------------------------------------
第二种方法：
SELECT
	u.user_id seller_id,
	(
		CASE
		WHEN u.user_id = 2nd_favorite_users.user_id THEN
			'yes'
		ELSE
			'no'
		END
	) 2nd_item_fav_brand
FROM
	users u
LEFT JOIN (
	SELECT
		u.user_id
	FROM
		users u
	LEFT JOIN items i ON u.favorite_brand = i.item_brand
	LEFT JOIN (
		SELECT
			order_date,
			item_id,
			seller_id,
			@row_num := (
				CASE
				WHEN seller_id =@seller_id THEN
					@row_num :=@row_num + 1
				ELSE
					1
				END
			) row_num,
			@seller_id := seller_id
		FROM
			(
				SELECT
					order_date,
					item_id,
					seller_id
				FROM
					orders
				ORDER BY
					seller_id,
					order_date
			) sell_order,
			(
				SELECT
					@seller_id := 0,
					@row_num := 0
			) variable
	) sells_order ON u.user_id = sells_order.seller_id
	WHERE
		i.item_id = sells_order.item_id
	AND row_num = 2
) 2nd_favorite_users ON u.user_id = 2nd_favorite_users.user_id
