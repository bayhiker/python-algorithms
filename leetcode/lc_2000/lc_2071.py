class Solution:
    def maxTaskAssign(
        self, tasks: list[int], workers: list[int], pills: int, strength: int
    ) -> int:
        """Binary search the max number of tasks.

        Sort tasks and worker in ascending order
        Check k number of tasks doable?
        First look at task[k-1], this can be done either by worker[n-1], if worker[n-1] not strong enough, find the next weakest worker that can handle this task after taking one pill. Repeat this process.

        Args:
            tasks (list[int]): _description_
            workers (list[int]): _description_
            pills (int): _description_
            strength (int): _description_

        Returns:
            int: _description_
        """
        pass
