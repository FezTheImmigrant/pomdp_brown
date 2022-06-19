from tabulate import tabulate
from grid_component import GridComponent


class MenuComponent:
    def __init__(self):
        self.Grid = GridComponent("parameters.json")

    def displayMainMenuSelection(self):

        while True:
            print()
            print()
            print("----------MARKOV DECISION PROBLEM ON GRID WORLD----------")
            print()
            print()
            print("-----------CURRENT GRID WORLD----------")
            print()
            print("Parameters:")
            print()
            print("Rows = ", self.Grid.Parameters.Row)
            print("Columns = ", self.Grid.Parameters.Col)
            print("Reward = ", self.Grid.Parameters.Reward)
            print("Lambda = ", self.Grid.Parameters.Lambda)
            print("Walls = ", self.Grid.Parameters.Walls)
            print("End States = ", self.Grid.Parameters.EndStates)
            print()
            print("Grid World Utility:")
            print()
            table = tabulate(self.Grid.Utility, tablefmt="fancy_grid")
            print(table)
            print()
            print("Grid World Policy:")
            print()
            table = tabulate(self.Grid.Policy, tablefmt="fancy_grid")
            print(table)
            print()
            print("Current Iteration: ", self.Grid.Iteration)
            print()
            print("----------MAIN MENU----------")
            print()
            print("Select one of the following options:")
            print()
            print("1. Calculate grid world utility.")
            print("2. Reset grid world utility.")
            print("3. Display grid world policy.")
            print("4. Quit.")
            print()
            print("> ", end="")

            inp = input()

            if not self.processMainMenuInput(inp):
                break

            time.sleep(1)

    def processMainMenuInput(self, inp):
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
    m = MenuComponent()
