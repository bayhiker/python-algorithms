# SQL https://circlecoder.com/suspicious-bank-accounts/
"""
select distinct(account_id) 
from
	(select t.account_id, sum(amount)-a.max_income as diff_income, 
		extract(month from day) as day, 
		extract(month from lead(day) 
			over(partition by t.account_id order by day)) as next_day
	from Transactions t
	join Accounts a on t.account_id=a.account_id
	where type='Creditor'
	group by t.account_id, left(day,7)
	having diff_income>0
	order by transaction_id) t1
where day+1=next_day
"""
