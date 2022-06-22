from menu_component import MenuComponent
from grid_component import GridComponent
from utils import Utils
import time


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
            self.__compute_optimal_mdp(iterations)
            return True

        # Reset grid world
        elif inp == "2":
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

    def __compute_optimal_mdp(self,iterations):
        """
        Computes optimal Markov Decision Process policy using value iteration. Updates policy and utility graph.

            Parameters:
                iterations: (integer): Number of iterations to run value iteration for

            Returns:

        """

        if Utils.is_positive_int(iterations):
            self.grid.iteration += int(iterations)


if __name__ == "__main__":
    world = GridWorld()
    world.start_grid_world()
