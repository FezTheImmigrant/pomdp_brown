import numpy as np
import sys
import time
import json
from tabulate import tabulate

np.set_printoptions(precision=4)
np.set_printoptions(threshold=sys.maxsize) # display entire array
np.linspace(1,10)

class GridWorld:
    Iteration = 0
    Walls = []
    WinState = []
    def __init__(self):

        if not self.load_parameters("parameters.json"):
            exit(-1)

        if not self.initializeGridWorld():
            exit(-1)

        self.displayMainMenuSelection()

    def load_parameters(self,file_name):

        f= open (file_name,"r")

        data = json.loads(f.read())

        if self.is_positive_int(data['Rows']):
            self.Row = int(data['Rows'])
        else:
            print("Row parameter must be a postive integer value.")
            return False

        if self.is_positive_int(data['Columns']):
            self.Col = int(data['Columns'])
        else:
            print("Column parameter must be a positive integer value.")
            return False

        if self.is_float(data['Reward']):
            self.Reward = float(data['Reward'])
        else:
            print("Reward parameter must be a float value.")
            return False

        if self.is_float(data['Lambda']):
            self.Lambda = float(data['Lambda'])
        else:
            print("Lambda parameter must be a float value.")
            return False


        for wall in data["Walls"]:

            if not len(wall) == 2:
                print ("A wall takes only two parameters: (row,column)")
                return False

            if not self.is_positive_int(wall[0]) or not self.is_positive_int(wall[1]):
                print ("A wall takes only positive integer parameters")
                return False

            self.Walls.append(wall)

        if not len(data["WinState"]) == 2:
            print ("The win state takes only two parameters: (row,column)")
            return False

        if not self.is_positive_int(data["WinState"][0]) or not self.is_positive_int(data["WinState"][1]):
            print ("The win state takes only positive integer parameters")
            return False
        
        self.WinState = data["WinState"]

        if self.is_float(data["WinStateReward"]):
            self.WinStateReward = data["WinStateReward"]
        else:
            print("Win state reward parameter must be a float value.")
            return False
        
        return True


    def initializeGridWorld(self):
        self.Utility = [[ 0 for c in range(self.Col) ] for r in range(self.Row)]
        self.Policy = [[ "<" for c in range(self.Col) ] for r in range(self.Row)]

        for wall in self.Walls:
            if wall[0] < self.Row and wall[1] < self.Col:
                self.Utility[wall[0]][wall[1]] = "X"
                self.Policy[wall[0]][wall[1]] = "X"
            else:
                print ("Given wall is out of range of grid world", wall)
                return False

        if self.WinState[0] < self.Row and self.WinState[1] < self.Col:
           self.Utility[self.WinState[0]][self.WinState[1]] = "[" + str(self.WinStateReward) + "]"
           self.Policy[self.WinState[0]][self.WinState[1]] = "E"
        else:
           print ("Given wall is out of range of grid world", wall)
           return False
        
        return True



    def displayMainMenuSelection(self):

        while True:
            print()
            print()
            print ("----------MARKOV DECISION PROBLEM ON GRID WORLD----------")
            print()
            print()
            print("-----------CURRENT GRID WORLD----------")
            print()
            print("Parameters:")
            print()
            print("Rows = ",self.Row)
            print("Columns = ",self.Col)
            print("Reward = ",self.Reward)
            print("Lambda = ",self.Lambda)
            print("Walls = ",self.Walls)
            print("Win State = ",self.WinState)
            print()
            print("Grid World Utility:")
            print()

            table = tabulate(self.Utility,tablefmt="fancy_grid")
            print(table)
            print()
            print("Current Iteration: ", self.Iteration)
            print()
            print ("----------MAIN MENU----------")
            print()
            print ("Select one of the following options:")
            print()
            print ("2. Calculate grid world utility.")
            print ("3. Reset grid world utility.")
            print ("4. Display grid world policy.")
            print ("5. Quit.")
            print()
            print("> ",end="")

            inp = input()

            if not self.processMainMenuInput(inp):
                break

            time.sleep(1)


    def processMainMenuInput(self,inp):
            if inp == "2":
                return True
            elif inp == "3":
                return True
            elif inp == "4":
                return True
            elif inp == "5":
                print()
                print()
                print ("Quitting.")
                print()
                print()
                return False
            else:
                print()
                print()
                print ("Invalid selection.")
                print()
                print()
                return True

    def is_positive_int(self,inp):
        is_positive_int = False
        try:
            int (inp)
            is_positive_int = int(inp) >= 0
        except ValueError:
            is_positive_int = False

        return is_positive_int

    def is_float(self,inp):
        is_float = False
        try:
            float (inp)
            is_float = True
        except ValueError:
            is_float = False

        return is_float









if __name__ == "__main__":
    g = GridWorld()



