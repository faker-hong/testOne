第一种方案： 
SELECT
	every_hacker_submit.submission_date submission_date,
	every_hacker_submit.cnt every_hacker_submit,
	most_submit.hacker_id hacker_id,
	hackers.`name`
FROM
	(
		SELECT
			group_date_hacker.submission_date,
			group_date_hacker.hacker_id,
			MAX(cnt)
		FROM
			(
				SELECT
					s.submission_date,
					s.hacker_id,
					COUNT(*) cnt
				FROM
					submissions s
				GROUP BY
					s.submission_date,
					s.hacker_id
				ORDER BY
					cnt DESC,
					s.hacker_id
			) group_date_hacker
		GROUP BY
			group_date_hacker.submission_date
	) most_submit
LEFT JOIN hackers 
	ON hackers.hacker_id = most_submit.hacker_id
LEFT JOIN (
	(
		SELECT
			s.submission_date,
			COUNT(*) cnt
		FROM
			submissions s
		GROUP BY
			s.submission_date
		LIMIT 1
	)
	UNION ALL
		SELECT
			group_date_hacker_1.submission_date,
			COUNT(*) cnt
		FROM
			(
				SELECT
					submission_date,
					hacker_id,
					COUNT(*) cnt
				FROM
					submissions
				GROUP BY
					submission_date,
					hacker_id
			) group_date_hacker_1
		JOIN (
			SELECT
				submission_date,
				hacker_id,
				COUNT(*) cnt
			FROM
				submissions
			GROUP BY
				submission_date,
				hacker_id
		) group_date_hacker_2 ON DATEDIFF(
			group_date_hacker_1.submission_date,
			group_date_hacker_2.submission_date
		) = 1
		AND group_date_hacker_1.hacker_id IN (
			group_date_hacker_2.hacker_id
		)
		GROUP BY
			group_date_hacker_1.submission_date
) every_hacker_submit ON every_hacker_submit.submission_date = most_submit.submission_date 




第二种方案： 
SELECT
	most_submit.submission_date,
	every_day_submit.cnt,
	most_submit.hacker_id,
	hackers.`name`
FROM
	(
		SELECT
			count_submit.submission_date,
			count_submit.hacker_id,
			MAX(count_submit.hacker_submit) submit
		FROM
			(
				SELECT
					submission_date,
					hacker_id,
					COUNT(*) hacker_submit
				FROM
					submissions
				GROUP BY
					submission_date,
					hacker_id
				ORDER BY
					hacker_submit DESC,
					hacker_id
			) count_submit
		GROUP BY
			count_submit.submission_date
	) most_submit
LEFT JOIN hackers ON hackers.hacker_id = most_submit.hacker_id
LEFT JOIN (
	SELECT
		count_hackers.submission_date,
		(
			CASE
			WHEN count_hackers.submission_date = every_day_submit.submission_date THEN
				every_day_submit.cnt
			ELSE
				count_hackers.cnt
			END
		) cnt
	FROM
		(
			SELECT
				submission_date,
				COUNT(DISTINCT hacker_id) cnt
			FROM
				submissions
			GROUP BY
				submission_date
		) count_hackers
	LEFT JOIN (
		SELECT
			group_date_hacker_1.submission_date,
			COUNT(*) cnt
		FROM
			(
				SELECT
					submission_date,
					hacker_id,
					COUNT(*) cnt
				FROM
					submissions
				GROUP BY
					submission_date,
					hacker_id
			) group_date_hacker_1
		JOIN (
			SELECT
				submission_date,
				hacker_id,
				COUNT(*) cnt
			FROM
				submissions
			GROUP BY
				submission_date,
				hacker_id
		) group_date_hacker_2 ON DATEDIFF(
			group_date_hacker_1.submission_date,
			group_date_hacker_2.submission_date
		) = 1
		AND group_date_hacker_1.hacker_id IN (
			group_date_hacker_2.hacker_id
		)
		GROUP BY
			group_date_hacker_1.submission_date
	) every_day_submit ON every_day_submit.submission_date = count_hackers.submission_date
) every_day_submit ON every_day_submit.submission_date = most_submit.submission_date