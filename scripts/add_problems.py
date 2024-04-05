import os
import re
import sys
from pathlib import Path

problem_ids = "159 234 2233 952 2672 2899 1247 2158 793 1689 2462 2650 187 2911 234 51"


def add_problems() -> int:
    problems = re.split("\s*,\s*|\s+" if "," in problem_ids else "\s+", problem_ids)
    for problem in problems:
        problem_number = int(problem)
        folder = f"{get_lc_folder()}/lc_{str(problem_number // 100 * 100).zfill(4)}"
        if not os.path.exists(folder):
            os.mkdir(folder)
        problem_file = f"{folder}/lc_{problem.zfill(4)}.py"
        Path(problem_file).touch()
        print(f"Touched file {problem_file}")


def get_lc_folder() -> str:
    cwd = os.getcwd()
    parts = cwd.split("/")
    while len(parts) > 0 and parts[-1] != "python-algorithms":
        parts.pop()
    if len(parts) == 0:
        raise FileNotFoundError(
            "python-algorithms/leetcode directory not found, "
            + "make sure script is run inside python-algorithms project folder"
        )
    repo_folder = "/".join(parts)
    lc_folder = f"{repo_folder}/leetcode"
    if not os.path.isdir(lc_folder):
        raise FileNotFoundError(
            "python-algorithms directory found, but leetcode not found, "
            + " make sure python-algorithms/leetcode exists and is a folder"
        )
    return lc_folder


if __name__ == "__main__":
    sys.exit(add_problems())
