# [leetcode 15: 3 sum](https://youquiz.me/jobs/problem/3sum/)

How to remove duplicates?

- i loops through 0 - n-1
- p1 moves from i+1 towards p2
- p2 moves from n-1 towards p1
- **After** each i loop, each p1 and p2 move, skip all numbers that are the same as the current num to avoid duplicates. This should not be done at the beginning of these loops, otherwise you may miss some combos. For example, if nums=[-4, 1, 2, 2, 2, 4], when i is 0 (nums[i] == -4) and p1=2 (nums[p1] == 2), if p1 skips duplicate nums[3] and nums[4], you'll miss combo [-4, 2, 2].

# [leetcode 1150]: Two Sum BSTs

This is similar to regular two sum with sorted nums after in-order traversing through the BSTs. Let p1 point to start of nums1 and p2 point to end of nums2. Move p1 right if sum is smaller than target, or p2 to the left if sum is larger then target, until p1 is at len(nums1) or p2 at 0.

# [leetcode 1872: Stone Game viii](https://leetcode.com/problems/stone-game-viii/)

Understanding the state transition formula is key to solving this problem.

- dp[i]: Max score difference when current player is at stones[i], and have the option to pick [i], [i, i+1], ..., [i,i+1,...,n-1]
- dp[n-1]: 0 as border condition
- dp[n-1] = prefix_sum(n-1) There are only two stones: stones[n-1] and the one that was added on the left, x>1, so take both.
- dp[i] = max(prefix_sum(j) - dp[j+1]) for all i <= j < n - 1 where prefix_sum(j) - dp[j+1] is the case where player takes stones i through j

```
   dp[i] = max(prefix_sum(i) - dp[i+1],
               prefix_sum(i+1) - dp[i+2],
               prefix_sum(i+2) - dp[i+3],
               ...
               prefix_sum(n-1) - dp[n],
           )
   dp[i+1] = max(prefix_sum(i+1) - dp[i+2],
               prefix_sum(i+2) - dp[i+3],
               ...
               prefix_sum(n-1) - dp[n],
           )
```

Observation: dp[i+1] is exactly the portion of dp[i] after prefix_sum[i] - dp[i+1]
dp[i] = max(prefix_sum[i], dp[i+1])
This leads to the following simpler state transition, which gives us O(n) time instead of O(n\*\*2):

    dp[n-1] = prefix_sum[n-1]
    dp[i] = max(dp[i+1], prefix_sum[i] - dp[i+1]) for 1 <= i <= n-2
    return dp[1]

Refer to [this article](https://juejin.cn/post/6967904225363755015) for some more details.
These articles also have some additional information:[here](https://leetcode.com/problems/stone-game-viii/discuss/1224639/Python-prefix-sum) by zdu011, and [here](https://leetcode-cn.com/problems/stone-game-viii/solution/python-dong-tai-gui-hua-by-qubenhao-j287/) as explained by Benhao.

# [Leetcode 2029: Stone Game ix](https://leetcode.com/problems/stone-game-ix/)

Solve this problem by counting remainders when divided by 3: n0 for number of stones with remainder 0, n1 for number of stones with remainder 1, and n2 for number of stones with remainder 2

- if n1 == 0 and n2 == 0, then Alice loses the second she picks up a stone
- if n1 == 0 and n2 > 0, then Alice wins only if n2 > 2 and n0 is odd
- if n1 > 0 and n2 == 0, then Alice wins only if n1 > 2 and n0 is odd
- if n1 > 0 and n2 > 0, then not considering n0 items, game only goes on if 112121212... or 221212121... Alice wins if n0 is even and n2 - n1 > 2
