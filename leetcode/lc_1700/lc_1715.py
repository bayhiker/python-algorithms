# SQL
""" 
select sum(ifnull(box.apple_count, 0) + ifnull(chest.apple_count, 0)) as apple_count,
    sum(ifnull(box.orange_count, 0) + ifnull(chest.orange_count, 0)) as orange_count
    from Boxes as box
    left join Chests as chest
    on box.chest_id = chest.chest_id;
"""
