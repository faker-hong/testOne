create TABLE `Spending`(
`user_id` INT,
`spend_date` Date,
`platform` enum('desktop', 'mobile'),
`amount` INT,
PRIMARY KEY (`user_id`, `spend_date`, `platform`)
)

需求：
统计每天使用desktop，mobile，both方式的用户总数和金额总数

1.转换出result表结构
SELECT
	spend_date,
	platform
FROM
	(SELECT DISTINCT spend_date FROM spending) a,
	(SELECT 'desktop' platform
		UNION
		SELECT 'mobile'
		UNION 
		SELECT 'both') type_platform


2.取出每人每天不同方式购物有两条记录的人，也就是用了both方法的人
SELECT
	user_id,
	spend_date,
	platform,
	SUM(amount) amount
FROM
	spending
GROUP BY
	user_id, spend_date,platform


3.根据cnt为2来取出当天使用both方法的人
SELECT
	spend_date,
	'both' platform,
	count(1) total_users,
	SUM(amount) total_amount
FROM
	(SELECT
		user_id,
		spend_date,
		platform,
		COUNT(*) cnt,
		SUM(amount) amount
	FROM
		(SELECT
		user_id,
		spend_date,
		platform,
		SUM(amount) amount
	FROM
		spending
	GROUP BY
		user_id, spend_date,platform) every_day_diff_way
	GROUP BY
		user_id, spend_date
	) count_buy_ways
WHERE cnt=2
GROUP BY spend_date



4.与定义好的表结构left join填值,这里得到的是both的值
SELECT
	table_structure.spend_date,
	table_structure.platform,
	IFNULL(both_way.total_amount,0) total_amount,
	IFNULL(both_way.total_users,0) total_users
FROM
	(SELECT
		spend_date,
		platform
	FROM
		(SELECT DISTINCT spend_date FROM spending) a,
		(SELECT 'desktop' platform
			UNION
			SELECT 'mobile'
			UNION 
			SELECT 'both') type_platform) table_structure
LEFT JOIN
	(SELECT
	spend_date,
	'both' platform,
	count(1) total_users,
	SUM(amount) total_amount
FROM
	(
	SELECT
			user_id,
			spend_date,
			COUNT(*) cnt,
			SUM(amount) amount
		FROM
			(SELECT
			user_id,
			spend_date,
			platform,
			SUM(amount) amount
		FROM
			spending
		GROUP BY
			user_id, spend_date,platform) every_day_diff_way
		GROUP BY
			user_id, spend_date
		) count_buy_ways
	WHERE cnt=2
	GROUP BY spend_date) both_way
ON both_way.platform=table_structure.platform AND both_way.spend_date=table_structure.spend_date


5.与定义好的表结构left join 这里是不为both的人
SELECT
	spend_date,
	platform,
	COUNT(*) total_users,
	SUM(amount) total_amount
FROM
	(SELECT
		user_id,
		spend_date,
		platform,
		COUNT(*) cnt,
		SUM(amount) amount
	FROM
		(SELECT
		user_id,
		spend_date,
		platform,
		SUM(amount) amount
	FROM
		spending
	GROUP BY
		user_id, spend_date,platform) every_day_diff_way
	GROUP BY
		user_id, spend_date
	) count_buy_ways
WHERE cnt=1
GROUP BY spend_date, platform


6.不为both的人的信息left join 表结构
SELECT
	table_structure.spend_date,
	table_structure.platform,
	IFNULL(not_both_way.total_amount,0) total_amount,
	IFNULL(not_both_way.total_users,0) total_users
FROM
	(SELECT
		spend_date,
		platform
	FROM
		(SELECT DISTINCT spend_date FROM spending) date,
		(SELECT 'desktop' platform
			UNION
			SELECT 'mobile'
			UNION 
			SELECT 'both') type_platform) table_structure
LEFT JOIN
	(SELECT
	spend_date,
	platform,
	COUNT(*) total_users,
	SUM(amount) total_amount
FROM
	(SELECT
		user_id,
		spend_date,
		platform,
		COUNT(*) cnt,
		SUM(amount) amount
	FROM
		(SELECT
		user_id,
		spend_date,
		platform,
		SUM(amount) amount
	FROM
		spending
	GROUP BY
		user_id, spend_date,platform) every_day_diff_way
	GROUP BY
		user_id, spend_date
	) count_buy_ways
WHERE cnt=1
GROUP BY spend_date, platform) not_both_way
ON not_both_way.platform=table_structure.platform AND not_both_way.spend_date=table_structure.spend_date



7.最终结果
SELECT
	a.spend_date,
	a.platform,
	IFNULL((CASE WHEN a.platform='both' THEN b.total_amount ELSE a.total_amount END),0) total_amount,
	IFNULL((CASE WHEN a.platform='both' THEN b.total_users ELSE a.total_users END),0) total_users
FROM
	(SELECT
		table_structure.spend_date,
		table_structure.platform,
		IFNULL(not_both_way.total_amount,0) total_amount,
		IFNULL(not_both_way.total_users,0) total_users
	FROM
		(SELECT
			spend_date,
			platform
		FROM
			(SELECT DISTINCT spend_date FROM spending) date,
			(SELECT 'desktop' platform
				UNION
				SELECT 'mobile'
				UNION 
				SELECT 'both') type_platform) table_structure
	LEFT JOIN
		(SELECT
		spend_date,
		platform,
		COUNT(*) total_users,
		SUM(amount) total_amount
	FROM
		(SELECT
			user_id,
			spend_date,
			platform,
			COUNT(*) cnt,
			SUM(amount) amount
		FROM
			(SELECT
			user_id,
			spend_date,
			platform,
			SUM(amount) amount
		FROM
			spending
		GROUP BY
			user_id, spend_date,platform) every_day_diff_way
		GROUP BY
			user_id, spend_date
		) count_buy_ways
	WHERE cnt=1
	GROUP BY spend_date, platform) not_both_way
	ON not_both_way.platform=table_structure.platform AND not_both_way.spend_date=table_structure.spend_date) a
LEFT JOIN
	(SELECT
	table_structure.spend_date,
	table_structure.platform,
	IFNULL(both_way.total_amount,0) total_amount,
	IFNULL(both_way.total_users,0) total_users
FROM
	(SELECT
		spend_date,
		platform
	FROM
		(SELECT DISTINCT spend_date FROM spending) a,
		(SELECT 'desktop' platform
			UNION
			SELECT 'mobile'
			UNION 
			SELECT 'both') type_platform) table_structure
LEFT JOIN
	(SELECT
	spend_date,
	'both' platform,
	count(1) total_users,
	SUM(amount) total_amount
FROM
	(
	SELECT
			user_id,
			spend_date,
			COUNT(*) cnt,
			SUM(amount) amount
		FROM
			(SELECT
			user_id,
			spend_date,
			platform,
			SUM(amount) amount
		FROM
			spending
		GROUP BY
			user_id, spend_date,platform) every_day_diff_way
		GROUP BY
			user_id, spend_date
		) count_buy_ways
	WHERE cnt=2
	GROUP BY spend_date) both_way
ON both_way.platform=table_structure.platform AND both_way.spend_date=table_structure.spend_date
WHERE both_way.platform='both'
) b
ON a.spend_date = b.spend_date AND a.platform=b.platform
ORDER BY a.spend_date