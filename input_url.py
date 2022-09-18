class InputCheck:
    """
    Check if the input list len and return the Value: Int
    """

    def __init__(self, input) -> None:
        self.input = input

    def check_multi_or_single(self):
        if len(self.input) == 0 or None:
            return False

        else:
            input_values = len(self.input)
            return input_values
