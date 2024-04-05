"""
# SQL from https://leetcode.ca/2021-07-25-1892-Page-Recommendations-II/
select f.user1_id as user_id, l.page_id, count(*) as friends_likes
    from (
        select user1_id, user2_id from Friendship union select user2_id, user1_id from Friendship
    ) as f
    inner join Likes l
    on f.user2_id = l.user_id 
    where not exists (
        select * from Likes where user_id = f.user1_id and page_id = l.page_id
    )
    group by f.user1_id, l.page_id;
"""
