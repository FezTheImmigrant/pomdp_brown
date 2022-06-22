from tabulate import tabulate
from grid_component import GridComponent
import time


class MenuComponent:
    def __init__(self, grid):
        self.grid = grid

    def display_main_menu_selection(self):
        """
        Displays main menu for grid world. Returns user input from main menu selection.

            Parameters:

            Returns:
                inp: (Integer): Integer of user input from main menu selection
        """
        print()
        print()
        print("----------MARKOV DECISION PROBLEM ON GRID WORLD----------")
        print()
        print()
        print("-----------CURRENT GRID WORLD----------")
        print()
        print("Parameters:")
        print()
        print("Rows = ", self.grid.parameters.row)
        print("Columns = ", self.grid.parameters.col)
        print("Reward = ", self.grid.parameters.reward)
        print("Lambda = ", self.grid.parameters.lamb)
        print("cw_0 probability = ", self.grid.parameters.cw_0)
        print("cw_90 probability = ", self.grid.parameters.cw_90)
        print("cw_180 probability = ", self.grid.parameters.cw_180)
        print("cw_270 probability = ", self.grid.parameters.cw_270)
        print("Walls = ", self.grid.parameters.walls)
        print("End States = ", self.grid.parameters.end_states)
        print()
        print("Grid World Utility:")
        print()
        table = tabulate(self.grid.utility, tablefmt="fancy_grid")
        print(table)
        print()
        print("Grid World Policy:")
        print()
        table = tabulate(self.grid.policy, tablefmt="fancy_grid")
        print(table)
        print()
        print("Current Iteration: ", self.grid.iteration)
        print()
        print("----------MAIN MENU----------")
        print()
        print("Select one of the following options:")
        print()
        print("1. Compute Optimal MDP policy.")
        print("2. Reset grid world.")
        print("3. Quit.")
        print()
        print("> ", end="")

        inp = input()

        return inp

    def display_calculate_sub_emnu(self):
        print()
        print()
        print("For how many iterations?")
        print()
        print("> ", end="")

        inp = input()

        return inp
