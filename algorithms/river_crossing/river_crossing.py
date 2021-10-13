# RiverCrossing problem from Ted-ED: https://www.youtube.com/v/ADR7dUoVh_c
#
# Three lions and three wildebeests are running away from a fire,
# but a river is in front of them with only one raft that holds
# at most two animals and needs at least one animal to operate the
# raft back and forth. At no time can more lions be left alone with
# less wildebeests, otherwise the lions will eat the wildebeests.
# Note that this also includes to animals being offloaded from boats.
#
# Figure out a way for all animals to safely cross the river only
# with this single raft.

from enum import Enum
from typing import Dict, List
from queue import SimpleQueue


class BoatAt(Enum):
    UNKNOWN = 0
    LEFT = 1
    RIVER = 2
    RIGHT = 3


class ValidState:
    def __init__(
        self,
        lion_left=0,
        lion_boat=0,
        lion_right=0,
        wilde_left=0,
        wilde_boat=0,
        wilde_right=0,
        boat_at=BoatAt.RIVER,
    ) -> None:
        self.lion_left = lion_left
        self.lion_boat = lion_boat
        self.lion_right = lion_right
        self.wilde_left = wilde_left
        self.wilde_boat = wilde_boat
        self.wilde_right = wilde_right
        self.boat_at = boat_at
        self.next_states = []

    def pretty_print(self, compressed=False, print_next=False):
        def print_num_letter(num, letter):
            if compressed:
                return f"{num}{letter}" if num > 0 else " "
            else:
                return (
                    f"{num}{letter}" if num > 1 else f" {letter}" if num == 1 else "  "
                )

        ll = print_num_letter(self.lion_left, "L")
        lb = print_num_letter(self.lion_boat, "L")
        lr = print_num_letter(self.lion_right, "L")
        l_boat_at = "B" if self.boat_at == BoatAt.LEFT else " "
        wl = print_num_letter(self.wilde_left, "W")
        wb = print_num_letter(self.wilde_boat, "W")
        wr = print_num_letter(self.wilde_right, "W")
        r_boat_at = "B" if self.boat_at == BoatAt.RIGHT else " "
        next_states_info = ""
        if print_next:
            next_states_info = " ("
            for next_state in self.next_states:
                next_states_info += next_state.pretty_print(compressed=True) + ","
            next_states_info += ")"
        return f"{ll}{wl}{l_boat_at}|{lb}{wb}|{lr}{wr}{r_boat_at}{next_states_info}"


