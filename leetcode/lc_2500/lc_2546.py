class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        return self.make_strings_equal(s, target)

    def make_strings_equal(self, s: str, target: str) -> bool:
        """
        s_i, x_j ---> new_s_i, new_s_j
         0    0          0        0 (No use, bits don't change)
         0    1          1        1
         1    0          1        1
         1    1          1        0

        Observation 1: all 0 strings can only convert to all 0 string,
                        no "1"s can be produced from all 0 strings
        Observation 2: all 0 targets can only be produced from an s with any 1s
                       because 1s cannot be eliminated with 01->11, 10->11, 11->10.
                       Number of 1s can be reduced but not eliminated

        Args:
            s (str): _description_
            target (str): _description_

        Returns:
            bool: _description_
        """
        s_has_1 = "1" in s
        t_has_1 = "1" in target
        return (s_has_1 and t_has_1) or (not s_has_1 and not t_has_1)
