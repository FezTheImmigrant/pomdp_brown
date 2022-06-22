from menu_component import MenuComponent
from grid_component import GridComponent
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
                inp: (integer): Integer of user input from main menu selection

            Returns:
                is_quitting: (bool): Boolean of whether or not to quit the grid world.


        """
        """Processes input from user. Returns False if the user selects 'Quit'"""

        if inp == "1":
            return True
        elif inp == "2":
            return True
        elif inp == "3":
            return True
        elif inp == "4":
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


if __name__ == "__main__":
    world = GridWorld()
    world.start_grid_world()
