1.将日期和购物方式笛卡尔积，获得所需的表结构, diff_date_type
SELECT
	DISTINCT spend_date
FROM
	spending,
	(SELECT 'desktop' platform
		UNION
		SELECT 'mobile'
		UNION
		SELECT 'both') platform_type


2.根据id和日期分组，有两条数据的both，处理数据
SELECT
	user_id, 
	spend_date,
	(CASE COUNT(DISTINCT platform) WHEN 1 THEN platform WHEN 2 THEN 'both' END) platform,
	SUM(amount) amount
FROM
	spending
GROUP BY
	user_id, spend_date


3.获得total_user和total_mount
SELECT
	spend_date, 
	platform,
	SUM(amount) total_amount,
	COUNT(*) total_user
FROM
	(SELECT
	user_id, 
	spend_date,
	(CASE COUNT(DISTINCT platform) WHEN 1 THEN platform WHEN 2 THEN 'both' END) platform,
	SUM(amount) amount
FROM
	spending
GROUP BY
	user_id, spend_date
	) three_platform
GROUP BY
	spend_date, platform




3.最终结果
SELECT
	table_structure.spend_date,
	table_structure.platform,
	IFNULL(total.total_amount, 0) total_amount,
	IFNULL(total.total_users, 0) total_users
FROM
	(
		SELECT DISTINCT
			(spend_date),
			platform_type.platform
		FROM
			spending,
			(
				SELECT
					'desktop' platform
				UNION
					SELECT
						'mobile' platform
					UNION
						SELECT
							'both' platform
			) platform_type
	) table_structure
LEFT JOIN (
	SELECT
		spend_date,
		platform,
		SUM(amount) total_amount,
		COUNT(user_id) total_users
	FROM
		(
			SELECT
				user_id,
				spend_date,
				(
					CASE COUNT(DISTINCT platform)
					WHEN 1 THEN
						platform
					WHEN 2 THEN
						'both'
					END
				) platform,
				SUM(amount) amount
			FROM
				spending
			GROUP BY
				user_id,
				spend_date
		) three_platform
	GROUP BY
		spend_date,	
		platform
) total ON table_structure.spend_date = total.spend_date
AND table_structure.platform = total.platform





