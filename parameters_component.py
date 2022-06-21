import json


class ParametersComponent:
    walls = []
    end_states = []
    row = 0
    col = 0
    reward = 0
    lamb = 0

    def load_parameters(self, file_name):
        """
        Returns True if parameters from 'parameters.json' are valid.

            Parameters:

                filename: (str): parameter file name

            Returns:
                is_valid: (bool): Boolean of whether or not parameters are valid.
        """

        f = open(file_name, "r")

        data = json.loads(f.read())

        if not self.__load_row(data):
            return False
        if not self.__load_column(data):
            return False
        if not self.__load_reward(data):
            return False
        if not self.__load_lambda(data):
            return False
        if not self.__load_walls(data):
            return False
        if not self.__load_end_states(data):
            return False

        return True

    def __load_row(self, data):
        """
        Returns True if row parameter from 'parameters.json' is a positive integer.

            Parameters:

                data: (dict): dictionary containing parameter data for grid.

            Returns:
                is_valid: (bool): Boolean of whether or not row parameter is valid.
        """

        if self.__is_positive_int(data["Rows"]):
            self.row = int(data["Rows"])
        else:
            print("Row parameter must be a postive integer value.")
            return False

        return True

    def __load_column(self, data):
        """loads column parameter from 'parameters.json. Returns False if column is not a postive integer'"""

        if self.__is_positive_int(data["Columns"]):
            self.col = int(data["Columns"])
        else:
            print("Column parameter must be a positive integer value.")
            return False

        return True

    def __load_reward(self, data):
        """loads reward parameter from 'parameters.json. Returns False if reward is not a float'"""

        if self.__is_float(data["Reward"]):
            self.reward = float(data["Reward"])
        else:
            print("Reward parameter must be a float value.")
            return False

        return True

    def __load_lambda(self, data):
        """loads lambda parameter from 'parameters.json. Returns False if lambda is not a float'"""

        if self.__is_float(data["Lambda"]):
            self.lamb = float(data["Lambda"])
        else:
            print("Lambda parameter must be a float value.")
            return False

        return True

    def __load_walls(self, data):
        """loads wall parameters from 'parameters.json. Returns False if a wall is not in form [row,column]'"""

        for wall in data["Walls"]:

            if not len(wall) == 2:
                print("A wall takes only two parameters: (row,column)")
                return False

            if not self.__is_positive_int(wall[0]) or not self.__is_positive_int(
                wall[1]
            ):
                print("A wall takes only positive integer parameters")
                return False

            self.walls.append(wall)

        return True

    def __load_end_states(self, data):
        """loads end state parameters from 'parameters.json. Returns False if a wall is not in form [row,column,reward]'"""

        for end_state in data["EndStates"]:

            if not len(end_state) == 3:
                print("An end state takes only three parameters: (row,column,utility)")
                return False

            if not self.__is_positive_int(end_state[0]) or not self.__is_positive_int(
                end_state[1]
            ):
                print(
                    "The first two parameters for an end state must be positive integer parameters"
                )
                return False
            if not self.__is_float(end_state[2]):
                print("The third parameter for an end state must be a float.")

            self.end_states.append(end_state)

        return True

    def __is_positive_int(self, inp):
        """returns True if 'inp' is a positive integer"""
        is_positive_int = False
        try:
            int(inp)
            is_positive_int = int(inp) >= 0
        except ValueError:
            is_positive_int = False

        return is_positive_int

    def __is_float(self, inp):
        """returns True if 'inp' is a float"""
        is_float = False
        try:
            float(inp)
            is_float = True
        except ValueError:
            is_float = False

        return is_float
