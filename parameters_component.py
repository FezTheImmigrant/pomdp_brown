import json

class ParametersComponent:
    Walls = []
    EndStates = []
    Row = 0
    Col = 0
    Reward = 0
    Lambda = 0
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

        for end_state in data["EndStates"]:


            if not len(end_state) == 3:
                print ("An end state takes only three parameters: (row,column,utility)")
                return False

            if not self.is_positive_int(end_state[0]) or not self.is_positive_int(end_state[1]):
                print ("The first two parameters for an end state must be positive integer parameters")
                return False
            if not self.is_float(end_state[2]):
                print ("The third parameter for an end state must be a float.")
            
            self.EndStates.append(end_state)

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
