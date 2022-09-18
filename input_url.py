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


# Test Cases
test_single = ["a"]
test_multi = ["a", "basd", "c", "d"]
test_null = []
s = InputCheck(test_single).check_multi_or_single()
print(s)
m = InputCheck(test_multi).check_multi_or_single()
print(m)
v = InputCheck(test_null).check_multi_or_single()
print(v)
