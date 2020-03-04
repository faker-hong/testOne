-- 求出最大事务次数
SELECT
	count(*) cnt
FROM
	transactions t
GROUP BY
	t.user_id,
	t.transaction_date
ORDER BY
	cnt DESC
LIMIT 1 




-- 求出0到最大值的事务次数
SELECT DISTINCT

IF (
	@transaction_count < (
		SELECT
			count(*) cnt
		FROM
			transactions t
		GROUP BY
			t.user_id,
			t.transaction_date
		ORDER BY
			cnt DESC
		LIMIT 1
	),
	@transaction_count :=@transaction_count + 1,
	@transaction_count :=@transaction_count
) transactions_count
FROM
	transactions t,
	(
		SELECT
			@transaction_count :=- 1
	) tran_count




-- 计算不同事务次数的访问次数
SELECT
	h.transactions_count,
	COUNT(h.transaction_times) visit_count
FROM
	(
		SELECT
			IFNULL(a.cnt, 0) transactions_count,
			IFNULL(a.cnt, 0) transaction_times
		FROM
			visits v
		LEFT JOIN (
			SELECT
				t.user_id,
				t.transaction_date,
				count(*) cnt
			FROM
				transactions t
			GROUP BY
				t.user_id,
				t.transaction_date
		) a ON v.user_id = a.user_id
		AND v.visit_date = a.transaction_date
	) h
GROUP BY
	transactions_count




-- 最终结果
SELECT
	b.transactions_count,
	IFNULL(a.visit_count, 0) visit_count
FROM
	(
		SELECT
			h.transactions_count,
			COUNT(h.transaction_times) visit_count
		FROM
			(
				SELECT
					IFNULL(a.cnt, 0) transactions_count,
					IFNULL(a.cnt, 0) transaction_times
				FROM
					visits v
				LEFT JOIN (
					SELECT
						t.user_id,
						t.transaction_date,
						count(*) cnt
					FROM
						transactions t
					GROUP BY
						t.user_id,
						t.transaction_date
				) a ON v.user_id = a.user_id
				AND v.visit_date = a.transaction_date
			) h
		GROUP BY
			transactions_count
	) a
RIGHT JOIN (
	SELECT DISTINCT

	IF (
		@transaction_count < (
			SELECT
				count(*) cnt
			FROM
				transactions t
			GROUP BY
				t.user_id,
				t.transaction_date
			ORDER BY
				cnt DESC
			LIMIT 1
		),
		@transaction_count :=@transaction_count + 1,
		@transaction_count :=@transaction_count
	) transactions_count
	FROM
		transactions t,
		(
			SELECT
				@transaction_count :=- 1
		) tran_count
) b ON a.transactions_count = b.transactions_count