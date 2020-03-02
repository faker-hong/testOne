-- 求出最大事务次数
SELECT MAX(cnt)
			from visits v 
			LEFT JOIN (SELECT t.user_id, t.transaction_date, count(*) cnt
															from transactions t
															GROUP BY t.user_id, t.transaction_date) a
			ON v.user_id = a.user_id and v.visit_date = a.transaction_date

-- 求出0到最大值的事务次数
SELECT DISTINCT IF(@transaction_count<(SELECT MAX(cnt)
			from visits v 
			LEFT JOIN (SELECT t.user_id, t.transaction_date, count(*) cnt
															from transactions t
															GROUP BY t.user_id, t.transaction_date) a
			ON v.user_id = a.user_id and v.visit_date = a.transaction_date), @transaction_count:=@transaction_count+1, @transaction_count:=@transaction_count) transactions_count
from 
(SELECT IFNULL(a.cnt,0) transactions_times
			from visits v 
			LEFT JOIN (SELECT t.user_id, t.transaction_date, count(*) cnt
															from transactions t
															GROUP BY t.user_id, t.transaction_date) a
			ON v.user_id = a.user_id and v.visit_date = a.transaction_date
order by transactions_times) tran_times, (SELECT @transaction_count:=-1) tran_count


-- 计算不同事务次数的访问次数
SELECT h.transactions_count, COUNT(h.transaction_times) visit_count
from (SELECT IFNULL(a.cnt,0) transactions_count, IFNULL(a.cnt,0) transaction_times
			from visits v 
			LEFT JOIN (SELECT t.user_id, t.transaction_date, count(*) cnt
															from transactions t
															GROUP BY t.user_id, t.transaction_date) a
			ON v.user_id = a.user_id and v.visit_date = a.transaction_date) h
GROUP BY transactions_count


-- 求得最终结果
SELECT b.transactions_count, IFNULL(a.visit_count,0) visit_count
from (SELECT h.transactions_count, COUNT(h.transaction_times) visit_count
from (SELECT IFNULL(a.cnt,0) transactions_count, IFNULL(a.cnt,0) transaction_times
			from visits v 
			LEFT JOIN (SELECT t.user_id, t.transaction_date, count(*) cnt
															from transactions t
															GROUP BY t.user_id, t.transaction_date) a
			ON v.user_id = a.user_id and v.visit_date = a.transaction_date) h
GROUP BY transactions_count) a RIGHT JOIN (SELECT DISTINCT IF(@transaction_count<(SELECT MAX(cnt)
			from visits v 
			LEFT JOIN (SELECT t.user_id, t.transaction_date, count(*) cnt
															from transactions t
															GROUP BY t.user_id, t.transaction_date) a
			ON v.user_id = a.user_id and v.visit_date = a.transaction_date), @transaction_count:=@transaction_count+1, @transaction_count:=@transaction_count) transactions_count
from 
(SELECT IFNULL(a.cnt,0) transactions_times
			from visits v 
			LEFT JOIN (SELECT t.user_id, t.transaction_date, count(*) cnt
															from transactions t
															GROUP BY t.user_id, t.transaction_date) a
			ON v.user_id = a.user_id and v.visit_date = a.transaction_date
order by transactions_times) tran_times, (SELECT @transaction_count:=-1) tran_count) b
ON a.transactions_count = b.transactions_count
