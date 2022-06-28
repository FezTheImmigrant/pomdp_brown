import numpy as np
import sys
import time
from parameters_component import ParametersComponent

np.set_printoptions(precision=4)
np.set_printoptions(threshold=sys.maxsize)  # display entire array


class GridComponent:
    iteration = 0

    def __init__(self, file_name):
        self.parameters = ParametersComponent()

        if not self.parameters.load_parameters(file_name):
            exit(-1)

        if not self.__initialize_grid():
            exit(-1)

    def reset_grid(self):
        """
        Reset utility and policy grid to their initial states.

            Parameters:

            Returns:

        """
        self.__initialize_grid()

    def __initialize_grid(self):
        """
        Create a utility and policy grid. Returns True if walls and end_states are valid parameters.

            Parameters:

            Returns:
                is_valid: (bool): Boolean of whether or not parameters are valid.
        """
        self.iteration = 0

        self.utility = [
            [0 for c in range(self.parameters.col)] for r in range(self.parameters.row)
        ]
        self.policy = [
            ["<" for c in range(self.parameters.col)]
            for r in range(self.parameters.row)
        ]

        return self.__initialize_walls() and self.__initialize_end_states()

    def get_transition_model(self, state, action):
        """
        Returns transition model for a given state and action.

            Parameters:
                state: (list): row and column of state.
                action: (list): delta row and delta column for movement on grid.

            Returns:
                is_valid: (bool): Boolean of whether or not parameters are valid.
        """

        row = state[0]
        col = state[1]

        # there is no transition model for walls or end states
        if (
            not [row, col] in self.parameters.walls
            and not [row, col] in self.parameters.end_states
        ):

            up_prob = 0
            right_prob = 0
            down_prob = 0
            left_prob = 0

            # UP
            if action == [-1, 0]:
                up_prob = self.parameters.cw_0
                right_prob = self.parameters.cw_90
                down_prob = self.parameters.cw_180
                left_prob = self.parameters.cw_270

            # RIGHT
            elif action == [0, 1]:
                up_prob = self.parameters.cw_270
                right_prob = self.parameters.cw_0
                down_prob = self.parameters.cw_90
                left_prob = self.parameters.cw_180

            # DOWN
            elif action == [1, 0]:
                up_prob = self.parameters.cw_180
                right_prob = self.parameters.cw_270
                down_prob = self.parameters.cw_0
                left_prob = self.parameters.cw_90

            # LEFT
            elif action == [0, -1]:
                up_prob = self.parameters.cw_90
                right_prob = self.parameters.cw_180
                down_prob = self.parameters.cw_270
                left_prob = self.parameters.cw_0

            # don't allow movement into a wall or grid edge.
            up_r = max(row - 1, 0)
            up_c = col

            if [up_r, up_c] in self.parameters.walls:
                up_r = row
                up_c = col

            # don't allow movement into a wall or grid edge.
            right_r = row
            right_c = min(col + 1, self.parameters.col - 1)

            if [right_r, right_c] in self.parameters.walls:
                right_r = row
                right_c = col

            # don't allow movement into a wall or grid edge.
            down_r = min(row + 1, self.parameters.row - 1)
            down_c = col

            if [down_r, down_c] in self.parameters.walls:
                down_r = row
                down_c = col

            # don't allow movement into a wall or grid edge.
            left_r = row
            left_c = max(col - 1, 0)

            if [left_r, left_c] in self.parameters.walls:
                left_r = row
                left_c = col

            transition_model = [
                [up_r, up_c, up_prob],
                [right_r, right_c, right_prob],
                [down_r, down_c, down_prob],
                [left_r, left_c, left_prob],
            ]

            return transition_model

    def __initialize_walls(self):
        """
        Initializes walls on utility and policy grid.
        Returns True if walls are in range of the grid world  row and column parameters.

            Parameters:

            Returns:
                is_valid: (bool): Boolean of whether or not walls are within the grid world parameters
        """

        for wall in self.parameters.walls:
            if wall[0] < self.parameters.row and wall[1] < self.parameters.col:
                self.utility[wall[0]][wall[1]] = "X"
                self.policy[wall[0]][wall[1]] = "X"
            else:
                print("Given wall is out of range of grid world", wall)
                return False

        return True

    def __initialize_end_states(self):
        """
        Initializes end states on utility and policy grid.
        Returns True if end_states are in range of the grid world row and column parameters, and if there is not already a wall placed.

            Parameters:

            Returns:
                is_valid: (bool): Boolean of whether or not end states are within the grid world parameters
        """

        i = 0
        for end_state in self.parameters.end_states:
            if (
                end_state[0] < self.parameters.row
                and end_state[1] < self.parameters.col
            ):
                if self.utility[end_state[0]][end_state[1]] == "X":
                    print(
                        "Given end state cannot be placed where wall currently is.",
                        end_state,
                    )
                    return False

                self.utility[end_state[0]][end_state[1]] = (
                    "[" + str(self.parameters.end_state_rewards[i]) + "]"
                )

                self.policy[end_state[0]][end_state[1]] = "E"

                i += 1
            else:
                print("Given end state is out of range of grid world", end_state)
                return False

        return True