class RiverCrossing:
    def __init__(self, num_lions, num_wildebeests, init_states_later=False) -> None:
        if num_lions > num_wildebeests:
            raise ValueError(
                f"Invalid initial state, {num_lions} lions will eat all {num_wildebeests} wildebeests"
            )
        self.num_lions = num_lions
        self.num_wildebeests = num_wildebeests
        self.start_state = None
        self.end_state = None
        self.valid_states = []
        if not init_states_later:
            self.__init_valid_states()

    def traverse_bfs(self):
        paths: List[List[ValidState]] = {}
        q: SimpleQueue[ValidState] = SimpleQueue()
        q.put(self.start_state)
        paths[self.start_state] = [self.start_state]
        while not q.empty():
            state = q.get()
            for next_state in state.next_states:
                if next_state in paths:
                    continue  # Already know how to get to this state from start_state
                q.put(next_state)
                path_to_next_state = paths[state].copy()
                path_to_next_state.append(next_state)
                paths[next_state] = path_to_next_state
                if next_state is self.end_state:
                    return path_to_next_state
        return None

    def traverse_dfs(self):
        paths: List[List[ValidState]] = {}
        s: List[ValidState] = []
        s.append(self.start_state)
        paths[self.start_state] = [self.start_state]
        while not len(s) == 0:
            state = s.pop()
            for next_state in state.next_states:
                if next_state in paths:
                    continue  # Already know how to get to this state from start_state
                s.append(next_state)
                path_to_next_state = paths[state].copy()
                path_to_next_state.append(next_state)
                paths[next_state] = path_to_next_state
                if next_state is self.end_state:
                    return path_to_next_state
        return None

    def __edge_exists(self, state1: ValidState, state2: ValidState):
        if not state1 or not state2:
            return False
        # Get onto the boat from left bank(state1->state2)
        if (
            state1.boat_at == BoatAt.LEFT
            and state2.boat_at == BoatAt.RIVER
            and state1.lion_left == state2.lion_left + state2.lion_boat
            and state1.wilde_left == state2.wilde_left + state2.wilde_boat
            and state1.lion_right == state2.lion_right
            and state1.wilde_right == state2.wilde_right
        ):
            return True
        # Get off the boat to the left bank(state1->state2)
        if (
            state1.boat_at == BoatAt.RIVER
            and state2.boat_at == BoatAt.LEFT
            and state1.lion_boat + state1.lion_left == state2.lion_left
            and state1.wilde_boat + state1.wilde_left == state2.wilde_left
            and state1.lion_right == state2.lion_right
            and state1.wilde_right == state2.wilde_right
        ):
            return True
        # Get onto the boat from right bank(state1->state2)
        if (
            state1.boat_at == BoatAt.RIGHT
            and state2.boat_at == BoatAt.RIVER
            and state1.lion_right == state2.lion_right + state2.lion_boat
            and state1.wilde_right == state2.wilde_right + state2.wilde_boat
            and state1.lion_left == state2.lion_left
            and state1.wilde_left == state2.wilde_left
        ):
            return True
        # Get off the boat to the right bank(state1->state2)
        if (
            state1.boat_at == BoatAt.RIVER
            and state2.boat_at == BoatAt.RIGHT
            and state1.lion_boat + state1.lion_right == state2.lion_right
            and state1.wilde_boat + state1.wilde_right == state2.wilde_right
            and state1.lion_left == state2.lion_left
            and state1.wilde_left == state2.wilde_left
        ):
            return True

        return False

    def __init_valid_states(self):
        valid_states: List[ValidState] = []

        def get_layouts(num):
            layouts = []
            for i in range(0, num + 1):
                for j in range(0, num + 1):
                    if i + j <= num:
                        layouts.append([i, j, num - i - j])
            return layouts

        lion_layouts = get_layouts(self.num_lions)
        wilde_layouts = get_layouts(self.num_wildebeests)
        for lion_layout in lion_layouts:
            (lion_left, lion_boat, lion_right) = lion_layout
            for wilde_layout in wilde_layouts:
                (wilde_left, wilde_boat, wilde_right) = wilde_layout
                if (
                    (lion_left > wilde_left and wilde_left != 0)
                    or (lion_right > wilde_right and wilde_right != 0)
                    or lion_boat + wilde_boat > 2
                    or (
                        (lion_boat + lion_left) > (wilde_boat + wilde_left)
                        and wilde_boat + wilde_left != 0
                        and (lion_boat + lion_right) > (wilde_boat + wilde_right)
                        and wilde_boat + wilde_right != 0
                    )
                ):
                    continue
                state_params = {
                    "lion_left": lion_left,
                    "lion_boat": lion_boat,
                    "lion_right": lion_right,
                    "wilde_left": wilde_left,
                    "wilde_boat": wilde_boat,
                    "wilde_right": wilde_right,
                }
                if lion_boat == 0 and wilde_boat == 0:
                    if not (lion_right == 3 and wilde_right == 3):
                        valid_state = ValidState(**state_params, boat_at=BoatAt.LEFT)
                        valid_states.append(valid_state)
                    if not (lion_left == 3 and wilde_left == 3):
                        valid_state = ValidState(**state_params, boat_at=BoatAt.RIGHT)
                        valid_states.append(valid_state)
                else:
                    valid_state = ValidState(**state_params, boat_at=BoatAt.RIVER)
                    valid_states.append(valid_state)
        for valid_state in valid_states:
            if (
                valid_state.lion_left == self.num_lions
                and valid_state.wilde_left == self.num_wildebeests
                and valid_state.boat_at == BoatAt.LEFT
            ):
                self.start_state = valid_state
            if (
                valid_state.lion_right == self.num_lions
                and valid_state.wilde_right == self.num_wildebeests
                and valid_state.boat_at == BoatAt.RIGHT
            ):
                self.end_state = valid_state
            valid_state.next_states = []
            for next_candidate in valid_states:
                if valid_state is next_candidate:
                    continue
                if self.__edge_exists(valid_state, next_candidate):
                    valid_state.next_states.append(next_candidate)

        self.valid_states = valid_states
