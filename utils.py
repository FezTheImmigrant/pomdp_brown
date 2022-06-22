class Utils:
    @staticmethod
    def is_positive_int(inp):
        """
        Returns True if 'inp' parameter is a positive integer

            Parameters:

                inp: (object): python object

            Returns:
                is_valid: (bool): Boolean of whether or not 'inp' is valid.
        """

        is_positive_int = False
        try:
            int(inp)
            is_positive_int = int(inp) >= 0
        except ValueError:
            is_positive_int = False

        return is_positive_int

    @staticmethod
    def is_float(inp):
        """
        Returns True if 'inp' parameter is a float

            Parameters:

                inp: (object): python object

            Returns:
                is_valid: (bool): Boolean of whether or not 'inp' is valid.
        """

        is_float = False
        try:
            float(inp)
            is_float = True
        except ValueError:
            is_float = False

        return is_float
