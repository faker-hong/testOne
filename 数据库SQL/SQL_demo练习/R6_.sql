SELECT
	period_state,
	MIN(date) start_date,
	MAX(date) end_date
FROM
	(
		SELECT
			date,

		IF (
			period_state =@state,
			@rank :=@rank,
			@rank :=@rank + 1
		) rank,
		@state := period_state period_state
	FROM
		(
			SELECT
				'failed' period_state,
				fail_date date
			FROM
				failed
			WHERE
				fail_date BETWEEN '2019-01-01'
			AND '2019-12-31'
			UNION ALL
				SELECT
					'succeeded' period_state,
					success_date date
				FROM
					succeeded
				WHERE
					success_date BETWEEN '2019-01-01'
				AND '2019-12-31'
				ORDER BY
					date
		) order_date,
		(SELECT @state := '', @rank := 0) state
	) group_date
GROUP BY
	rank