from menu_component import MenuComponent
from grid_component import GridComponent
from utils import Utils
import time
import sys


class GridWorld:
    grid = None
    menu = None

    def __init__(self):
        self.grid = GridComponent("parameters.json")

        self.menu = MenuComponent(self.grid)

    def start_grid_world(self):
        """
        Starts the grid world main menu selection and processes the user input.

            Parameters:

            Returns:

        """

        while True:

            inp = self.menu.display_main_menu_selection()

            if not self.__process_main_menu_input(inp):
                break

            time.sleep(1)

    def __process_main_menu_input(self, inp):
        """
        Processes input from user. Returns False if the user selects 'Quit'

            Parameters:
                inp: (integer): User input from main menu selection

            Returns:
                is_quitting: (bool): Boolean of whether or not to quit the grid world.

        """

        # Compute omptimal grid world policy
        if inp == "1":

            iterations = self.menu.display_calculate_sub_emnu()

            if Utils.is_positive_int(iterations):
                iterations = int(iterations)
            else:
                print("Iterations must be an integer value.")
                return True

            self.__compute_optimal_mdp(iterations)
            return True

        # Reset grid world
        elif inp == "2":
            self.grid.reset_grid()
            return True

        # Quit
        elif inp == "3":
            print()
            print()
            print("Quitting.")
            print()
            print()
            return False
        else:
            print()
            print()
            print("Invalid selection.")
            print()
            print()
            return True

    def __compute_optimal_mdp(self, iterations):
        """
        Computes optimal Markov Decision Process policy using value iteration. Updates policy and utility graph.

            Parameters:
                iterations: (integer): Number of iterations to run value iteration for

            Returns:

        """

        # UP, RIGHT, DOWN, LEFT
        actions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        for i in range(iterations):
            for row in range(self.grid.parameters.row):
                for col in range(self.grid.parameters.col):

                    state = [row, col]

                    if (
                        not state in self.grid.parameters.walls
                        and not state in self.grid.parameters.end_states
                    ):

                        max_sum = float(-100000000)

                        for action in actions:
                            sum = 0

                            transitions = self.grid.get_transition_model(state, action)

                            for transition in transitions:
                                r = transition[0]
                                c = transition[1]

                                s_prime_utility = self.grid.utility[r][c]

                                if isinstance(s_prime_utility, str):
                                    s_prime_utility = s_prime_utility.strip("[]")

                                sum += transition[2] * float(s_prime_utility)

                            if sum > max_sum:

                                # UP
                                if action == [-1,0]:
                                    self.grid.policy[row][col] = "^"
                                # RIGHT
                                if action == [0,1]:
                                    self.grid.policy[row][col] = ">"
                                # DOWN 
                                if action == [1,0]:
                                    self.grid.policy[row][col] = "v"
                                # LEFT
                                if action == [0,-1]:
                                    self.grid.policy[row][col] = "<"

                                max_sum = sum

                        self.grid.utility[row][col] = round(self.grid.parameters.reward + (
                            self.grid.parameters.lamb * max_sum
                        ),3)

            self.grid.iteration += 1


if __name__ == "__main__":
    world = GridWorld()
    world.start_grid_world()
