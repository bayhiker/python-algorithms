class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # Observation (x, y) -> (x, x+y) or (x+y, y)
        # with x, y > 1. Therefore, to get the only point that we get (tx,ty) from,
        # we only need to subtract the smaller number from the larger of tx ty
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return True
            elif tx > ty:
                tx %= ty
            else:
                ty %= tx
        return False


"""
class Solution:
    def __init__(self) -> None:
        # dp[i][j]: (i, j) is reachable from (sx, sy)
        # dp[i][j] = dp[i-j][j] or dp[j][j-i]
        self.dp: dict[str:bool] = {}

    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        key = f"{tx}-{ty}"
        if key not in self.dp:
            if tx == sx and ty == sy:
                self.dp[key] = True
            elif tx < sx or ty < sy:
                self.dp[key] = False
            else:
                self.dp[key] = self.reachingPoints(
                    sx, sy, tx - ty, ty
                ) or self.reachingPoints(sx, sy, tx, ty - tx)
        return self.dp[key]

"""
