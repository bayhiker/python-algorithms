class Solution:
    def racecar(self, target: int) -> int:
        # For reach step, we have two options: go forward, or hit R to reset
        # speed to 1 in the opposite direction, and start going the opposite direction in the next step
        # So every turn resets speed to 1 and costs 1 instruction
        #
        # To get the min instruction, we have the following options:
        # Let f(x) = 1+2+4+...+2**x
        # Step 1: go as close to target as possible and pause at step x to make a decision
        #   f(x) < target but f(x+1) > target (if f(x) == target then x is the answer which is trivial)
        # Step 2: Either accelerate past target, and turn and recurse racecar(f(x+1)-target)
        #       or use two R instructions to reset speed to 1, recurse racecar(f(target - f(x)))
        #       Note that turn back costs 1 instruction, while reset speed costs 2 R instructions
        pass
