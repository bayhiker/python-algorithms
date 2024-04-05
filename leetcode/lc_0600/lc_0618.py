# 618 - Students Report By Geography
"""
select America, Asia, Europe from
    (
        select @asia := 0, @america := 0, @europe := 0
    ) t,
    (
        select @asia := @asia + 1 as Asia_Id, name as Asia from student
            where continent = 'Asia' order by Asia
    ) t1
        right join
    (
        select @america := @america + 1 as America_Id, name as America from student
            where continent = 'America' order by America
    ) t2 on Asia_Id = America_Id
        left join
    (
        select @europe := @europe + 1 as Europe_Id, name as Europe from student
            where continent = 'Europe' order by Europe
    ) t3 on America_Id = Europe_Id
;
"""
